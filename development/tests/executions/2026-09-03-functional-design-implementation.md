# Functional Design Implementation Review

- Date: 2026-09-03
- Skill: `functional-design` methodology version 0.1
- Scope: methodology, runtime references, tests, documentation, manifests,
  and local Codex/Claude Code installation
- Result: PASS WITH RESERVATIONS

## Delivered Contract

The former placeholder now creates, reviews, or evolves the living
`_project-design/functional-design.md` business artefact from a validated
Project Canvas and project evidence. The contract covers stable identifiers,
controlled change history, Actors and roles, global Processes, the
product-module-feature inventory, detailed feature specifications, interfaces
and fields, Business Rules, acceptance criteria, Open Questions, and one
global message catalog.

Nominal scenarios, alternative valid scenarios, errors, and exceptions remain
distinct. Functional-design owns no architecture, API, database schema,
implementation task, prioritization, estimate, backlog item, document format,
or template. Founded framing changes return to `project-framing`.

The guided state machine still routes only `project-framing`.
`functional-design` is independently callable and does not modify guided state.

## Automated Validation

| Control | Result | Evidence |
| --- | --- | --- |
| Python test suite | PASS | 61 tests passed |
| Functional-design contract tests | PASS | Structure, evolution, feature mapping, message resolution, boundaries, and runtime isolation checked |
| Official functional-design skill validator | PASS | `Skill is valid!` |
| Official validators for all nine skills | PASS | Nine of nine valid |
| Official Codex plugin validator | PASS | Plugin validation passed |
| Claude Code plugin manifest validation | PASS | Strict validation passed |
| Claude Code marketplace validation | PASS | Strict validation passed |
| JSON parsing | PASS | Codex/Claude manifests and both marketplace catalogs parse with `jq` |
| Runtime isolation | PASS | No installable bundle reference to repository development or local-work paths |
| Whitespace/error check | PASS | `git diff --check` passed |

## Installation Verification

- Codex cachebuster updated through the official helper to
  `0.1.0+codex.20260903155050`.
- Codex plugin reinstalled from local marketplace `project-design`.
- Claude Code plugin `0.1.0` was reinstalled because same-version update kept
  its previous cache.
- Both installed plugin trees compare byte-for-byte with
  `plugins/project-design/`.

## Test Corpus and Golden Outputs

The four permanent scenarios now contain functional-design-specific expected
observations. The development checklist and one flat manual test file cover
all four fixtures plus a controlled real project and an explicit update case.

No Golden Output was created or modified.

## Reservations and Next Gate

The automated contract and packaging checks pass, but the four fixture replays
and the controlled manual creation/update replay have not been executed in
this iteration. The skill therefore remains implemented with fixture and
manual replay pending. Do not describe it as fully methodologically validated
until those reviews pass.
