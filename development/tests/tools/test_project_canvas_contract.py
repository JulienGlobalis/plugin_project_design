from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPOSITORY_ROOT / "plugins/project-design/skills/project-framing"
EXAMPLE = SKILL_ROOT / "references/project-canvas-example.md"
FRAMING_SKILL = SKILL_ROOT / "SKILL.md"
CANVAS_REFERENCE = SKILL_ROOT / "references/project-canvas.md"
ORCHESTRATOR_SKILL = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/SKILL.md"
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


    def section(self, number: int) -> str:
        following = re.split(rf"^### {number}\.", self.canvas, flags=re.MULTILINE)[1]
        return re.split(r"^##+ (?:\d+\.|Capacité)", following, flags=re.MULTILINE)[0]

    @staticmethod
    def rows(section: str, header: str) -> list[list[str]]:
        lines = section.splitlines()
        start = lines.index(header)
        rows = []
        for line in lines[start + 2:]:
            if not line.startswith("|"):
                break
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
        return rows

    def test_example_uses_the_four_mandatory_tables(self) -> None:
        scope_header = "| Module | Fonctionnalité | Description succincte |"
        scope = self.section(5)
        self.assertEqual(scope.count(scope_header), 2)
        self.assertLess(scope.index("#### MVP"), scope.index("#### Hors MVP"))
        self.assertIn("| Risque | Impact | Solution |", self.section(7))
        self.assertIn("| Thème | Décision |", self.section(8))
        self.assertIn("| N° | Question | Réponse |", self.section(9))

    def test_example_features_start_with_an_infinitive_verb(self) -> None:
        mvp, outside = self.section(5).split("#### Hors MVP")
        header = "| Module | Fonctionnalité | Description succincte |"
        features = [row[1] for part in (mvp, outside) for row in self.rows(part, header)]
        self.assertGreaterEqual(len(features), 3)
        for feature in features:
            self.assertRegex(feature.split()[0], r"(?:er|ir|re)$", feature)
        self.assertEqual(len(features), len(set(features)))

    def test_example_services_are_bullets_after_the_mvp_table(self) -> None:
        mvp = self.section(5).split("#### Hors MVP")[0]
        self.assertRegex(mvp, r"\|\n\nPrestations incluses :\n\n- ")

    def test_example_questions_keep_stable_numbers_and_answers(self) -> None:
        rows = self.rows(self.section(9), "| N° | Question | Réponse |")
        self.assertEqual([row[0] for row in rows], [str(n) for n in range(1, len(rows) + 1)])
        self.assertIn("À apporter", [row[2] for row in rows])
        self.assertTrue(any(row[2] not in {"À apporter", "Reportée"} for row in rows))
        self.assertIn("question n° 1", self.canvas.split("## Capacité à poursuivre", 1)[1])

    def test_reference_defines_tables_and_feature_formulation(self) -> None:
        reference = CANVAS_REFERENCE.read_text(encoding="utf-8")
        for required in (
            "## Tabular Sections (Mandatory Format)",
            "`Module | Feature | Short description`",
            "`Risk | Impact | Solution`",
            "`Topic | Decision`",
            "`No. | Question | Answer`",
            "`To be provided` (FR: `À apporter`)",
            "### Feature Formulation Rules",
            "**[Nouveau]**",
        ):
            self.assertIn(required, reference)

    def test_framing_boundary_expects_a_feature_inventory(self) -> None:
        self.assertIn("A feature inventory in the Functional", self.framing_skill)
        self.assertNotIn("Do not produce detailed modules, features", self.framing_skill)
        self.assertIn("#### Source Extraction", self.framing_skill)
        self.assertIn("Candidate\nquestions for the next batch", self.framing_skill)

    def test_orchestrator_has_no_mandatory_source_strategy_step(self) -> None:
        orchestrator = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        self.assertNotIn("awaiting_source_strategy", orchestrator)
        self.assertIn("Start always creates `_sources/documents/`", orchestrator)


if __name__ == "__main__":
    unittest.main()
