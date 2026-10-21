---
name: project-design
description: Guide a project manager through application or software framing with recommended next actions, supported decision choices, resumable questions, Canvas approval, and optional document delivery. Use when starting, resuming, or checking the project-design specification workflow. The persistent guided route covers framing; functional design is directly callable and complete multi-discipline orchestration remains future work.
---

# Project Design

## Status

IMPLEMENTED — STATEFUL GUIDED ENTRY VERSION 0.5; COMPLETE ORCHESTRATION NOT IMPLEMENTED

Use the bundled state machine to enforce the implemented guided chain. Do not
replace its transitions with conversational memory or an informal checklist.

## Purpose

Guide the user through consent, project workspace initialization, stage
selection, delivery choice, source intake, iterative framing, Canvas approval,
and optional documentary restitution. Persist non-business workflow state so a
new conversation can resume without losing or skipping the current step.

Before guiding the conversation, read and apply the
[Project Manager Interaction contract](references/project-manager-interaction.md)
for recommendations, decision support, progressive answers, explicit deferrals,
and actionable handoffs. Preserve the mandatory transitions below.

## Mandatory State Machine

Resolve `scripts/workflow.py` relative to this skill directory. It owns:

```text
_project-design/project-design-state.json
```

The state file records consent, current phase, selected stage, documentary
choice, presence of inputs, iteration and question-batch counters, approval,
delivery references, source-workspace mode, and transition history. It must not
contain the project description, source contents, question text, answer text, or
Canvas business knowledge.

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
- `functional-design` — implemented, independently callable creation, review,
  and controlled evolution of the Functional Design; the current guided state
  machine does not route it yet;
- `document-project-canvas` — implemented optional Markdown, Word, or Google
  Docs restitution of a validated Canvas;
- `technical-design`, `product-backlog`, and the three remaining document
  skills — installed placeholders whose methodologies do not run.

Explain the `_project-design/` workspace and state file. Ask the user to
confirm use of the plugin for the project specifications if that explicit
consent has not already been given for this scope. This is a mandatory
consent gate, not a repeated confirmation. A refusal creates nothing.

After explicit agreement, run:

```text
python3 scripts/workflow.py start \
  --project-root <project-root> \
  --confirmed
```

`start` safely creates or reuses `_project-design/` and `documents/`, and the
`_sources/` intake workspace (`documents/`, `source-index.md`, `links.md`),
adds `/_sources/` to the target project's `.gitignore` without duplicating the
rule, creates the state file on first use, and resumes it unchanged on later
calls. Presenting the plugin includes stating that `_sources/` will be created.

### 2. Select the Stage

When the state phase is `awaiting_stage`, explain that the current guided
state machine supports `project-framing` only and propose it explicitly as
the default. Do not present an unsupported route or placeholder as executable.

Reuse an explicit framing request as the stage selection; do not ask for the
same choice again. Otherwise recommend it and obtain the missing choice.
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

### 4. Use the Source Workspace

Delivery selection leads directly to `awaiting_sources`; there is no
separate source-strategy choice. Start always creates `_sources/documents/`,
ignored by Git. Invite the user to drop their source documents there, in any
format the active environment can read, or to provide them as links. Copying a
file located elsewhere still requires explicit approval, file by file. Index
every document present in `_sources/source-index.md`. Never modify an
original.

Use `scripts/source_workspace.py add-local` only after explicit consent to
copy each local file. It never overwrites an existing destination and records
the original path and SHA-256 in the index. Use `add-link` for native Google
Drive, Docs, Sheets, or Slides sources; record the link without exporting it.
After the user drops files into `_sources/documents/`, run
`scripts/source_workspace.py index-documents --project-root <project-root>`;
it records each not-yet-indexed file with its SHA-256 and changes none of them.

Keeping originals in place remains an optional opt-out, never a mandatory
question. Only when the user asks for it, record:

```text
python3 scripts/workflow.py set-source-strategy \
  --project-root <project-root> \
  --mode external
```

The opt-out never deletes `_sources/`. Returning to the centralized default
requires `--mode centralized --confirmed`.

### 5. Obtain Initial Project Inputs

When the phase is `awaiting_sources`, ask for a project description in the
conversation, source documents, or both. Do not store their contents in the
state file.

Sources may be supplied by files dropped into `_sources/documents/`, links,
approved copies, or original locations under the opt-out. After at least one
input form is actually available, run `confirm-inputs` with
`--description-provided`, `--documents-provided`, or both.

### 6. Run Iterative Project Framing

When the phase is `framing_iterations`, open exactly one iteration:

```text
python3 scripts/workflow.py open-iteration --project-root <project-root>
```

In `framing_iteration_preparation`, invoke `project-framing`, analyze the
available inputs, update the working Canvas, and identify every question that
genuinely conditions framing, functional design, technical design, backlog
preparation, or Canvas validation. Write the complete non-duplicated batch in
the Canvas `Questions` section and present that same batch to the user. There
is no numeric cap. Record only the number actually presented:

```text
python3 scripts/workflow.py present-questions \
  --project-root <project-root> \
  --questions-asked <count>
```

A zero count is valid when analysis finds no necessary question and moves
directly to iteration completion. A positive count moves to
`awaiting_framing_answers`.

In `awaiting_framing_answers`, read the existing unanswered questions from
`_project-design/project-canvas.md`. Present or resume those questions without
inventing or duplicating any. A new conversation, a request to save state, or
a technical transition instruction is not a business answer or a deferral.

When new questions emerge while a batch is pending, do not add them to the
Canvas. Present them in the delivery message under the heading `Candidate
questions for the next batch` (French: `Questions candidates pour le prochain
lot`), then open them in the next iteration once the current batch is settled.

For substantive answers, update only the affected Canvas content, write each
answer as the current result in the `Questions` table row of its question,
keep the remaining questions marked `To be provided`, and record the count
received:

```text
python3 scripts/workflow.py record-answers \
  --project-root <project-root> \
  --answers-received <count>
```

For questions the user explicitly defers, keep them in the Canvas section 9
table with the deferred marker in their answer cell, so resumption can
distinguish them from active questions still marked `To be provided`. Then
run:

```text
python3 scripts/workflow.py defer-questions \
  --project-root <project-root> \
  --questions-deferred <count> \
  --confirmed
```

Partial answers and partial deferrals leave the phase unchanged. Follow
`next_action`, which gives the remaining count and requires reading the actual
questions from the Canvas. The state file stores counts only.

When answers plus explicit deferrals cover the presented batch, close it:

```text
python3 scripts/workflow.py close-question-batch \
  --project-root <project-root>
```

The command refuses closure while any question remains unaccounted for. In
`framing_iteration_completion`, finish the Canvas update and close the active
iteration:

```text
python3 scripts/workflow.py complete-iteration \
  --project-root <project-root>
```

Add `--ready-for-review` only when the Canvas is ready for explicit review.
Otherwise the workflow returns to `framing_iterations` for a new explicit
iteration.

If the user requests another iteration from `awaiting_canvas_approval`, run:

```text
python3 scripts/workflow.py continue-framing --project-root <project-root>
```

### 7. Approve the Canvas

When the phase is `awaiting_canvas_approval`, ask the user to approve the
current saved Canvas after linking it and presenting material changes, remaining
blockers, and the three readiness conclusions. After explicit approval, run:

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

For Word, the script checks basic OOXML package structure. This does not
replace native rendering and semantic verification by `document-project-canvas`.
At completion, apply the interaction contract's actionable handoff; do not
describe the entire project as completed merely because framing is complete.

## Recovery and Resumption

On a new conversation or an ambiguous continuation, run `status`, summarize
the current phase and recorded choices, then perform only `next_action`. Calling
`start --confirmed` on an existing valid state resumes it and never resets it.
There is intentionally no reset command; replacing established workflow state
requires an explicit future recovery policy.

When `status` returns `awaiting_framing_answers`, read and present exactly the
unanswered questions already in the Canvas. Do not run `open-iteration` or
`present-questions`. Continue the existing batch until every question is
answered or explicitly deferred.

Migration of an older ambiguous `framing_iterations` state enters
`framing_recovery`. Inspect the Canvas without changing it, then use
`resolve-framing-recovery --confirmed` with either:

- `--mode pending-questions --questions-asked <observed-count>` when its
  current questions were already presented; or
- `--mode new-iteration` when no presented batch is pending.

Never infer a legacy answer, deferral, or pending count from old iteration
counters.

## Boundaries

- Keep business methodology in `project-framing` and documentary methodology
  in `document-project-canvas`.
- Store no project knowledge, confidential source text, questions, or answers
  in the workflow state.
- Never treat a conversation boundary or technical workflow request as a
  business answer or explicit deferral.
- Keep `_sources/` separate from the `_project-design/` delivery workspace,
  create it at start, and ignore it from Git by default.
- Never advance a phase without a successful script transition.
- Never initialize before explicit consent or reset an existing state.
- Never execute a placeholder methodology or invent an unsupported guided
  transition. `functional-design` remains directly callable outside this
  state machine when its input contract is satisfied.
- Do not require GitHub Spec Kit or a platform-specific runtime.
- Do not invent unsupported project information.

## Future Routing

Guided routing across functional design, technical design, and backlog work,
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
