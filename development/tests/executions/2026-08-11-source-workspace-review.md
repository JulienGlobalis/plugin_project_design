# Optional Source Workspace Review

Date: 2026-08-11

## Scope

Add an explicit source-storage decision before source intake and provide a
safe optional `_sources/` workspace without mixing raw inputs with generated
`_project-design/` deliverables.

## Contract

- `external` keeps every source at its original location.
- `centralized` requires explicit confirmation and initializes
  `_sources/documents/`, `source-index.md`, and `links.md`.
- Local files require per-file copy confirmation and are never overwritten.
- Google Drive-native sources are recorded as links and are not exported.
- The source workspace is ignored from Git by default.
- Workflow state stores only the selected mode, never source contents or URLs.
- Version 1 workflow states migrate to version 2 without discarding history.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Unit tests | PASS | 27 tests cover source initialization, consent, copying, links, symlink safety, workflow order, migration, and prior gates |
| Source/delivery separation | PASS | `_sources/` and `_project-design/` have distinct contracts |
| No-overwrite behavior | PASS | Duplicate local destinations are rejected |
| Source privacy | PASS | `/_sources/` is appended once to `.gitignore` |
| State privacy | PASS | State records mode and path only |
| Manual recipe alignment | PASS | Markdown grid and Google Sheet contain 43 criteria, including four source-workspace prompts |
| Google Sheet native controls | PASS | Readback confirms copied formatting and PASS result validation on all four rows |
| Skill validation | PASS | All nine installed skills pass the official validator |
| Plugin validation | PASS | Official plugin validator passes |
| Plugin installation | PASS | `0.1.0+codex.20260811141829` is installed and the cache contains the source workflow |
| Patch hygiene | PASS | `git diff --check` passes |

## Result

PASS WITH RESERVATIONS — implementation, automated tests, validators, Markdown
recipe, and connected Google Sheet readback pass. A user replay in a new Codex
thread remains required.
