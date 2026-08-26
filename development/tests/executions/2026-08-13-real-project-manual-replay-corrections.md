# Real-Project Manual Replay Corrections — 2026-08-13

## Scope

Reviewed the completed `project-framing` and `document-project-canvas` manual
test results recorded in the native Google Sheet `Recette`, tab
`project-framing`:

`https://docs.google.com/spreadsheets/d/1iMINOtoyTMTa5aA80ies8TjdjrIlL5mJKtU2fpDzNVE/edit?gid=0#gid=0`

The replay used a real AI-managed project and covered the stateful guided
workflow, Project Canvas methodology, source workspace, and native Word
restitution.

## Observed Results

The 43 recorded controls contain:

- 29 `PASS`;
- 5 `PASS WITH RESERVATIONS`;
- 9 `FAIL`.

The result and comment columns are retained as historical execution evidence.
This correction updates only the test definition columns where the expected
behavior had drifted or where a corrective re-test is required.

## Classification

### Obsolete Test Expectations

Five `FAIL` results describe behavior that is intentionally excluded by the
current Project Canvas contract rather than runtime defects:

- question batches limited to three items;
- iterative framing limited to three questions per round;
- proposed Options and unresolved Scope displayed as current Scope categories;
- normalization statuses displayed in the standard Canvas;
- contradiction narratives displayed in the standard Canvas.

The Google Sheet now tests the decisions already implemented: complete
necessary question batches without a numeric cap, current validated Scope
only, internal statuses, and concise Decision questions instead of conflict
narratives.

### Confirmed Methodology Gaps

Four `FAIL` results identified genuine defects:

- no explicit functional-design readiness conclusion;
- no explicit technical-design readiness conclusion;
- no explicit backlog-preparation readiness conclusion;
- derived subtitle and traceability summary added to the Word document even
  though those statements were absent from the Canvas.

## Corrections

### `project-framing` 0.5

- Keep exactly ten numbered Canvas sections.
- Require one unnumbered downstream-readiness block after those sections.
- Qualify functional design, technical design, and backlog preparation
  separately as `Ready`, `Ready with reservations`, or `Not ready`, or natural
  equivalents in the requested language.
- Justify every conclusion from current validated content and distinguish
  blockers from non-blocking reservations.
- Extend the installed fictional example and runtime checklist to exercise the
  three distinct conclusions.

### `document-project-canvas` 0.2

- Require a forward preservation map and a reverse content map.
- Apart from neutral structural labels, require every sentence to map to the
  Canvas or explicit user-supplied document metadata.
- Forbid derived subtitles, summaries, question counts, traceability
  statements, approval statements, and other narrative adornment.
- Keep a separately supplied audit or traceability artefact outside the Canvas
  document unless the user explicitly requests a combined document.

### Manual Recipe

The native Google Sheet and repository manual grid now use the same contracts.
The Google Sheet update preserves:

- all 43 historical result values;
- every user comment and reservation;
- the `PASS`, `PASS WITH RESERVATIONS`, and `FAIL` validation lists;
- existing formatting and frozen rows.

## Deferred Decisions

The following feedback is useful but requires separate architectural scope and
is not silently implemented by this correction:

- automatic versioning or replacement policy for canonical artefact paths;
- a mandatory Canvas adjustment changelog;
- native document validation inside the workflow state machine rather than in
  the specialized document skill.

## Re-Test Requirement

The first real-project replay is accepted as correction evidence, not as a
full methodology PASS. Re-run at least the following controls with the updated
installed bundle:

- complete question batch without numeric cap and exact resumption;
- the three separate readiness conclusions;
- blocking versus non-blocking classification;
- Canvas-to-document forward preservation;
- document-to-Canvas reverse mapping with no derived subtitle, summary, or
  audit content.

Do not overwrite the historical results when recording the corrective replay;
record a new execution result or clearly dated re-test evidence.
