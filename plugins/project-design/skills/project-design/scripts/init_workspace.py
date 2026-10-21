#!/usr/bin/env python3
"""Safely initialize the project-design delivery and source workspaces."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


class WorkspaceError(ValueError):
    """Raised when a workspace target is unsafe or unusable."""


def emit(status: str, **values: object) -> None:
    print(json.dumps({"status": status, **values}, sort_keys=True))


def resolve_project_root(value: str) -> Path:
    root = Path(value).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise WorkspaceError("project root must be an existing directory")
    if root == Path(root.anchor) or root == Path.home().resolve():
        raise WorkspaceError("filesystem root and home directory are not valid targets")
    return root


def initialize_workspace(
    root: Path, dry_run: bool = False, sources: bool = True
) -> dict[str, object]:
    """Create _project-design and, by default, the _sources intake workspace."""
    # Imported here because source_workspace reuses this module's helpers.
    from source_workspace import initialize_source_workspace

    workspace = root / "_project-design"
    documents = workspace / "documents"
    for target in (workspace, documents):
        if target.exists() and not target.is_dir():
            raise WorkspaceError(f"target exists and is not a directory: {target}")
    if sources:
        # Validate the source targets before creating anything.
        initialize_source_workspace(root, dry_run=True)

    existed = workspace.is_dir() and documents.is_dir()
    source_result = None
    if not dry_run:
        documents.mkdir(parents=True, exist_ok=True)
    if sources:
        source_result = initialize_source_workspace(root, dry_run=dry_run)
        existed = existed and source_result["result"] == "existing"
    result: dict[str, object] = {
        "status": "dry-run" if dry_run else ("existing" if existed else "created"),
        "project_root": str(root),
        "workspace": str(workspace),
        "documents": str(documents),
    }
    if source_result is not None:
        result["sources"] = source_result
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create _project-design, its documents directory, and _sources."
    )
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--confirmed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.confirmed:
        emit("error", error="explicit user confirmation is required")
        return 2
    try:
        root = resolve_project_root(args.project_root)
        result = initialize_workspace(root, args.dry_run)
    except WorkspaceError as error:
        emit("error", error=str(error))
        return 2
    emit(**result)
    return 0


if __name__ == "__main__":
    # Run through the importable module so WorkspaceError raised by
    # source_workspace is the same class as the one caught by main().
    import init_workspace

    raise SystemExit(init_workspace.main())
