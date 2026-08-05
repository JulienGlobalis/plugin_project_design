# Document Project Canvas Implementation Review

Date: 2026-08-05  
Repository: `/Users/julienoger/Documents/Dev/project_design`  
Branch: `main`  
Baseline: `dfba5f1` (`Finalize document skill architecture`)  
Initial repository state: clean and aligned with `origin/main`

## Objective

Advance the planned `document-project-canvas` iteration so the user can test
`project-framing` and final Project Canvas documentary restitution in one
sequential manual replay.

The implementation must not change `project-framing`, add business knowledge,
resolve a question, alter a Decision, or implement any of the three remaining
document placeholders.

## Result

`document-project-canvas` methodology version 0.1 is implemented. It consumes
one validated Project Canvas artefact and produces a document in:

- native Markdown by default;
- Microsoft Word on explicit request;
- native Google Docs on explicit request.

The skill applies a default professional structure when no template is
supplied. A supplied template is accepted only when it can preserve every
required section, explicit gap, status, lifecycle perspective, contradiction,
Decision, question, readiness qualification, and traceability element.

The skill owns only documentary structure, presentation, format production,
template application, and document-level verification. It returns artefact
defects to `project-framing` instead of repairing them silently.

## Runtime Files Created

- `plugins/project-design/skills/document-project-canvas/references/document-structure.md`
- `plugins/project-design/skills/document-project-canvas/references/format-guidance.md`
- `plugins/project-design/skills/document-project-canvas/references/quality-checklist.md`

## Runtime File Implemented

- `plugins/project-design/skills/document-project-canvas/SKILL.md`

The directory contains no template, script, generator, runtime example, or
platform-specific integration.

## Development Files Aligned

- `README.md`
- `CHANGELOG.md`
- `development/PLAN.md`
- `development/PROJECT_CONTEXT.md`
- `development/SPEC.md`
- `development/tests/TESTING.md`
- `development/tests/manual/README.md`
- `development/tests/manual/project-framing.md`
- `development/tests/quality-checklists/document-project-canvas.md`
- all four permanent fixture scenarios
- both plugin manifests
- `plugins/project-design/README.md`
- this execution report

No fixture, Golden Output, canonical concept, Knowledge Model, Project Model,
Information Architecture decision, French canonical terminology, or business
methodology was modified.

## Combined Manual Validation

The single manual file still contains `PF-MAN-001` through `PF-MAN-005`. Its
workflow now preserves two separate outputs:

1. the Project Canvas business artefact produced by `project-framing`;
2. the final document produced from that artefact by
   `document-project-canvas`.

The bilingual grid adds documentary checks for content parity, complete
structure, readability, non-invention, and verified native format. A `Prompt`
column now provides a copy-ready prompt for every criterion, while every manual
case result table identifies the project-framing and documentary prompts to
run.

The connected Google Sheet
[`Recette`](https://docs.google.com/spreadsheets/d/1iMINOtoyTMTa5aA80ies8TjdjrIlL5mJKtU2fpDzNVE/edit)
was updated in its `project-framing` tab. The title and instructions now name
both skills, the new column D contains one prompt per criterion, and rows 27
through 31 contain the five documentary controls. The result and comment
columns moved to E and F. Readback confirmed all 28 prompt values, formatting,
and the existing `PASS` / `PASS WITH RESERVATIONS` / `FAIL` validation lists.

## Scenario Evidence

The four retained Project Canvas fixture outputs were checked as valid inputs:
each contains the ten required sections plus downstream readiness in the
requested language. Native Markdown restitution used a lossless representation
and exact comparisons reported no difference for:

- `incomplete-project`;
- `contradictory-project`;
- `application-modernization`;
- `new-application` in French.

Word and Google Docs result-level verification remains part of the combined
manual replay. The skill contract requires a real `.docx` render inspection or
native Google Docs readback before either format may be claimed for an actual
delivery.

## Marketplace and Cache

The repository marketplace already referenced `./plugins/project-design`, but
Codex still had the `project-design` marketplace configured against the old
iCloud clone. The obsolete configured source was removed with the official
CLI and the correct repository root was added.

The official cachebuster workflow updated the Codex version from
`0.1.0+codex.20260805192838` to
`0.1.0+codex.20260805204858`, then reinstalled
`project-design@project-design`.

The active installation now resolves to the correct repository and exposes
exactly nine skills. Its cached `document-project-canvas` contains the
implemented `SKILL.md` and three runtime references. The former generic skill
is absent.

## Validation Results

| Control | Result |
| --- | --- |
| Exact repository path | PASS |
| Initial Git state | PASS — clean `main`, aligned at `dfba5f1` |
| Nine official skill validations | PASS — `quick_validate.py` |
| `document-project-canvas` implemented status and frontmatter | PASS |
| Codex plugin validation | PASS — official plugin validator with PyYAML runtime |
| Claude strict plugin validation | PASS |
| Local Markdown links | PASS — 107 files, no broken target |
| Markdown code fences | PASS — balanced |
| Bundle dependency on `development/` | PASS — none |
| Protected foundations, fixtures, and Golden Outputs | PASS — unchanged |
| Four retained Canvas inputs | PASS — ten sections and readiness present |
| Native Markdown lossless restitution | PASS — four exact comparisons |
| Word and Google Docs result-level replay | PASS WITH RESERVATIONS — user replay pending |
| Manual Markdown prompt column | PASS — five case tables and 28 verification rows populated |
| Google Sheet prompt column | PASS — 28 prompts populated in column D |
| Google Sheet values and dropdown validation | PASS — connector readback |
| Google Sheet native visual inspection | PASS WITH RESERVATIONS — API-level formatting check only |
| Correct marketplace source | PASS — current repository root |
| Active cachebuster and installed skill content | PASS |
| `git diff --check` | PASS |

The first plugin-validator invocation lacked PyYAML in its isolated runtime;
rerunning the official validator with the required PyYAML dependency passed.
This was an environment invocation issue, not a plugin defect.

## Final Status

Technical implementation and structural validation are complete. Full
methodology validation remains pending until the user performs the combined
manual replay and returns both the Canvas artefact and final document results.

No commit or push was requested or performed in this iteration.
