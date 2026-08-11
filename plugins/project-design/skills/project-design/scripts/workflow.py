#!/usr/bin/env python3
"""Enforce and persist the guided project-design workflow state."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
from typing import Any

from init_workspace import WorkspaceError, initialize_workspace, resolve_project_root
from source_workspace import initialize_source_workspace


STATE_NAME = "project-design-state.json"
CANVAS_NAME = "project-canvas.md"


class WorkflowError(ValueError):
    """Raised when a requested workflow transition is invalid."""


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def emit(status: str, **values: object) -> None:
    print(json.dumps({"status": status, **values}, ensure_ascii=False, sort_keys=True))


def state_path(root: Path) -> Path:
    return root / "_project-design" / STATE_NAME


def load_state(root: Path) -> dict[str, Any]:
    path = state_path(root)
    if not path.is_file():
        raise WorkflowError("workflow is not initialized; run start after user consent")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise WorkflowError(f"workflow state is unreadable: {error}") from error
    if state.get("project_root") != str(root):
        raise WorkflowError("workflow state belongs to a different project root")
    schema_version = state.get("schema_version", 1)
    if schema_version == 1:
        state["source_workspace"] = {
            "mode": None,
            "path": None,
            "gitignored": False,
        }
        if state.get("phase") == "awaiting_sources":
            state["phase"] = "awaiting_source_strategy"
        elif state.get("phase") in {
            "framing_iterations", "awaiting_canvas_approval",
            "awaiting_document", "complete"
        }:
            state["source_workspace"]["mode"] = "external"
        state["schema_version"] = 2
        state.setdefault("history", []).append(
            {"event": "workflow_state_migrated_to_v2", "at": now()}
        )
        save_state(root, state)
    elif schema_version != 2:
        raise WorkflowError(f"unsupported workflow schema version: {schema_version}")
    return state


def save_state(root: Path, state: dict[str, Any]) -> None:
    path = state_path(root)
    state["updated_at"] = now()
    handle = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, prefix=".state-", delete=False
    )
    temporary = Path(handle.name)
    try:
        with handle:
            json.dump(state, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def next_action(state: dict[str, Any]) -> str:
    return {
        "awaiting_stage": "Ask the user to select a stage; propose project-framing by default.",
        "awaiting_delivery": "Ask whether Word or Google Docs is required in addition to Markdown and resolve the template mode.",
        "awaiting_source_strategy": "Ask whether sources should remain at their original locations or be centralized in _sources.",
        "awaiting_sources": "Collect the project description and source references using the selected source strategy.",
        "framing_iterations": "Use project-framing, ask at most three high-value questions, update the working Canvas, then record the iteration.",
        "awaiting_canvas_approval": "Ask the user to approve the saved Project Canvas or continue framing iterations.",
        "awaiting_document": "Use document-project-canvas with the recorded delivery choice, verify the native result, then record delivery.",
        "complete": "Report the completed guided workflow and preserve the state file for future continuation.",
    }[state["phase"]]


def require_phase(state: dict[str, Any], expected: str) -> None:
    if state["phase"] != expected:
        raise WorkflowError(
            f"transition requires phase {expected}; current phase is {state['phase']}"
        )


def append_event(state: dict[str, Any], event: str) -> None:
    state["history"].append({"event": event, "at": now()})


def start(root: Path, confirmed: bool) -> dict[str, Any]:
    if not confirmed:
        raise WorkflowError("explicit user confirmation is required")
    initialize_workspace(root)
    path = state_path(root)
    if path.exists():
        return load_state(root)
    timestamp = now()
    state: dict[str, Any] = {
        "schema_version": 2,
        "project_root": str(root),
        "phase": "awaiting_stage",
        "consent": {"confirmed": True, "confirmed_at": timestamp},
        "stage": None,
        "delivery": {
            "markdown_path": "_project-design/project-canvas.md",
            "additional_format": None,
            "template_mode": None,
            "template_reference": None,
        },
        "inputs": {"description_provided": False, "documents_provided": False},
        "source_workspace": {"mode": None, "path": None, "gitignored": False},
        "framing": {"iterations": [], "canvas_approved": False},
        "document": {"file": None, "url": None},
        "history": [{"event": "workflow_started", "at": timestamp}],
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    save_state(root, state)
    return state


def select_stage(state: dict[str, Any], stage: str) -> None:
    require_phase(state, "awaiting_stage")
    if stage != "project-framing":
        raise WorkflowError(f"stage is not implemented: {stage}")
    state["stage"] = stage
    state["phase"] = "awaiting_delivery"
    append_event(state, "stage_selected")


def set_delivery(
    state: dict[str, Any], output_format: str, template_mode: str | None,
    template_reference: str | None
) -> None:
    require_phase(state, "awaiting_delivery")
    if output_format == "none":
        if template_mode or template_reference:
            raise WorkflowError("template options require an additional document format")
        selected_format = None
    else:
        if template_mode is None:
            raise WorkflowError("template mode is required for Word or Google Docs")
        if template_mode in {"local", "drive"} and not template_reference:
            raise WorkflowError("local and Drive template modes require a template reference")
        if template_mode == "default" and template_reference:
            raise WorkflowError("default template mode does not accept a template reference")
        if template_mode == "local" and not Path(template_reference).expanduser().is_file():
            raise WorkflowError("local template reference must be an existing file")
        if template_mode == "drive" and not template_reference.startswith(
            ("https://drive.google.com/", "https://docs.google.com/")
        ):
            raise WorkflowError("Drive template reference must be a Google Drive URL")
        selected_format = output_format
    state["delivery"].update(
        {
            "additional_format": selected_format,
            "template_mode": template_mode,
            "template_reference": template_reference,
        }
    )
    state["phase"] = "awaiting_source_strategy"
    append_event(state, "delivery_selected")


def set_source_strategy(
    root: Path, state: dict[str, Any], mode: str, confirmed: bool
) -> None:
    require_phase(state, "awaiting_source_strategy")
    if mode == "centralized":
        if not confirmed:
            raise WorkflowError("explicit confirmation is required to create or reuse _sources")
        initialize_source_workspace(root)
        state["source_workspace"] = {
            "mode": mode,
            "path": "_sources",
            "gitignored": True,
        }
        append_event(state, "source_workspace_initialized")
    else:
        state["source_workspace"] = {
            "mode": "external",
            "path": None,
            "gitignored": False,
        }
        append_event(state, "external_sources_selected")
    state["phase"] = "awaiting_sources"


def confirm_inputs(state: dict[str, Any], description: bool, documents: bool) -> None:
    require_phase(state, "awaiting_sources")
    if not description and not documents:
        raise WorkflowError("a project description, source documents, or both are required")
    state["inputs"] = {
        "description_provided": description,
        "documents_provided": documents,
    }
    state["phase"] = "framing_iterations"
    append_event(state, "inputs_confirmed")


def record_iteration(
    state: dict[str, Any], questions: int, answers: int, ready_for_review: bool
) -> None:
    require_phase(state, "framing_iterations")
    if questions < 1 or questions > 3:
        raise WorkflowError("each framing iteration must contain one to three questions")
    if answers < 0 or answers > questions:
        raise WorkflowError("answers received must be between zero and questions asked")
    state["framing"]["iterations"].append(
        {
            "number": len(state["framing"]["iterations"]) + 1,
            "questions_asked": questions,
            "answers_received": answers,
            "recorded_at": now(),
        }
    )
    state["phase"] = "awaiting_canvas_approval" if ready_for_review else "framing_iterations"
    append_event(state, "framing_iteration_recorded")


def continue_framing(state: dict[str, Any]) -> None:
    require_phase(state, "awaiting_canvas_approval")
    state["phase"] = "framing_iterations"
    append_event(state, "canvas_review_deferred")


def approve_canvas(root: Path, state: dict[str, Any], confirmed: bool) -> None:
    require_phase(state, "awaiting_canvas_approval")
    if not confirmed:
        raise WorkflowError("explicit Canvas approval is required")
    canvas = root / "_project-design" / CANVAS_NAME
    if not canvas.is_file() or not canvas.read_text(encoding="utf-8").strip():
        raise WorkflowError("a non-empty _project-design/project-canvas.md is required")
    state["framing"]["canvas_approved"] = True
    state["framing"]["canvas_path"] = str(canvas)
    state["phase"] = (
        "awaiting_document"
        if state["delivery"]["additional_format"] is not None
        else "complete"
    )
    append_event(state, "canvas_approved")


def complete_document(
    root: Path, state: dict[str, Any], document_file: str | None,
    document_url: str | None
) -> None:
    require_phase(state, "awaiting_document")
    output_format = state["delivery"]["additional_format"]
    if output_format == "docx":
        if not document_file:
            raise WorkflowError("Word delivery requires --document-file")
        path = Path(document_file).expanduser().resolve()
        if not path.is_file() or path.suffix.lower() != ".docx":
            raise WorkflowError("Word delivery must reference an existing .docx file")
        try:
            path.relative_to(root / "_project-design" / "documents")
        except ValueError as error:
            raise WorkflowError(
                "Word delivery must be stored under _project-design/documents"
            ) from error
        state["document"]["file"] = str(path)
    elif output_format == "google-docs":
        if not document_url or not document_url.startswith("https://docs.google.com/document/"):
            raise WorkflowError("Google Docs delivery requires a native document URL")
        state["document"]["url"] = document_url
    else:
        raise WorkflowError("no external document is configured")
    state["phase"] = "complete"
    append_event(state, "document_delivered")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    def command(name: str) -> argparse.ArgumentParser:
        child = subparsers.add_parser(name)
        child.add_argument("--project-root", required=True)
        return child

    command("status")
    start_parser = command("start")
    start_parser.add_argument("--confirmed", action="store_true")
    stage_parser = command("select-stage")
    stage_parser.add_argument("--stage", required=True)
    delivery_parser = command("set-delivery")
    delivery_parser.add_argument(
        "--additional-format", choices=("none", "docx", "google-docs"), required=True
    )
    delivery_parser.add_argument("--template-mode", choices=("default", "local", "drive"))
    delivery_parser.add_argument("--template-reference")
    input_parser = command("confirm-inputs")
    input_parser.add_argument("--description-provided", action="store_true")
    input_parser.add_argument("--documents-provided", action="store_true")
    source_parser = command("set-source-strategy")
    source_parser.add_argument("--mode", choices=("external", "centralized"), required=True)
    source_parser.add_argument("--confirmed", action="store_true")
    iteration_parser = command("record-iteration")
    iteration_parser.add_argument("--questions-asked", type=int, required=True)
    iteration_parser.add_argument("--answers-received", type=int, required=True)
    iteration_parser.add_argument("--ready-for-review", action="store_true")
    command("continue-framing")
    approval_parser = command("approve-canvas")
    approval_parser.add_argument("--confirmed", action="store_true")
    document_parser = command("complete-document")
    document_parser.add_argument("--document-file")
    document_parser.add_argument("--document-url")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        root = resolve_project_root(args.project_root)
        if args.command == "start":
            state = start(root, args.confirmed)
        else:
            state = load_state(root)
            if args.command == "select-stage":
                select_stage(state, args.stage)
            elif args.command == "set-delivery":
                set_delivery(
                    state, args.additional_format, args.template_mode,
                    args.template_reference
                )
            elif args.command == "confirm-inputs":
                confirm_inputs(
                    state, args.description_provided, args.documents_provided
                )
            elif args.command == "set-source-strategy":
                set_source_strategy(root, state, args.mode, args.confirmed)
            elif args.command == "record-iteration":
                record_iteration(
                    state, args.questions_asked, args.answers_received,
                    args.ready_for_review
                )
            elif args.command == "continue-framing":
                continue_framing(state)
            elif args.command == "approve-canvas":
                approve_canvas(root, state, args.confirmed)
            elif args.command == "complete-document":
                complete_document(root, state, args.document_file, args.document_url)
            if args.command != "status":
                save_state(root, state)
        emit("ok", phase=state["phase"], next_action=next_action(state), state=state)
        return 0
    except (WorkflowError, WorkspaceError, OSError) as error:
        emit("error", error=str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
