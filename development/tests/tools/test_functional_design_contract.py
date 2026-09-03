from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPOSITORY_ROOT / "plugins/project-design/skills/functional-design"
SKILL = SKILL_ROOT / "SKILL.md"
STRUCTURE = SKILL_ROOT / "references/functional-design.md"
CHECKLIST = SKILL_ROOT / "references/quality-checklist.md"
EXAMPLE = SKILL_ROOT / "references/functional-design-example.md"


class FunctionalDesignContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.structure = STRUCTURE.read_text(encoding="utf-8")
        cls.checklist = CHECKLIST.read_text(encoding="utf-8")
        cls.example = EXAMPLE.read_text(encoding="utf-8")

    def test_skill_is_implemented_and_links_runtime_references(self) -> None:
        self.assertIn("IMPLEMENTED — METHODOLOGY VERSION 0.1", self.skill)
        self.assertNotIn("installed entry is a placeholder", self.skill.lower())
        for reference in (
            "references/functional-design.md",
            "references/quality-checklist.md",
            "references/functional-design-example.md",
        ):
            self.assertIn(reference, self.skill)

    def test_living_artefact_contract_is_explicit(self) -> None:
        for term in (
            "stable identifiers",
            "Addition",
            "Clarification",
            "Correction",
            "Deprecation",
            "Replacement",
            "change history",
        ):
            self.assertIn(term, self.skill + self.structure)

    def test_requested_structure_is_covered(self) -> None:
        for heading in (
            "## 1. Actors and Roles",
            "## 2. General Specifications",
            "### 2.1 Global Processes",
            "### 2.2 Product, Module, and Feature Inventory",
            "## 3. Detailed Functional Specifications",
            "#### General Information",
            "#### Nominal Scenario",
            "#### Alternative Valid Scenarios",
            "#### Errors and Exceptions",
            "#### Acceptance Criteria",
            "#### Questions and Required Decisions",
            "#### Interfaces and Fields",
            "#### Feature-Specific Business Rules",
            "#### Messages",
            "## 4. Annexes",
            "### 4.1 Global Message Catalog",
        ):
            self.assertIn(heading, self.structure)

    def test_example_inventory_and_details_have_the_same_features(self) -> None:
        inventory = set(re.findall(r"^\| (FNC-\d+) \|", self.example, re.MULTILINE))
        details = set(
            re.findall(r"^### 3\.\d+ (FNC-\d+) —", self.example, re.MULTILINE)
        )
        self.assertTrue(inventory)
        self.assertEqual(inventory, details)

    def test_example_message_references_resolve_to_catalog(self) -> None:
        referenced = set(re.findall(r"\bMSG-\d+\b", self.example))
        catalog_match = re.search(
            r"### 4\.1 Catalogue global des messages\n(?P<body>.*?)(?:\n## |\Z)",
            self.example,
            re.DOTALL,
        )
        self.assertIsNotNone(catalog_match)
        defined = set(
            re.findall(r"^\| (MSG-\d+) \|", catalog_match.group("body"), re.MULTILINE)
        )
        self.assertTrue(defined)
        self.assertEqual(referenced, defined)

    def test_boundaries_exclude_technical_design_and_backlog_content(self) -> None:
        combined = self.skill + self.checklist
        for excluded in (
            "database schema",
            "API design",
            "implementation task",
            "priority",
            "estimate",
            "backlog",
            "document template",
        ):
            self.assertIn(excluded.lower(), combined.lower())

    def test_bundle_has_no_development_runtime_dependency(self) -> None:
        for path in SKILL_ROOT.rglob("*"):
            if path.is_file():
                content = path.read_text(encoding="utf-8")
                self.assertNotIn("development/", content, str(path))
                self.assertNotIn(".local/", content, str(path))


if __name__ == "__main__":
    unittest.main()
