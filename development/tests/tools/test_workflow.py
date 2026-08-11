from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/scripts/workflow.py"


class WorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_cli(self, command: str, *arguments: str) -> tuple[subprocess.CompletedProcess[str], dict]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), command, "--project-root", str(self.root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )
        return result, json.loads(result.stdout)

    def start(self) -> dict:
        result, output = self.run_cli("start", "--confirmed")
        self.assertEqual(result.returncode, 0, result.stderr)
        return output

    def advance_to_iterations(self, output_format: str = "none") -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        delivery = ["--additional-format", output_format]
        if output_format != "none":
            delivery.extend(["--template-mode", "default"])
        self.run_cli("set-delivery", *delivery)
        self.run_cli("confirm-inputs", "--description-provided")

    def test_start_requires_confirmation_and_creates_nothing(self) -> None:
        result, output = self.run_cli("start")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output["status"], "error")
        self.assertFalse((self.root / "_project-design").exists())

    def test_start_creates_persistent_state_and_is_resumable(self) -> None:
        first = self.start()
        second = self.start()
        self.assertEqual(first["phase"], "awaiting_stage")
        self.assertEqual(second["state"]["created_at"], first["state"]["created_at"])
        self.assertTrue((self.root / "_project-design" / "project-design-state.json").is_file())

    def test_steps_cannot_be_skipped(self) -> None:
        self.start()
        result, output = self.run_cli("set-delivery", "--additional-format", "none")
        self.assertEqual(result.returncode, 2)
        self.assertIn("requires phase awaiting_delivery", output["error"])

    def test_placeholder_stage_is_rejected(self) -> None:
        self.start()
        result, output = self.run_cli("select-stage", "--stage", "functional-design")
        self.assertEqual(result.returncode, 2)
        self.assertIn("not implemented", output["error"])

    def test_external_delivery_requires_template_mode(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        result, output = self.run_cli("set-delivery", "--additional-format", "docx")
        self.assertEqual(result.returncode, 2)
        self.assertIn("template mode is required", output["error"])

    def test_local_template_must_exist(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        result, output = self.run_cli(
            "set-delivery", "--additional-format", "docx", "--template-mode",
            "local", "--template-reference", str(self.root / "missing.docx")
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("existing file", output["error"])

    def test_drive_template_must_be_a_google_url(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        result, output = self.run_cli(
            "set-delivery", "--additional-format", "google-docs",
            "--template-mode", "drive", "--template-reference",
            "https://example.com/template"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Google Drive URL", output["error"])

    def test_inputs_are_required(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        self.run_cli("set-delivery", "--additional-format", "none")
        result, output = self.run_cli("confirm-inputs")
        self.assertEqual(result.returncode, 2)
        self.assertIn("description", output["error"])

    def test_iteration_rejects_more_than_three_questions(self) -> None:
        self.advance_to_iterations()
        result, output = self.run_cli(
            "record-iteration", "--questions-asked", "4", "--answers-received", "4"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("one to three", output["error"])

    def test_markdown_only_flow_completes_after_canvas_approval(self) -> None:
        self.advance_to_iterations()
        self.run_cli(
            "record-iteration", "--questions-asked", "2", "--answers-received", "2",
            "--ready-for-review"
        )
        canvas = self.root / "_project-design" / "project-canvas.md"
        canvas.write_text("# Project Canvas\n", encoding="utf-8")
        result, output = self.run_cli("approve-canvas", "--confirmed")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output["phase"], "complete")

    def test_canvas_approval_requires_a_non_empty_file(self) -> None:
        self.advance_to_iterations()
        self.run_cli(
            "record-iteration", "--questions-asked", "1", "--answers-received", "1",
            "--ready-for-review"
        )
        result, output = self.run_cli("approve-canvas", "--confirmed")
        self.assertEqual(result.returncode, 2)
        self.assertIn("non-empty", output["error"])

    def test_word_flow_requires_and_records_a_docx(self) -> None:
        self.advance_to_iterations("docx")
        self.run_cli(
            "record-iteration", "--questions-asked", "1", "--answers-received", "1",
            "--ready-for-review"
        )
        (self.root / "_project-design" / "project-canvas.md").write_text(
            "# Project Canvas\n", encoding="utf-8"
        )
        self.run_cli("approve-canvas", "--confirmed")
        result, _ = self.run_cli("complete-document")
        self.assertEqual(result.returncode, 2)
        document = self.root / "_project-design" / "documents" / "project-canvas.docx"
        document.write_bytes(b"PK test")
        result, output = self.run_cli("complete-document", "--document-file", str(document))
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output["phase"], "complete")


if __name__ == "__main__":
    unittest.main()
