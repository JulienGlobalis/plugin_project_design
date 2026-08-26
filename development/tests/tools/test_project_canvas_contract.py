from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPOSITORY_ROOT / "plugins/project-design/skills/project-framing"
EXAMPLE = SKILL_ROOT / "references/project-canvas-example.md"
FRAMING_SKILL = SKILL_ROOT / "SKILL.md"
DOCUMENT_SKILL_ROOT = REPOSITORY_ROOT / "plugins/project-design/skills/document-project-canvas"
DOCUMENT_SKILL = DOCUMENT_SKILL_ROOT / "SKILL.md"
DOCUMENT_STRUCTURE = DOCUMENT_SKILL_ROOT / "references/document-structure.md"
DOCUMENT_CHECKLIST = DOCUMENT_SKILL_ROOT / "references/quality-checklist.md"


class ProjectCanvasContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.canvas = EXAMPLE.read_text(encoding="utf-8")
        cls.framing_skill = FRAMING_SKILL.read_text(encoding="utf-8")
        cls.document_skill = DOCUMENT_SKILL.read_text(encoding="utf-8")
        cls.document_structure = DOCUMENT_STRUCTURE.read_text(encoding="utf-8")
        cls.document_checklist = DOCUMENT_CHECKLIST.read_text(encoding="utf-8")

    def test_authorized_rename_exposes_only_current_name(self) -> None:
        self.assertIn("Le nom officiel est Muzzo.", self.canvas)
        for former_name in ("Muzzo Booking", "RoomBooker"):
            self.assertNotIn(former_name, self.canvas)

    def test_undecided_alternatives_become_one_concise_question(self) -> None:
        self.assertIn(
            "Quel mode d'approbation des demandes doit être retenu pour le MVP ?",
            self.canvas,
        )
        self.assertNotRegex(self.canvas.lower(), r"contradic|source oppos|d'un côté")

    def test_proposed_capability_is_not_in_validated_scope(self) -> None:
        self.assertNotIn("automated access-code delivery", self.canvas)
        self.assertNotIn("codes d'accès automatiques", self.canvas)

    def test_empty_required_section_says_to_be_defined(self) -> None:
        technical = self.canvas.split("### 6. Contraintes techniques", 1)[1].split(
            "### 7. Risques", 1
        )[0]
        self.assertEqual(technical.strip(), "À définir.")

    def test_standard_canvas_contains_no_audit_mechanics(self) -> None:
        forbidden = (
            "Established",
            "Provisional",
            "Unresolved",
            "Établi",
            "Provisoire",
            "Non résolu",
            "historique",
            "traçabilité",
        )
        for term in forbidden:
            self.assertNotIn(term, self.canvas)
        self.assertIsNone(re.search(r"\bS[123]\b", self.canvas))

    def test_example_keeps_exactly_ten_canvas_sections(self) -> None:
        headings = re.findall(r"^### (\d+)\.", self.canvas, flags=re.MULTILINE)
        self.assertEqual(headings, [str(number) for number in range(1, 11)])

    def test_example_has_three_separate_downstream_readiness_conclusions(self) -> None:
        readiness = self.canvas.split("## Capacité à poursuivre", 1)[1]
        self.assertIn("### Conception fonctionnelle — Non prête", readiness)
        self.assertIn("### Conception technique — Prête avec réserves", readiness)
        self.assertIn("### Préparation du backlog — Non prête", readiness)

    def test_framing_requires_readiness_without_an_eleventh_canvas_section(self) -> None:
        self.assertIn("This companion assessment is mandatory", self.framing_skill)
        self.assertRegex(self.framing_skill, r"not an eleventh Canvas\s+section")
        for stage in ("functional-design", "technical-design", "backlog preparation"):
            self.assertIn(stage, self.framing_skill)

    def test_document_contract_forbids_unmapped_derived_narrative(self) -> None:
        for contract in (
            self.document_skill,
            self.document_structure,
            self.document_checklist,
        ):
            self.assertIn("subtitle", contract)
            self.assertIn("summary", contract)
            self.assertRegex(
                contract,
                re.compile(r"(?:open-)?question\s+count", flags=re.IGNORECASE),
            )
        self.assertIn("reverse check", self.document_skill)
        self.assertRegex(
            self.document_skill,
            r"explicit request for (?:a|that) combined\s+(?:document|scope)",
        )


if __name__ == "__main__":
    unittest.main()
