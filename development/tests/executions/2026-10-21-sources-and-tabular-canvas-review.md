# Default Source Workspace and Tabular Canvas Review

Date: 2026-10-21

## Scope

- `_sources/` created at the consented start; source-strategy phase removed;
  external opt-out kept; workflow schema 4 with migration from schema 3.
- `index-documents` command for files dropped into `_sources/documents/`.
- Project Canvas mandatory tables, feature formulation rules, exhaustive
  source extraction, technical-foundation intake question, and candidate
  questions during a pending batch.
- No plugin, methodology, CHANGELOG, or tag version change (user request).

## Automated Checks

| Check | Result |
| --- | --- |
| `python3 -m unittest discover -s development/tests/tools` (75 tests) | PASS |
| Skill Creator `quick_validate.py` on the nine skills | PASS |
| `claude plugin validate plugins/project-design` | PASS |
| Local Markdown links inside the bundle | PASS (0 broken) |
| Codex plugin validator | NOT RUN |

New or changed tests cover: `_sources/` creation at start and by
`init_workspace.py`, validation before any creation, v3 to v4 migration
(strategy phase, realigned external state, preserved external state without
`_sources/`), delivery leading directly to source collection, optional
opt-out, deposited-file indexing, the four example tables, infinitive verbs,
services after the MVP table, stable question numbers with `À apporter`, and
the framing boundary.

## Fictional Replay of project-framing

A temporary fictional project (equipment-lending association, brief plus a
legacy user manual defining the scope) was driven through the real workflow
up to `framing_iteration_preparation`. An independent agent then applied the
repository bundle of `project-framing`. Raw outputs stayed in the session
scratchpad and are not committed.

| Expected | Observed | Result |
| --- | --- | --- |
| `_sources/` created at start, Git-ignored, documents indexed with SHA-256 | Yes; originals unchanged (hashes match the index) | PASS |
| Delivery choice leads to `awaiting_sources` | Yes | PASS |
| Four tables with the mandatory columns | MVP, Hors MVP, Risques, Décisions, Questions present with exact columns | PASS |
| Features start with an infinitive verb, no profile duplication | Yes; bénévole and administrateur Matériel menus merged into one row | PASS |
| Every capability of the scope-defining manual covered | All five menus covered in MVP | PASS |
| `[Nouveau]` on target-only capability | Reminder email tagged | PASS |
| Services as bullets after the MVP table | Yes | PASS |
| Unanswered questions show `À apporter`, stable numbering, referenced by readiness | Six questions numbered 1-6, cited by number | PASS |
| No source identifier, status label, or contradiction narrative | None | PASS |
| Source coverage list in the delivery message | Present, per source with method | PASS |
| Technical-foundation answer classified | Technical Constraints and Hors MVP | PASS |
| `present-questions` recorded | 6 pending, `awaiting_framing_answers` | PASS |

## Reservations from the Replay

Corrected in this iteration:

- a cited future evolution goes to Outside MVP as a row, its preparation
  obligation to Technical Constraints;
- module names fall back to neutral business domains when the target
  modules are undefined;
- no proposal disclosure is needed when every Risk solution comes from the
  sources.

Open, not corrected:

- the success-criteria and objectives questions sit between the "only
  downstream-conditioning questions" rule and the Section 10 instruction to
  add necessary questions;
- the answered-question row deliberately duplicates the result incorporated
  in other sections;
- Risk solutions taken from outside the sources are disclosed only in the
  delivery message, not in the Canvas cell itself.

## Not Covered

The replay covered only the first exchange: no answer recording, deferral,
candidate-question case, scanned PDF/OCR case, or parallel sub-agent split.
The four permanent fixtures and the Google Sheet `Recette` were not
replayed or updated.

## User Guide

`development/documentation/USER_GUIDE.md` updated: start step, source
deposit, source reading and coverage, technical-foundation question, Canvas
tables, question table, candidate questions, and file tree.
