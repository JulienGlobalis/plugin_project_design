# Project Manager Support Review

Date: 2026-09-05. Baseline: `921f4ba` (`Implement functional design methodology`).
Initial working tree: clean. Reviewer: Codex, with one independent bounded
forward-testing agent authorized by the Skill Creator validation instructions.

## Scope and Outcome

Evaluated the implemented workflow, framing, functional design, delivery gates,
runtime references, and user guidance against the request for a more directive,
interactive project-manager assistant. The
[user-facing assessment](../../documentation/PLUGIN_PM_EVALUATION.fr.md)
separates implemented corrections from proposed product improvements.

Corrections add grounded decision support, reuse explicit intake choices,
distinguish active/deferred questions, prepare reviewable approval, and provide
an actionable handoff. A contradictory readiness reference and stale Canvas
specification were aligned. Invalid Word packages now fail before state mutation.
Guided-entry/framing/functional methodology revisions are 0.5/0.6/0.2; state
schema 3, release versions, and installed copies remain unchanged.

## CI Results

| Check | Result | Evidence and limits |
| --- | --- | --- |
| Python tests | PASS | `rtk proxy python3 -m unittest discover -s development/tests/tools -q`: 62 tests, 13.942 seconds, OK |
| Word failure-state preservation | PASS | Empty file, renamed text, unrelated ZIP, malformed XML, missing body, wrong content type rejected; persisted state bytes unchanged; transitional and strict Word namespaces accepted |
| Skill Creator validation | PASS | All nine skill directories pass the official `quick_validate.py` |
| Codex bundle validation | PASS | Official `validate_plugin.py plugins/project-design` passes |
| Claude manifest validation | PASS | `rtk proxy claude plugin validate plugins/project-design` passes; this is not a Claude behavioral replay |
| Runtime local links and packaging | PASS | 96 local Markdown links resolve; none escape the installable bundle |
| Corpus preservation | PASS | Exactly four fixture directories; no fixture or Golden Output changed |
| User guide and current specification | PASS | Updated interaction, deferrals, review handoff, Word gate, and current-position Canvas rules |
| Git whitespace check | PASS | `rtk git diff --check` |
| First-interaction fixture replay | PASS WITH RESERVATIONS | Four real isolated workflows reach pending-answer state; methodological reservations below |
| Human acceptance, answer/defer conversation replay, interactive widgets | NOT RUN | Updated manual cases provided; no user responses or widget behavior fabricated |
| Functional-design creation/update behavior | NOT RUN | Interaction contract updated; full validated-baseline fixture/manual replay remains pending |
| Native Word visual QA and Google Docs delivery | NOT APPLICABLE to this change | No external document requested/generated; package tests do not prove visual or semantic quality |
| Installation, publication, commit, push | NOT APPLICABLE | Not requested; source bundle evaluated directly |

The first post-change Python run failed one static assertion hardcoded to
functional methodology 0.1. It now checks implemented status with a numeric
methodology revision rather than rejecting every future version; the subsequent
full suite passed. No behavioral test failure was hidden by that change.

The default Python lacked PyYAML, preventing the official validators from
starting. A temporary environment at
`/private/tmp/project-design-validation-20260905` installed PyYAML 6.0.3 after
the sandbox DNS failure. Both official validators then ran successfully using
that environment; no repository or global Python dependency was changed.

## Independent First-Interaction Evidence

Raw outputs, source manifests and hashes, workflow command logs, saved Canvas
files, and final statuses are under:

```text
/private/tmp/project-design-forward-w19xwmm5/
```

The executing agent read all source artefacts before generation, saved raw
outputs before reading expected observations, and stopped at pending answers.
The request explicitly supplied workspace consent, framing selection,
Markdown-only delivery, and external sources. No answer, deferral, Canvas
approval, or source mutation was simulated.

| Fixture | Source files | Initially counted question bullets | Actual phase |
| --- | --- | --- | --- |
| incomplete-project | 5 | 10 | `awaiting_framing_answers` |
| contradictory-project | 6 | 8 | `awaiting_framing_answers` |
| application-modernization | 9 | 10 | `awaiting_framing_answers` |
| new-application | 9 | 11 | `awaiting_framing_answers` |

All four outputs contain ten numbered sections and the unnumbered three-stage
readiness block. Question wording in conversation matches the Canvas; counters
match the initial bullets. Source hashes and preserved raw outputs are unchanged.
The states contain zero answers/deferrals, no approval, and no question text.
Recommendations remain outside the Canvas and supplied setup choices are reused.

## Findings and Regression Classification

- **IMPROVEMENT:** a source-grounded recommendation, or an explicit reason why
  an option cannot be recommended, accompanies material decisions.
- **IMPROVEMENT:** initial setup choices are reused and readiness is saved in
  the artefact before user review.
- **REGRESSION RISK IDENTIFIED:** several initial question bullets bundled
  independently answerable decisions. For example, new-application combined
  load, maintenance windows and recovery point in one bullet, and hosting,
  technologies, support hours and service ownership in another. Matching
  counters to bullets therefore did not prove reliable partial-answer handling.
  The interaction contract and checklist now require one independent decision
  per counted question. Initial raw outputs are preserved as evidence.
- **UNRESOLVED ISSUE:** the first new-application Canvas underrepresents supplied
  structural service rules such as capacity and controlled approval. The
  existing source-coverage obligation remains; the current first-interaction
  replay is not full methodological approval. Recheck source coverage in the
  corrective framing recipe before release.

No approved Golden Output exists for comparison and none was created or changed.
The test agent's own evaluation is independent of implementation but is not
human acceptance. Technical state transitions do not prove answer semantics,
completeness of source coverage, cross-conversation recovery, or UX quality.

## Manual Handoff

Use the existing `PF-MAN-001` through `PF-MAN-005` and `FD-MAN-001` through
`FD-MAN-005`, with their added interaction criteria and the
[supplemental scenario](../scenarios/project-manager-interaction.md).
For a formatted ChatGPT report, provide case ID, project context, raw
conversation, preserved artefact, actual test results, and reservations.
Do not invent results, approve an artefact, or change unresolved business
decisions as part of formatting.

Before calling the methodology fully validated, complete answer/explicit-deferral
resumption, approved functional changes with stable IDs, review-only immutability,
and the outstanding framing/document corrective recipe. Installation in a new
thread is a separate delivery step; the currently installed plugin is unchanged.
