# Framing Question Resumption Review — 2026-08-11

## Scope

Corrected framing-question lifecycle and cross-conversation resumption in the
implemented `project-design -> project-framing` workflow. The change removes
the former numeric question cap, separates question presentation from answer
and iteration recording, supports partial answers and explicit deferrals, and
keeps all business text in the Project Canvas or conversation.

## Root Cause

The former `record-iteration` transition combined question presentation,
answer accounting, iteration closure, and review readiness. Until that command
ran, the persisted phase remained `framing_iterations`, so a new conversation
could not distinguish a new analysis round from an already-presented batch
whose answers were pending.

## Implemented State Model

The workflow state schema is version 3. Framing now follows:

```text
framing_iterations
-> framing_iteration_preparation
-> awaiting_framing_answers
-> framing_iteration_completion
-> framing_iterations | awaiting_canvas_approval
```

The dedicated commands are `open-iteration`, `present-questions`,
`record-answers`, `defer-questions`, `close-question-batch`, and
`complete-iteration`. Counts are control metadata only. Question text, answer
text, source content, project descriptions, and Canvas content are never
written to the state file.

Schema-2 framing states that may represent either a new iteration or an
unrecorded presented batch migrate to `framing_recovery`. Recovery requires an
explicit choice and never derives answers, deferrals, or pending counts from a
legacy counter. Migration is idempotent.

## Validation Results

| Check | Result |
| --- | --- |
| Python tool-test suite | PASS — 51 tests |
| Three-conversation resumption scenario | PASS |
| Pending batch larger than the former cap | PASS — 7 questions accepted |
| Partial answers and targeted resumption | PASS |
| Partial and complete explicit deferrals | PASS |
| Premature batch or iteration closure | PASS — rejected without state change |
| Schema 1 and schema 2 migration | PASS |
| Migration idempotence | PASS |
| State business-text exclusion | PASS |
| Numeric-cap repository search | PASS — no obsolete expression found |
| Skill Creator validation | PASS — 9/9 skills valid |
| Plugin Creator validation | PASS |
| Claude plugin validation | PASS |
| Plugin dependency on `development/` | PASS — none found |
| Git whitespace validation | PASS |
| Installed bundle comparison | PASS — source and cache identical |

The first direct validator attempt with the system Python failed because
`PyYAML` was unavailable. The repository-standard isolated
`uv run --with pyyaml` execution passed for every skill and the plugin.

## Packaging

The Plugin Creator cachebuster helper produced
`0.1.0+codex.20260811161924`. The plugin was reinstalled from the local
`project-design` marketplace. Readback confirmed state schema 3,
`awaiting_framing_answers`, guided-entry methodology version 0.4, and bytewise
bundle equivalence.

## Remaining Validation

The existing combined manual user replay of `project-framing` followed by
`document-project-canvas` remains pending. A new Codex conversation is required
to exercise the freshly installed skill registry in normal interactive use.

No Golden Output, shared model, commit, or push was created or changed.
