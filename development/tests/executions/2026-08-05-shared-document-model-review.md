# Shared Document Model Architecture Review

Date: 2026-08-05

Repository: `/Users/julienoger/Documents/Dev/project_design`

Branch: `main`

Baseline: `dfba5f1` (`Finalize document skill architecture`)

Initial repository state: existing uncommitted `document-project-canvas`
implementation series preserved

## Objective

Create one discipline-neutral documentary foundation before additional
document skills are implemented. The foundation prevents each future
`document-<discipline>` skill from defining a competing artefact-to-document
model.

This is an architecture-only intervention. It must not change a business
methodology, business artefact, fixture, Golden Output, or implemented
document methodology.

## Result

Shared Document Model version 0.1 is defined at:

- `plugins/project-design/shared/document-model/README.md`

It formalizes:

- a business artefact as a structured, versionable, format- and
  layout-independent result owned by its business skill;
- a document as a human-facing representation used for reading,
  distribution, validation, and sharing, never as the business source of
  truth;
- the one-way flow from business artefact through a document skill to a
  document;
- the prohibition on creating knowledge, resolving contradictions, making
  Decisions, or repairing business content during restitution;
- formats as delivery supports that cannot change meaning;
- templates as presentation constraints that cannot change business
  structure, Decisions, contradictions, statuses, or traceability;
- content-preservation mapping and traceability across format changes;
- the minimum contract and dependency direction for all current and future
  document skills.

The foundation is independent of every discipline and document skill. It may
reference other shared contracts, while document skills depend on it in one
direction only.

## Files Created

- `plugins/project-design/shared/document-model/README.md`
- `development/tests/executions/2026-08-05-shared-document-model-review.md`

## Files Modified

- `README.md`
- `CHANGELOG.md`
- `development/PLAN.md`
- `development/PROJECT_CONTEXT.md`
- `development/SPEC.md`
- `plugins/project-design/README.md`
- `plugins/project-design/.codex-plugin/plugin.json` — cachebuster only for
  local reinstall
- `plugins/project-design/skills/document-project-canvas/SKILL.md`
- `plugins/project-design/skills/document-functional-design/SKILL.md`
- `plugins/project-design/skills/document-technical-design/SKILL.md`
- `plugins/project-design/skills/document-product-backlog/SKILL.md`

The four skill changes add only a shared-reference link. No workflow,
boundary, format behavior, input, output, or methodology text was changed.

## References Added

The root and bundle README files, plan, specification, and continuity context
now identify the Shared Document Model as a stable bundle-owned foundation.

All four `document-<discipline>` skills reference the common contract. The
three future document skills remain non-operational placeholders.

## Marketplace and Cache

The official local-plugin update flow replaced the Codex cachebuster with
`0.1.0+codex.20260805211133` and reinstalled
`project-design@project-design` from the repository marketplace.

Readback confirmed that the active cache contains the Shared Document Model,
all nine skills, and the common reference in all four document skills. A new
Codex task is required to load the refreshed plugin registry.

## Architecture Checks

The accepted dependency direction is:

```text
Shared Document Model
        ^
        |
Document skills
```

The shared model contains no Markdown dependency on a business skill or
document skill. Its discipline names are illustrative artefact examples, not
runtime or architectural dependencies.

`document-project-canvas` already conformed to the new common contract:

- it consumes a validated Project Canvas;
- it produces only a document;
- it preserves business meaning and traceability;
- it returns business-content defects to `project-framing`;
- it claims only supported, natively verified formats;
- it does not own Canvas knowledge.

No methodological correction was required.

## Validation Results

| Control | Result |
| --- | --- |
| Exact repository path and initial Git inspection | PASS |
| Shared model scope and discipline independence | PASS |
| One-way documentary dependency and absence of circular links | PASS |
| `document-project-canvas` conformity | PASS |
| Four document-skill references | PASS |
| Nine official skill validations | PASS |
| Codex official plugin validation | PASS |
| Claude strict plugin validation | PASS |
| Official cachebuster update and local reinstall | PASS |
| Active cache readback | PASS — shared model and four references present |
| Local Markdown links across 110 files | PASS |
| Markdown code-fence balance | PASS |
| Bundle dependency on `development/` | PASS — none |
| `project-framing` business methodology | PASS — unchanged |
| Business artefacts, fixtures, and Golden Outputs | PASS — unchanged |
| `git diff --check` | PASS |
| Manual document-generation replay | NOT APPLICABLE — architecture-only iteration |

## Reservations

No architectural reservation was identified. The three future document
skills still require their own detailed methodologies and format contracts
before they can generate documents. This expected placeholder state is not a
failure of the shared model.

The combined manual validation of `project-framing` and
`document-project-canvas` remains pending from the preceding iteration and is
outside this architecture-only intervention.

## Explicit Confirmations

- No business methodology was modified.
- No business artefact was modified.
- No fixture or Golden Output was modified.
- The implemented `document-project-canvas` methodology was not modified; its
  `SKILL.md` received only the common-reference link.
- This intervention adds only a shared architectural foundation for current
  and future document skills.
- No commit was created.
- No push was performed.
