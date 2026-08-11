---
name: project-design
description: Run a strongly guided application or software specification workflow by presenting project-design skills, obtaining explicit consent, persisting and enforcing each workflow transition, proposing project-framing as the default first stage, collecting documentary choices and project inputs in order, and handing business and document work to implemented specialized skills. Use when starting, resuming, or checking a project-design specification workflow. Complete multi-discipline orchestration remains under construction.
---

# Project Design

## Status

IMPLEMENTED — STATEFUL GUIDED ENTRY VERSION 0.3; COMPLETE ORCHESTRATION NOT IMPLEMENTED

Use the bundled state machine to enforce the implemented guided chain. Do not
replace its transitions with conversational memory or an informal checklist.

## Purpose

Guide the user through consent, project workspace initialization, stage
selection, delivery choice, source intake, iterative framing, Canvas approval,
and optional documentary restitution. Persist non-business workflow state so a
new conversation can resume without losing or skipping the current step.

## Mandatory State Machine

Resolve `scripts/workflow.py` relative to this skill directory. It owns:

```text
_project-design/project-design-state.json
```

The state file records consent, current phase, selected stage, documentary
choice, presence of inputs, iteration counts, approval, delivery references,
source-workspace mode, and transition history. It must not contain the project description, source
contents, question text, answers, or Canvas business knowledge.

Before every substantive workflow action, run:

```text
python3 scripts/workflow.py status --project-root <project-root>
```

Follow only the returned `next_action`. After each user answer or completed
skill action, run the matching transition command. If a command returns
`status: error`, stop that transition, report the reason, and remain at the
current phase. Never edit the state JSON manually and never infer that a phase
was completed from conversation history alone.

## Guided Workflow

### 1. Present the Plugin and Obtain Consent

Apply the shared
[Invocation Brief and Project Workspace Delivery contract](../../shared/quality-rules/README.md).
Briefly present:

- `project-framing` — implemented step 1, producing the Project Canvas;
- `document-project-canvas` — implemented optional Markdown, Word, or Google
  Docs restitution of a validated Canvas;
- `functional-design`, `technical-design`, `product-backlog`, and their
  document skills — installed placeholders whose methodologies do not run.

Explain the `_project-design/` workspace and state file. Ask the user to
confirm use of the plugin for the project specifications. This is a mandatory
stop point. A refusal creates nothing.

After explicit agreement, run:

```text
python3 scripts/workflow.py start \
  --project-root <project-root> \
  --confirmed
```

`start` safely creates or reuses `_project-design/` and `documents/`, creates
the state file on first use, and resumes it unchanged on later calls.

### 2. Select the Stage

When the state phase is `awaiting_stage`, ask which stage to perform and
propose `project-framing` explicitly as the default. Do not present a
placeholder as executable.

After the user selects the implemented stage, run:

```text
python3 scripts/workflow.py select-stage \
  --project-root <project-root> \
  --stage project-framing
```

### 3. Resolve Documentary Delivery

When the phase is `awaiting_delivery`, present `project-framing`, its ten
Canvas chapters, mandatory `_project-design/project-canvas.md`, and the
optional document choices.

Record Markdown-only delivery with:

```text
python3 scripts/workflow.py set-delivery \
  --project-root <project-root> \
  --additional-format none
```

For Word or Google Docs, use `docx` or `google-docs` and require one template
mode:

- `default` — built-in professional structure, no reference;
- `local` — requires `--template-reference <path>`;
- `drive` — requires `--template-reference <url>`.

Example:

```text
python3 scripts/workflow.py set-delivery \
  --project-root <project-root> \
  --additional-format docx \
  --template-mode default
```

### 4. Choose the Source Strategy

When the phase is `awaiting_source_strategy`, ask whether sources should:

- remain at their original locations (`external`); or
- be centralized in the optional root-level `_sources/` workspace
  (`centralized`).

Centralization requires explicit confirmation. Record the choice with:

```text
python3 scripts/workflow.py set-source-strategy \
  --project-root <project-root> \
  --mode centralized \
  --confirmed
```

Use `--mode external` without `--confirmed` when originals remain in place.
For centralized mode, the command creates `_sources/documents/`,
`_sources/source-index.md`, and `_sources/links.md`, then adds `/_sources/` to
the target project's `.gitignore` without duplicating the rule.

Use `scripts/source_workspace.py add-local` only after explicit consent to
copy each local file. It never overwrites an existing destination and records
the original path and SHA-256 in the index. Use `add-link` for native Google
Drive, Docs, Sheets, or Slides sources; record the link without exporting it.
Never modify an original source.

### 5. Obtain Initial Project Inputs

When the phase is `awaiting_sources`, ask for a project description in the
conversation, source documents, or both. Do not store their contents in the
state file.

After at least one input form is actually available, run `confirm-inputs` with
`--description-provided`, `--documents-provided`, or both.

### 6. Run Iterative Project Framing

When the phase is `framing_iterations`, invoke `project-framing`. Build or
update the working Markdown Canvas and ask one to three high-value questions.
After receiving or explicitly deferring the answers, record the round:

```text
python3 scripts/workflow.py record-iteration \
  --project-root <project-root> \
  --questions-asked <1-3> \
  --answers-received <0-3>
```

Add `--ready-for-review` only when the working Canvas is ready for an explicit
user review. The command rejects more than three questions. It records counts,
not question or answer content.

If the user requests another iteration from `awaiting_canvas_approval`, run:

```text
python3 scripts/workflow.py continue-framing --project-root <project-root>
```

### 7. Approve the Canvas

When the phase is `awaiting_canvas_approval`, ask the user to approve the
current saved Canvas. After explicit approval, run:

```text
python3 scripts/workflow.py approve-canvas \
  --project-root <project-root> \
  --confirmed
```

Approval is rejected unless `_project-design/project-canvas.md` exists and is
non-empty. Markdown-only delivery then becomes `complete`; an external format
moves to `awaiting_document`.

### 8. Produce and Record the Optional Document

When the phase is `awaiting_document`, invoke `document-project-canvas` using
the recorded format and template choice. After native verification, record:

- Word with `complete-document --document-file <verified-docx-path>`;
- Google Docs with `complete-document --document-url <verified-native-url>`.

The state becomes `complete` only when the required native delivery reference
passes validation.

## Recovery and Resumption

On a new conversation or an ambiguous continuation, run `status`, summarize
the current phase and recorded choices, then perform only `next_action`. Calling
`start --confirmed` on an existing valid state resumes it and never resets it.
There is intentionally no reset command; replacing established workflow state
requires an explicit future recovery policy.

## Boundaries

- Keep business methodology in `project-framing` and documentary methodology
  in `document-project-canvas`.
- Store no project knowledge, confidential source text, questions, or answers
  in the workflow state.
- Keep `_sources/` separate from the `_project-design/` delivery workspace and
  ignore it from Git by default.
- Never advance a phase without a successful script transition.
- Never initialize before explicit consent or reset an existing state.
- Never execute a placeholder methodology.
- Do not require GitHub Spec Kit or a platform-specific runtime.
- Do not invent unsupported project information.

## Future Routing

Complete routing across functional design, technical design, and backlog work,
automatic cross-artefact consistency, and founded upstream revision remain
future orchestration. The current executable chain is only:

```text
project-design
    -> project-framing
    -> document-project-canvas (when requested)
```

## Shared References

- [Project model](../../shared/project-model/README.md)
- [Quality rules](../../shared/quality-rules/README.md)
- [Terminology](../../shared/terminology/README.md)
- [Spec Kit boundary](../../shared/spec-kit-boundary.md)
