#!/usr/bin/env python3
"""Create and maintain the optional project source workspace."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
from urllib.parse import urlparse

from init_workspace import WorkspaceError, resolve_project_root


INDEX_HEADER = """# Source Index

This inventory records the project sources made available to project-design.
Original sources remain authoritative and are never modified by this workspace.

| Added at | Kind | Reference | Original location | SHA-256 |
| --- | --- | --- | --- | --- |
"""

LINKS_HEADER = """# Source Links

Remote sources are referenced here and are not exported automatically.

"""


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def emit(status: str, **values: object) -> None:
    print(json.dumps({"status": status, **values}, ensure_ascii=False, sort_keys=True))


def source_paths(root: Path) -> tuple[Path, Path, Path, Path]:
    workspace = root / "_sources"
    return (
        workspace,
        workspace / "documents",
        workspace / "source-index.md",
        workspace / "links.md",
    )


def ensure_gitignore(root: Path, dry_run: bool = False) -> bool:
    path = root / ".gitignore"
    if path.is_symlink():
        raise WorkspaceError(".gitignore must not be a symbolic link")
    if path.exists() and not path.is_file():
        raise WorkspaceError(".gitignore exists and is not a file")
    rule = "/_sources/"
    existing = path.read_text(encoding="utf-8") if path.is_file() else ""
    if rule in {line.strip() for line in existing.splitlines()}:
        return False
    if not dry_run:
        prefix = "" if not existing or existing.endswith("\n") else "\n"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(f"{prefix}{rule}\n")
    return True


def initialize_source_workspace(root: Path, dry_run: bool = False) -> dict[str, object]:
    workspace, documents, index, links = source_paths(root)
    for target in (workspace, documents, index, links):
        if target.is_symlink():
            raise WorkspaceError(f"source workspace target must not be a symbolic link: {target}")
    for target in (workspace, documents):
        if target.exists() and not target.is_dir():
            raise WorkspaceError(f"target exists and is not a directory: {target}")
    for target in (index, links):
        if target.exists() and not target.is_file():
            raise WorkspaceError(f"target exists and is not a file: {target}")

    existed = all(target.exists() for target in (documents, index, links))
    gitignore_updated = ensure_gitignore(root, dry_run=dry_run)
    if not dry_run:
        documents.mkdir(parents=True, exist_ok=True)
        if not index.exists():
            index.write_text(INDEX_HEADER, encoding="utf-8")
        if not links.exists():
            links.write_text(LINKS_HEADER, encoding="utf-8")
    return {
        "workspace": str(workspace),
        "documents": str(documents),
        "index": str(index),
        "links": str(links),
        "gitignore_updated": gitignore_updated,
        "result": "dry-run" if dry_run else ("existing" if existed else "created"),
    }


def require_initialized(root: Path) -> tuple[Path, Path, Path, Path]:
    paths = source_paths(root)
    if not all(target.exists() for target in paths):
        raise WorkspaceError("_sources is not initialized")
    return paths


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def append_index(index: Path, kind: str, reference: str, origin: str, digest: str = "-") -> None:
    row = "| {} | {} | {} | {} | {} |\n".format(
        now(), kind, escape_table(reference), escape_table(origin), digest
    )
    with index.open("a", encoding="utf-8") as handle:
        handle.write(row)


def add_local_file(root: Path, source_value: str, confirmed: bool) -> dict[str, str]:
    if not confirmed:
        raise WorkspaceError("explicit confirmation is required before copying a local source")
    _, documents, index, _ = require_initialized(root)
    source = Path(source_value).expanduser().resolve()
    if not source.is_file():
        raise WorkspaceError("local source must be an existing file")
    destination = documents / source.name
    if destination.exists():
        raise WorkspaceError(f"destination already exists and will not be overwritten: {destination}")
    hasher = hashlib.sha256()
    with source.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    digest = hasher.hexdigest()
    shutil.copy2(source, destination)
    append_index(index, "local-copy", destination.name, str(source), digest)
    return {"source": str(source), "destination": str(destination), "sha256": digest}


def add_remote_link(root: Path, label: str, url: str) -> dict[str, str]:
    _, _, index, links = require_initialized(root)
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc not in {
        "drive.google.com", "docs.google.com", "sheets.google.com", "slides.google.com"
    }:
        raise WorkspaceError("remote source must be a Google Drive, Docs, Sheets, or Slides URL")
    safe_label = label.replace("\n", " ").replace("[", "").replace("]", "").strip()
    if not safe_label:
        raise WorkspaceError("remote source label is required")
    with links.open("a", encoding="utf-8") as handle:
        handle.write(f"- [{safe_label}]({url})\n")
    append_index(index, "remote-link", safe_label, url)
    return {"label": safe_label, "url": url}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    def command(name: str) -> argparse.ArgumentParser:
        child = subparsers.add_parser(name)
        child.add_argument("--project-root", required=True)
        return child

    init_parser = command("init")
    init_parser.add_argument("--confirmed", action="store_true")
    init_parser.add_argument("--dry-run", action="store_true")
    local_parser = command("add-local")
    local_parser.add_argument("--source", required=True)
    local_parser.add_argument("--confirmed-copy", action="store_true")
    link_parser = command("add-link")
    link_parser.add_argument("--label", required=True)
    link_parser.add_argument("--url", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        root = resolve_project_root(args.project_root)
        if args.command == "init":
            if not args.confirmed:
                raise WorkspaceError("explicit user confirmation is required")
            result = initialize_source_workspace(root, dry_run=args.dry_run)
        elif args.command == "add-local":
            result = add_local_file(root, args.source, args.confirmed_copy)
        else:
            result = add_remote_link(root, args.label, args.url)
        emit("ok", **result)
        return 0
    except (WorkspaceError, OSError) as error:
        emit("error", error=str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
