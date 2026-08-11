# Skill Invocation and Project Workspace Review

- Date: 2026-08-10
- Scope: all nine `project-design` skills
- Result: PASS WITH RESERVATIONS

## User Feedback

Manual testing identified two cross-skill needs:

1. present the selected skill, expected inputs, generated deliverables, and
   user-supplied models or templates before substantive work;
2. group every durable Markdown output under `_project-design/` at the target
   project root.

## Implemented Contract

The shared quality rules now define a concise invocation brief and these
default Markdown paths:

```text
_project-design/
├── project-canvas.md
├── functional-design.md
├── technical-design.md
├── product-backlog.md
└── documents/
    ├── project-canvas.md
    ├── functional-design.md
    ├── technical-design.md
    └── product-backlog.md
```

The nine skills reference this contract. Implemented skills identify their
current inputs, outputs, template rule, and delivery path. Placeholder skills
state that their methodology is unavailable and generate no file.

## Test Alignment

- The repository-wide and implemented-skill checklists cover the invocation
  brief, output placement, unavailable paths, and silent-overwrite protection.
- The manual Markdown grid contains 30 criteria and a prompt for each one.
- The Google Sheet `Recette`, tab `project-framing`, contains the same two new
  criteria at rows 4 and 5. Existing rows and entered results were shifted
  without loss; result dropdown validation remains active.

## Validation Results

| Control | Result |
| --- | --- |
| Nine skill validations | PASS |
| Codex plugin validation | PASS |
| Manual grid shape and prompt completeness | PASS — 30 rows |
| Google Sheet values and result validation | PASS — connector readback |
| Google Sheet native visual inspection | PASS WITH RESERVATIONS — API-level formatting inspection only |
| Bundle dependency on `development/` | PASS — none found |
| `git diff --check` | PASS |
| Updated marketplace installation | PASS — `0.1.0+codex.20260810124338` |

The native visual Google Sheet check remains reserved because the connected
browser profile could not open this file during the previous visual attempt.
Cell values, wrapping, borders, and validation were checked through the native
Sheets connector.
