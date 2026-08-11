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
SCHEMA_VERSION = 3


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
    migrated = False
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
        schema_version = 2
        state["schema_version"] = schema_version
        state.setdefault("history", []).append(
            {"event": "workflow_state_migrated_to_v2", "at": now()}
        )
        migrated = True
    if schema_version == 2:
        framing = state.setdefault("framing", {})
        framing["active_iteration"] = None
        for iteration in framing.setdefault("iterations", []):
            iteration.setdefault("status", "legacy_recorded")
            iteration.setdefault("resolution_status", "legacy_ambiguous")
        if state.get("phase") == "framing_iterations":
            state["phase"] = "framing_recovery"
            framing["recovery"] = {
                "reason": "legacy_framing_state_ambiguous",
                "questions_asked": None,
                "answers_received": None,
                "questions_deferred": None,
                "questions_pending": None,
            }
        state["schema_version"] = SCHEMA_VERSION
        state.setdefault("history", []).append(
            {"event": "workflow_state_migrated_to_v3", "at": now()}
        )
        migrated = True
    elif schema_version != SCHEMA_VERSION:
        raise WorkflowError(f"unsupported workflow schema version: {schema_version}")
    if migrated:
        save_state(root, state)
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
    phase = state["phase"]
    if phase == "awaiting_framing_answers":
        iteration = state["framing"]["active_iteration"]
        pending = iteration["questions_pending"]
        if pending == 0:
            return (
                "All presented questions are accounted for. Close the question batch; "
                "do not open or record another iteration yet."
            )
        return (
            "Read the currently unanswered business questions in the Questions section "
            "of _project-design/project-canvas.md and present or resume exactly those "
            f"existing questions ({pending} pending) without inventing new ones. Wait for "
            "answers or an explicit deferral, update the Canvas only from answers actually "
            "received, and record only the corresponding counts. Do not open or record a "
            "new iteration while this batch is pending. A conversation change or technical "
            "transition request is neither an answer nor a deferral."
        )
    return {
        "awaiting_stage": "Ask the user to select a stage; propose project-framing by default.",
        "awaiting_delivery": "Ask whether Word or Google Docs is required in addition to Markdown and resolve the template mode.",
        "awaiting_source_strategy": "Ask whether sources should remain at their original locations or be centralized in _sources.",
        "awaiting_sources": "Collect the project description and source references using the selected source strategy.",
        "framing_iterations": "Open one framing iteration before analyzing sources or changing the working Canvas.",
        "framing_iteration_preparation": "Use project-framing to analyze the available information, update _project-design/project-canvas.md, identify every necessary decision question, present the complete non-duplicated batch to the user, then record the number actually presented.",
        "framing_iteration_completion": "Update the Canvas from the recorded answers, keep unresolved or explicitly deferred questions visible as appropriate, then complete the active iteration and choose another iteration or Canvas review.",
        "framing_recovery": "This migrated framing state is ambiguous. Read the Questions section of _project-design/project-canvas.md without changing or duplicating it, then explicitly recover the existing presented batch with its observed count or confirm that a new iteration may be prepared. Do not infer answers, deferrals, or pending counts from legacy counters.",
        "awaiting_canvas_approval": "Ask the user to approve the saved Project Canvas or continue framing iterations.",
        "awaiting_document": "Use document-project-canvas with the recorded delivery choice, verify the native result, then record delivery.",
        "complete": "Report the completed guided workflow and preserve the state file for future continuation.",
    }[phase]


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
        "schema_version": SCHEMA_VERSION,
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
        "framing": {
            "iterations": [],
            "active_iteration": None,
            "canvas_approved": False,
        },
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


def open_iteration(state: dict[str, Any]) -> None:
    require_phase(state, "framing_iterations")
    if state["framing"].get("active_iteration") is not None:
        raise WorkflowError("a framing iteration is already active")
    timestamp = now()
    state["framing"]["active_iteration"] = {
        "number": len(state["framing"]["iterations"]) + 1,
        "status": "preparing",
        "questions_asked": None,
        "answers_received": 0,
        "questions_deferred": 0,
        "questions_pending": None,
        "opened_at": timestamp,
    }
    state["phase"] = "framing_iteration_preparation"
    append_event(state, "framing_iteration_opened")


def active_iteration(state: dict[str, Any]) -> dict[str, Any]:
    iteration = state["framing"].get("active_iteration")
    if not isinstance(iteration, dict):
        raise WorkflowError("no framing iteration is active")
    return iteration


def present_questions(state: dict[str, Any], questions: int) -> None:
    require_phase(state, "framing_iteration_preparation")
    if questions < 0:
        raise WorkflowError("questions asked must be zero or greater")
    iteration = active_iteration(state)
    iteration.update(
        {
            "status": "awaiting_answers" if questions else "question_batch_closed",
            "questions_asked": questions,
            "questions_pending": questions,
            "presented_at": now(),
        }
    )
    if questions:
        state["phase"] = "awaiting_framing_answers"
        append_event(state, "framing_questions_presented")
    else:
        iteration["batch_closed_at"] = now()
        state["phase"] = "framing_iteration_completion"
        append_event(state, "framing_question_batch_empty")


def record_answers(state: dict[str, Any], answers: int) -> None:
    require_phase(state, "awaiting_framing_answers")
    if answers < 1:
        raise WorkflowError("answers received must be greater than zero")
    iteration = active_iteration(state)
    if answers > iteration["questions_pending"]:
        raise WorkflowError("answers received cannot exceed pending questions")
    iteration["answers_received"] += answers
    iteration["questions_pending"] -= answers
    append_event(state, "framing_answers_recorded")


def defer_questions(state: dict[str, Any], questions: int, confirmed: bool) -> None:
    require_phase(state, "awaiting_framing_answers")
    if not confirmed:
        raise WorkflowError("explicit user deferral is required")
    if questions < 1:
        raise WorkflowError("questions deferred must be greater than zero")
    iteration = active_iteration(state)
    if questions > iteration["questions_pending"]:
        raise WorkflowError("questions deferred cannot exceed pending questions")
    iteration["questions_deferred"] += questions
    iteration["questions_pending"] -= questions
    append_event(state, "framing_questions_deferred")


def close_question_batch(state: dict[str, Any]) -> None:
    require_phase(state, "awaiting_framing_answers")
    iteration = active_iteration(state)
    if iteration["questions_pending"] != 0:
        raise WorkflowError(
            "cannot close question batch while questions remain unanswered or not deferred"
        )
    if (
        iteration["answers_received"] + iteration["questions_deferred"]
        != iteration["questions_asked"]
    ):
        raise WorkflowError("answer and deferral counts do not cover the presented questions")
    iteration["status"] = "question_batch_closed"
    iteration["batch_closed_at"] = now()
    state["phase"] = "framing_iteration_completion"
    append_event(state, "framing_question_batch_closed")


def complete_iteration(state: dict[str, Any], ready_for_review: bool) -> None:
    require_phase(state, "framing_iteration_completion")
    iteration = active_iteration(state)
    iteration["status"] = "completed"
    iteration["ready_for_review"] = ready_for_review
    iteration["completed_at"] = now()
    state["framing"]["iterations"].append(iteration)
    state["framing"]["active_iteration"] = None
    state["phase"] = (
        "awaiting_canvas_approval" if ready_for_review else "framing_iterations"
    )
    append_event(state, "framing_iteration_completed")


def resolve_framing_recovery(
    state: dict[str, Any], mode: str, questions: int | None, confirmed: bool
) -> None:
    require_phase(state, "framing_recovery")
    if not confirmed:
        raise WorkflowError("explicit recovery confirmation is required")
    if mode == "pending-questions":
        if questions is None or questions < 1:
            raise WorkflowError("pending-question recovery requires a positive observed count")
        timestamp = now()
        state["framing"]["active_iteration"] = {
            "number": len(state["framing"]["iterations"]) + 1,
            "status": "awaiting_answers",
            "questions_asked": questions,
            "answers_received": 0,
            "questions_deferred": 0,
            "questions_pending": questions,
            "opened_at": timestamp,
            "presented_at": timestamp,
            "recovered_from_legacy_state": True,
        }
        state["phase"] = "awaiting_framing_answers"
        append_event(state, "legacy_question_batch_recovered")
    else:
        if questions is not None:
            raise WorkflowError("new-iteration recovery does not accept a question count")
        state["phase"] = "framing_iterations"
        append_event(state, "legacy_framing_recovery_resolved")
    state["framing"].pop("recovery", None)


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
    command("open-iteration")
    question_parser = command("present-questions")
    question_parser.add_argument("--questions-asked", type=int, required=True)
    answer_parser = command("record-answers")
    answer_parser.add_argument("--answers-received", type=int, required=True)
    defer_parser = command("defer-questions")
    defer_parser.add_argument("--questions-deferred", type=int, required=True)
    defer_parser.add_argument("--confirmed", action="store_true")
    command("close-question-batch")
    completion_parser = command("complete-iteration")
    completion_parser.add_argument("--ready-for-review", action="store_true")
    recovery_parser = command("resolve-framing-recovery")
    recovery_parser.add_argument(
        "--mode", choices=("pending-questions", "new-iteration"), required=True
    )
    recovery_parser.add_argument("--questions-asked", type=int)
    recovery_parser.add_argument("--confirmed", action="store_true")
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
            elif args.command == "open-iteration":
                open_iteration(state)
            elif args.command == "present-questions":
                present_questions(state, args.questions_asked)
            elif args.command == "record-answers":
                record_answers(state, args.answers_received)
            elif args.command == "defer-questions":
                defer_questions(state, args.questions_deferred, args.confirmed)
            elif args.command == "close-question-batch":
                close_question_batch(state)
            elif args.command == "complete-iteration":
                complete_iteration(state, args.ready_for_review)
            elif args.command == "resolve-framing-recovery":
                resolve_framing_recovery(
                    state, args.mode, args.questions_asked, args.confirmed
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
