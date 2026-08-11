from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPOSITORY_ROOT / "plugins/project-design/skills/project-design/scripts/source_workspace.py"


class SourceWorkspaceTests(unittest.TestCase):
    def run_cli(self, root: Path, command: str, *arguments: str) -> tuple[subprocess.CompletedProcess[str], dict]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), command, "--project-root", str(root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )
        return result, json.loads(result.stdout)

    def test_initialization_requires_confirmation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result, output = self.run_cli(root, "init")
            self.assertEqual(result.returncode, 2)
            self.assertIn("confirmation", output["error"])
            self.assertFalse((root / "_sources").exists())

    def test_initialization_creates_index_links_documents_and_gitignore(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result, output = self.run_cli(root, "init", "--confirmed")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(output["result"], "created")
            self.assertTrue((root / "_sources" / "documents").is_dir())
            self.assertTrue((root / "_sources" / "source-index.md").is_file())
            self.assertTrue((root / "_sources" / "links.md").is_file())
            self.assertEqual((root / ".gitignore").read_text(encoding="utf-8"), "/_sources/\n")

    def test_initialization_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.run_cli(root, "init", "--confirmed")
            _, output = self.run_cli(root, "init", "--confirmed")
            self.assertEqual(output["result"], "existing")
            self.assertEqual((root / ".gitignore").read_text(encoding="utf-8").count("/_sources/"), 1)

    def test_local_copy_requires_confirmation_and_never_overwrites(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as source_directory:
            root = Path(directory)
            source = Path(source_directory) / "brief.md"
            source.write_text("project brief", encoding="utf-8")
            self.run_cli(root, "init", "--confirmed")
            denied, _ = self.run_cli(root, "add-local", "--source", str(source))
            self.assertEqual(denied.returncode, 2)
            accepted, output = self.run_cli(
                root, "add-local", "--source", str(source), "--confirmed-copy"
            )
            self.assertEqual(accepted.returncode, 0)
            self.assertTrue(Path(output["destination"]).is_file())
            duplicate, _ = self.run_cli(
                root, "add-local", "--source", str(source), "--confirmed-copy"
            )
            self.assertEqual(duplicate.returncode, 2)

    def test_drive_link_is_indexed_without_export(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.run_cli(root, "init", "--confirmed")
            result, _ = self.run_cli(
                root, "add-link", "--label", "Discovery notes",
                "--url", "https://docs.google.com/document/d/example/edit"
            )
            self.assertEqual(result.returncode, 0)
            self.assertIn("Discovery notes", (root / "_sources" / "links.md").read_text(encoding="utf-8"))
            self.assertEqual(list((root / "_sources" / "documents").iterdir()), [])

    def test_non_google_remote_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.run_cli(root, "init", "--confirmed")
            result, output = self.run_cli(
                root, "add-link", "--label", "Other", "--url", "https://example.com/source"
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("Google Drive", output["error"])

    def test_source_workspace_symlink_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            (root / "_sources").symlink_to(outside, target_is_directory=True)
            result, output = self.run_cli(root, "init", "--confirmed")
            self.assertEqual(result.returncode, 2)
            self.assertIn("symbolic link", output["error"])


if __name__ == "__main__":
    unittest.main()
