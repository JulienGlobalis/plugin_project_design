from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/scripts/init_workspace.py"


class InitializeWorkspaceTests(unittest.TestCase):
    def run_script(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_confirmation_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_script("--project-root", directory)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["status"], "error")
            self.assertFalse((Path(directory) / "_project-design").exists())

    def test_dry_run_creates_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_script("--project-root", directory, "--confirmed", "--dry-run")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)["status"], "dry-run")
            self.assertFalse((Path(directory) / "_project-design").exists())

    def test_initialization_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = self.run_script("--project-root", directory, "--confirmed")
            second = self.run_script("--project-root", directory, "--confirmed")
            self.assertEqual(json.loads(first.stdout)["status"], "created")
            self.assertEqual(json.loads(second.stdout)["status"], "existing")
            self.assertTrue((Path(directory) / "_project-design" / "documents").is_dir())

    def test_existing_file_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "_project-design"
            workspace.write_text("preserve", encoding="utf-8")
            result = self.run_script("--project-root", directory, "--confirmed")
            self.assertEqual(result.returncode, 2)
            self.assertEqual(workspace.read_text(encoding="utf-8"), "preserve")


if __name__ == "__main__":
    unittest.main()
