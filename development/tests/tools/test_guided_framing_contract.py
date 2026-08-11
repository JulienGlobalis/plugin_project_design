from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DESIGN_SKILL = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/SKILL.md"
PROJECT_FRAMING_SKILL = REPOSITORY_ROOT / "plugins/project-design/skills/project-framing/SKILL.md"
WORKFLOW = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/scripts/workflow.py"
ACTIVE_TESTS = REPOSITORY_ROOT / "development/tests/tools"


class GuidedFramingContractTests(unittest.TestCase):
    def test_skills_define_explicit_pending_answer_resumption(self) -> None:
        orchestration = PROJECT_DESIGN_SKILL.read_text(encoding="utf-8")
        framing = PROJECT_FRAMING_SKILL.read_text(encoding="utf-8")
        for required in (
            "framing_iteration_preparation",
            "awaiting_framing_answers",
            "framing_iteration_completion",
            "present-questions",
            "record-answers",
            "defer-questions",
            "close-question-batch",
            "complete-iteration",
        ):
            self.assertIn(required, orchestration)
        self.assertIn("read and resume only the unanswered questions", framing)
        self.assertIn("A deferral must be explicit", framing)

    def test_workflow_commands_have_one_transition_responsibility(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("record-iteration", workflow)
        self.assertRegex(workflow, r'command\("open-iteration"\)')
        self.assertRegex(workflow, r'command\("close-question-batch"\)')
        self.assertRegex(workflow, r'command\("complete-iteration"\)')

    def test_no_business_text_fields_are_defined_in_state(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        for forbidden in (
            '"question_text"',
            '"answer_text"',
            '"project_description"',
            '"canvas_content"',
        ):
            self.assertNotIn(forbidden, workflow)

    def test_active_contracts_contain_no_numeric_question_cap(self) -> None:
        files = [PROJECT_DESIGN_SKILL, PROJECT_FRAMING_SKILL, WORKFLOW]
        files.extend(ACTIVE_TESTS.glob("test_*.py"))
        patterns = (
            "one to " + "three",
            "1" + "-3",
            "at most " + "three",
            "up to " + "three",
            "three " + "questions",
            "trois " + "questions",
        )
        forbidden = re.compile("|".join(re.escape(item) for item in patterns), re.IGNORECASE)
        for path in files:
            self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), path)

    def test_questions_asked_acceptance_is_not_bounded_above(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('question_parser.add_argument("--questions-asked", type=int, required=True)', workflow)
        self.assertNotRegex(workflow, r"questions\s*>\s*\d")


if __name__ == "__main__":
    unittest.main()
