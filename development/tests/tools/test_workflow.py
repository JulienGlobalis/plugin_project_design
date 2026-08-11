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
        self.assertTrue(result.stdout, result.stderr)
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
        self.run_cli("set-source-strategy", "--mode", "external")
        self.run_cli("confirm-inputs", "--description-provided")

    def open_question_batch(self, questions: int) -> dict:
        self.run_cli("open-iteration")
        result, output = self.run_cli(
            "present-questions", "--questions-asked", str(questions)
        )
        self.assertEqual(result.returncode, 0)
        return output

    def complete_answered_iteration(self, questions: int, ready: bool = False) -> dict:
        self.open_question_batch(questions)
        self.run_cli("record-answers", "--answers-received", str(questions))
        self.run_cli("close-question-batch")
        arguments = ("--ready-for-review",) if ready else ()
        return self.run_cli("complete-iteration", *arguments)[1]

    def state_file(self) -> Path:
        return self.root / "_project-design" / "project-design-state.json"

    def test_start_requires_confirmation_and_creates_nothing(self) -> None:
        result, output = self.run_cli("start")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output["status"], "error")
        self.assertFalse((self.root / "_project-design").exists())

    def test_start_creates_v3_state_and_is_resumable(self) -> None:
        first = self.start()
        second = self.start()
        self.assertEqual(first["state"]["schema_version"], 3)
        self.assertEqual(second["state"]["created_at"], first["state"]["created_at"])
        self.assertTrue(self.state_file().is_file())

    def test_v1_state_migrates_through_v2_to_v3_without_losing_history(self) -> None:
        initial = self.start()["state"]
        initial["schema_version"] = 1
        initial["phase"] = "awaiting_sources"
        initial.pop("source_workspace")
        self.state_file().write_text(json.dumps(initial), encoding="utf-8")
        result, output = self.run_cli("status")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output["state"]["schema_version"], 3)
        self.assertEqual(output["phase"], "awaiting_source_strategy")
        events = [item["event"] for item in output["state"]["history"]]
        self.assertEqual(events.count("workflow_state_migrated_to_v2"), 1)
        self.assertEqual(events.count("workflow_state_migrated_to_v3"), 1)
        self.assertEqual(output["state"]["history"][0]["event"], "workflow_started")

    def test_v2_ambiguous_framing_state_migrates_cautiously_and_idempotently(self) -> None:
        initial = self.start()["state"]
        initial["schema_version"] = 2
        initial["phase"] = "framing_iterations"
        initial["stage"] = "project-framing"
        initial["delivery"].update(
            {"additional_format": "docx", "template_mode": "default"}
        )
        initial["source_workspace"] = {
            "mode": "external", "path": None, "gitignored": False
        }
        initial["framing"] = {
            "iterations": [{"number": 1, "questions_asked": 4, "answers_received": 2}],
            "canvas_approved": False,
        }
        self.state_file().write_text(json.dumps(initial), encoding="utf-8")
        _, first = self.run_cli("status")
        _, second = self.run_cli("status")
        self.assertEqual(first["phase"], "framing_recovery")
        recovery = first["state"]["framing"]["recovery"]
        self.assertIsNone(recovery["questions_pending"])
        self.assertIsNone(recovery["questions_deferred"])
        self.assertEqual(first["state"]["stage"], "project-framing")
        self.assertEqual(first["state"]["delivery"]["additional_format"], "docx")
        self.assertEqual(first["state"]["source_workspace"]["mode"], "external")
        self.assertEqual(first["state"]["framing"]["iterations"][0]["number"], 1)
        self.assertEqual(
            first["state"]["history"], second["state"]["history"]
        )

    def test_legacy_recovery_requires_explicit_choice(self) -> None:
        initial = self.start()["state"]
        initial["schema_version"] = 2
        initial["phase"] = "framing_iterations"
        self.state_file().write_text(json.dumps(initial), encoding="utf-8")
        self.run_cli("status")
        result, output = self.run_cli(
            "resolve-framing-recovery", "--mode", "pending-questions",
            "--questions-asked", "5"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("explicit recovery", output["error"])
        _, recovered = self.run_cli(
            "resolve-framing-recovery", "--mode", "pending-questions",
            "--questions-asked", "5", "--confirmed"
        )
        self.assertEqual(recovered["phase"], "awaiting_framing_answers")
        self.assertEqual(
            recovered["state"]["framing"]["active_iteration"]["questions_pending"], 5
        )

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
        self.run_cli("set-source-strategy", "--mode", "external")
        result, output = self.run_cli("confirm-inputs")
        self.assertEqual(result.returncode, 2)
        self.assertIn("description", output["error"])

    def test_source_strategy_is_required_before_inputs(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        _, delivery = self.run_cli("set-delivery", "--additional-format", "none")
        self.assertEqual(delivery["phase"], "awaiting_source_strategy")
        result, output = self.run_cli("confirm-inputs", "--description-provided")
        self.assertEqual(result.returncode, 2)
        self.assertIn("awaiting_sources", output["error"])

    def test_centralized_source_strategy_requires_confirmation(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        self.run_cli("set-delivery", "--additional-format", "none")
        result, output = self.run_cli("set-source-strategy", "--mode", "centralized")
        self.assertEqual(result.returncode, 2)
        self.assertIn("explicit confirmation", output["error"])
        self.assertFalse((self.root / "_sources").exists())

    def test_centralized_source_strategy_initializes_private_workspace(self) -> None:
        self.start()
        self.run_cli("select-stage", "--stage", "project-framing")
        self.run_cli("set-delivery", "--additional-format", "none")
        result, output = self.run_cli(
            "set-source-strategy", "--mode", "centralized", "--confirmed"
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output["phase"], "awaiting_sources")
        self.assertTrue((self.root / "_sources" / "documents").is_dir())
        self.assertIn("/_sources/", (self.root / ".gitignore").read_text(encoding="utf-8"))

    def test_present_questions_accepts_more_than_three(self) -> None:
        self.advance_to_iterations()
        output = self.open_question_batch(7)
        iteration = output["state"]["framing"]["active_iteration"]
        self.assertEqual(output["phase"], "awaiting_framing_answers")
        self.assertEqual(iteration["questions_asked"], 7)
        self.assertEqual(iteration["questions_pending"], 7)

    def test_status_resumes_existing_batch_without_recording_an_iteration(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(5)
        before = json.loads(self.state_file().read_text(encoding="utf-8"))
        _, output = self.run_cli("status")
        after = json.loads(self.state_file().read_text(encoding="utf-8"))
        self.assertIn("Questions section", output["next_action"])
        self.assertIn("without inventing new ones", output["next_action"])
        self.assertEqual(output["phase"], "awaiting_framing_answers")
        self.assertEqual(len(output["state"]["framing"]["iterations"]), 0)
        self.assertEqual(before, after)

    def test_partial_answers_keep_only_remaining_count_pending(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(6)
        _, output = self.run_cli("record-answers", "--answers-received", "2")
        iteration = output["state"]["framing"]["active_iteration"]
        self.assertEqual(output["phase"], "awaiting_framing_answers")
        self.assertEqual(iteration["answers_received"], 2)
        self.assertEqual(iteration["questions_pending"], 4)
        self.assertIn("4 pending", output["next_action"])

    def test_partial_and_complete_explicit_deferral(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(5)
        self.run_cli("record-answers", "--answers-received", "2")
        _, partial = self.run_cli(
            "defer-questions", "--questions-deferred", "1", "--confirmed"
        )
        self.assertEqual(
            partial["state"]["framing"]["active_iteration"]["questions_pending"], 2
        )
        _, complete = self.run_cli(
            "defer-questions", "--questions-deferred", "2", "--confirmed"
        )
        iteration = complete["state"]["framing"]["active_iteration"]
        self.assertEqual(iteration["questions_deferred"], 3)
        self.assertEqual(iteration["questions_pending"], 0)

    def test_deferral_requires_explicit_confirmation(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(2)
        result, output = self.run_cli("defer-questions", "--questions-deferred", "2")
        self.assertEqual(result.returncode, 2)
        self.assertIn("explicit user deferral", output["error"])
        _, status = self.run_cli("status")
        iteration = status["state"]["framing"]["active_iteration"]
        self.assertEqual(iteration["questions_pending"], 2)
        self.assertEqual(iteration["questions_deferred"], 0)

    def test_technical_transition_cannot_close_or_defer_pending_questions(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(3)
        result, output = self.run_cli("close-question-batch")
        self.assertEqual(result.returncode, 2)
        self.assertIn("remain unanswered or not deferred", output["error"])
        result, output = self.run_cli("complete-iteration")
        self.assertEqual(result.returncode, 2)
        self.assertIn("framing_iteration_completion", output["error"])

    def test_all_answers_close_batch_and_complete_iteration(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(4)
        self.run_cli("record-answers", "--answers-received", "4")
        _, closed = self.run_cli("close-question-batch")
        self.assertEqual(closed["phase"], "framing_iteration_completion")
        _, completed = self.run_cli("complete-iteration")
        self.assertEqual(completed["phase"], "framing_iterations")
        self.assertEqual(len(completed["state"]["framing"]["iterations"]), 1)
        self.assertIsNone(completed["state"]["framing"]["active_iteration"])

    def test_completed_iteration_can_move_to_canvas_approval(self) -> None:
        self.advance_to_iterations()
        output = self.complete_answered_iteration(4, ready=True)
        self.assertEqual(output["phase"], "awaiting_canvas_approval")

    def test_next_iteration_gets_next_number(self) -> None:
        self.advance_to_iterations()
        self.complete_answered_iteration(1)
        output = self.open_question_batch(5)
        self.assertEqual(
            output["state"]["framing"]["active_iteration"]["number"], 2
        )

    def test_zero_question_iteration_can_be_completed(self) -> None:
        self.advance_to_iterations()
        self.run_cli("open-iteration")
        _, presented = self.run_cli("present-questions", "--questions-asked", "0")
        self.assertEqual(presented["phase"], "framing_iteration_completion")
        _, completed = self.run_cli("complete-iteration", "--ready-for-review")
        self.assertEqual(completed["phase"], "awaiting_canvas_approval")

    def test_markdown_only_flow_completes_after_canvas_approval(self) -> None:
        self.advance_to_iterations()
        self.complete_answered_iteration(4, ready=True)
        canvas = self.root / "_project-design" / "project-canvas.md"
        canvas.write_text("# Project Canvas\n", encoding="utf-8")
        result, output = self.run_cli("approve-canvas", "--confirmed")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output["phase"], "complete")

    def test_canvas_approval_requires_a_non_empty_file(self) -> None:
        self.advance_to_iterations()
        self.complete_answered_iteration(1, ready=True)
        result, output = self.run_cli("approve-canvas", "--confirmed")
        self.assertEqual(result.returncode, 2)
        self.assertIn("non-empty", output["error"])

    def test_word_flow_requires_and_records_a_docx(self) -> None:
        self.advance_to_iterations("docx")
        self.complete_answered_iteration(1, ready=True)
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

    def test_state_contains_control_metadata_but_no_business_text(self) -> None:
        self.advance_to_iterations()
        self.open_question_batch(4)
        self.run_cli("record-answers", "--answers-received", "1")
        serialized = self.state_file().read_text(encoding="utf-8")
        self.assertNotIn("Which approval mode", serialized)
        self.assertNotIn("The sponsor answered", serialized)
        state = json.loads(serialized)
        iteration = state["framing"]["active_iteration"]
        self.assertEqual(
            set(iteration).intersection({"question_text", "answer_text", "project_description"}),
            set(),
        )


if __name__ == "__main__":
    unittest.main()
