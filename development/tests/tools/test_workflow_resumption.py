from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/scripts/workflow.py"


class WorkflowResumptionIntegrationTests(unittest.TestCase):
    def run_cli(self, root: Path, command: str, *arguments: str) -> dict:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), command, "--project-root", str(root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        return json.loads(result.stdout)

    def test_three_conversations_resume_one_question_batch_without_duplication(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            # Conversation 1: initialize, build the Canvas, and present one complete batch.
            self.run_cli(root, "start", "--confirmed")
            self.run_cli(root, "select-stage", "--stage", "project-framing")
            self.run_cli(root, "set-delivery", "--additional-format", "none")
            self.run_cli(root, "set-source-strategy", "--mode", "external")
            self.run_cli(root, "confirm-inputs", "--description-provided")
            self.run_cli(root, "open-iteration")
            canvas = root / "_project-design" / "project-canvas.md"
            original_questions = (
                "# Project Canvas\n\n"
                "### 9. Questions\n\n"
                "1. Which approval authority is required?\n"
                "2. Which user group is in the MVP?\n"
                "3. Which retention rule applies?\n"
                "4. Which success measure validates launch?\n"
            )
            canvas.write_text(original_questions, encoding="utf-8")
            presented = self.run_cli(
                root, "present-questions", "--questions-asked", "4"
            )
            self.assertEqual(presented["phase"], "awaiting_framing_answers")

            # Conversation 2: status alone resumes the existing batch and changes nothing.
            before_state = (root / "_project-design" / "project-design-state.json").read_text(
                encoding="utf-8"
            )
            resumed = self.run_cli(root, "status")
            self.assertIn("present or resume exactly those existing questions", resumed["next_action"])
            self.assertEqual(canvas.read_text(encoding="utf-8"), original_questions)
            self.assertEqual(
                (root / "_project-design" / "project-design-state.json").read_text(
                    encoding="utf-8"
                ),
                before_state,
            )
            self.assertEqual(len(resumed["state"]["framing"]["iterations"]), 0)

            # A partial answer updates only the Canvas and the control count.
            remaining_questions = (
                "# Project Canvas\n\n"
                "### 8. Decisions\n\n"
                "- The product owner is the approval authority.\n\n"
                "### 9. Questions\n\n"
                "1. Which user group is in the MVP?\n"
                "2. Which retention rule applies?\n"
                "3. Which success measure validates launch?\n"
            )
            canvas.write_text(remaining_questions, encoding="utf-8")
            partial = self.run_cli(root, "record-answers", "--answers-received", "1")
            self.assertIn("3 pending", partial["next_action"])

            # Conversation 3: only the remaining Canvas questions are resumed.
            third = self.run_cli(root, "status")
            self.assertEqual(third["phase"], "awaiting_framing_answers")
            self.assertEqual(
                third["state"]["framing"]["active_iteration"]["questions_pending"], 3
            )
            current_canvas = canvas.read_text(encoding="utf-8")
            self.assertEqual(current_canvas, remaining_questions)
            self.assertNotIn("Which approval authority is required?", current_canvas)
            self.assertEqual(len(third["state"]["framing"]["iterations"]), 0)


if __name__ == "__main__":
    unittest.main()
