# Testing Strategy

This document is the testing reference for every `project-design` change.

## Purpose

Tests verify methodological quality, not identical wording. They evaluate:

- structure and completeness;
- internal consistency and source fidelity;
- traceability of facts, interpretations, assumptions, proposals, decisions,
  and open questions;
- quality of reasoning and handling of uncertainty;
- compliance with skill responsibilities and boundaries;
- absence of unsupported invention;
- clarity of the pre-execution skill, input, output, and template brief;
- correct placement of durable Markdown outputs under `_project-design/`;
- explicit consent before workspace initialization and idempotent creation;
- default stage selection and focused iterative framing dialogue;
- persisted phase transitions that reject skipped or invalid steps;
- absence of business or source content from the workflow state;
- Canvas and external-document completion gates.

A skill change is incomplete until its affected tests and documentation have
also been updated.

## Mandatory Workflow

```text
Modify a skill
        |
Update the corresponding tests
        |
Run the relevant scenarios
        |
Evaluate with repository and skill checklists
        |
Compare with approved reference outputs
        |
Explain every meaningful difference
        |
Correct if necessary
        |
Validate manually
        |
Only then update reference outputs
```

For every future iteration:

1. Read `README.md`, `development/PLAN.md`, `development/SPEC.md`,
   `CHANGELOG.md`, `CONTRIBUTING.md`, and
   `development/PROJECT_CONTEXT.md`.
2. Read this document.
3. Identify the impacted skills, shared contracts, scenarios, and checklists.
4. Update the affected tests in the same change.
5. Run the relevant scenarios on each supported platform when portability is
   affected.
6. Evaluate outputs with the repository-wide and skill-specific checklists.
7. Compare outputs with approved golden outputs when they exist.
8. Classify and explain every meaningful difference.
9. Verify that `plugins/project-design/` has no dependency on
   `development/`.
10. Record the test run and update repository documentation.
11. Never modify a golden output without explicit human approval.

## Test Architecture

| Area | Role |
| --- | --- |
| `fixtures/` | Stable, anonymized project source material |
| `scenarios/` | Reusable execution instructions and expected observations |
| `quality-checklists/` | Common and skill-specific evaluation criteria |
| `golden-outputs/` | Explicitly approved reference artefacts |
| `regression/` | Difference classification and regression procedure |
| `executions/` | Test-run evidence and validation decisions |
| `manual/` | One lightweight manual test file per implemented skill |

Test data, execution instructions, evaluation criteria, and approved outputs
must remain separate. This prevents expected conclusions from leaking into a
scenario input.

## Fixture Strategy

The permanent regression corpus contains exactly four fixtures:

- `incomplete-project`;
- `contradictory-project`;
- `application-modernization`;
- `new-application`.

Each fixture contains a `README.md` describing its purpose, anonymization, and
source-artefact inventory. Project information is distributed across the
heterogeneous artefacts listed there. Directory structures may differ when
the consulting context justifies it. Every fixture is fictional and fully
anonymized.

Do not add another permanent fixture. A one-off case may be created in a
temporary test-run location, must not be committed under
`development/tests/fixtures/`, and must be deleted after its evidence has
been recorded.

Do not use real customers, companies, projects, people, email addresses, URLs,
confidential rules, internal identifiers, or commercial information in test
material.

## Scenario Execution

Choose scenarios by changed behavior, not by file count. Run at least:

- the scenario directly exercising the changed behavior;
- any scenario covering uncertainty, contradiction, or boundaries affected by
  the change;
- all four scenarios when a shared model, shared quality rule, orchestration
  rule, or cross-skill contract changes.

For each run:

1. Use every source artefact listed by the scenario's fixture README as
   project input, excluding the README itself.
2. Invoke the selected skill without supplying the evaluation checklist or
   expected observations.
3. Preserve the raw output before review.
4. Evaluate it with `repository-quality.md` and the selected skill checklist.
   Confirm that the invocation brief appears before substantive work and that
   any durable Markdown file uses the target project's `_project-design/`
   workspace.
5. Compare it with the matching approved golden output, if one exists.
6. Record platform, skill version or commit, scenario, reviewer, result,
   differences, and unresolved issues under `executions/`.

Temporary raw outputs may be kept outside the permanent corpus during a test
run. They become golden outputs only through the approval process below.

## Quality Checklists

Every run uses:

- [the repository-wide checklist](quality-checklists/repository-quality.md);
- [the checklist for the invoked skill](quality-checklists/README.md);
- any scenario-specific expected observations.

Record each criterion as `PASS`, `FAIL`, or `NOT APPLICABLE`, with concise
evidence. A criterion marked `TO BE DEFINED` is not silently treated as
passing; record it as an unresolved methodology item.

Checklists evolve with the methodology. Changes to a skill's responsibility,
inputs, outputs, boundaries, or quality contract require a corresponding
checklist update.

## Golden Outputs

A golden output is a manually reviewed and explicitly approved reference
artefact. It is a comparison aid, not an exact text snapshot.

Compare:

- structure;
- information captured or deliberately left unresolved;
- reasoning quality;
- traceability;
- methodological completeness;
- compliance with skill boundaries.

Do not fail a run for stylistic variation alone. Do not create or replace a
golden output merely because a new run looks better. Approval must identify
the reviewer, date, scenario, skill, platform-neutral expectations, and reason
for accepting the reference.

No Golden Output has yet received explicit human approval. The
`project-framing` methodology is implemented, but its outputs remain
unapproved references until the review and approval process above is
completed.

## Regression Testing

For every meaningful difference from an approved reference, classify it as:

- `IMPROVEMENT`: better methodological quality without loss of required
  information;
- `ACCEPTABLE VARIATION`: different expression with equivalent quality and
  meaning;
- `REGRESSION`: loss, distortion, unsupported invention, boundary violation,
  or reduced traceability;
- `UNRESOLVED ISSUE`: impact cannot yet be determined or needs a decision.

Correct regressions before completion. Document unresolved issues and obtain a
decision before treating the change as validated. See
[the regression procedure](regression/README.md).

## Portability Testing

Codex and Claude Code must use identical fixtures, scenarios, expected
observations, and quality criteria. Only invocation syntax and platform
metadata may differ.

When a change can affect platform behavior:

1. Run the same scenario with the same selected skill on both platforms.
2. Evaluate both outputs independently with the same checklists.
3. Compare methodological results, not formatting or invocation syntax.
4. Record platform-specific differences and classify them.

A platform adapter must not alter the shared methodology or create a separate
fixture corpus.

## Release Validation

Before a release:

- run all four permanent scenarios against every skill changed since the last
  release;
- run all four scenarios against `project-design` when orchestration or shared
  contracts changed;
- complete repository-wide and affected skill checklists;
- resolve every regression and disposition every unresolved issue;
- verify fixture anonymization and the four-fixture limit;
- validate Codex and Claude Code manifests;
- validate every modified skill;
- confirm that core behavior remains independent from Spec Kit;
- confirm that golden-output changes have explicit human approval;
- record the release validation under `executions/`.

## Future Automation

Automation may later help enumerate fixtures, check links and manifests,
collect raw outputs, or verify that execution records are complete. It must
not:

- compare prose byte-for-byte;
- assign methodological approval without human review;
- update golden outputs automatically;
- create permanent fixtures from live customer data;
- couple shared tests to Codex, Claude Code, Spec Kit, or another runtime.

Add automation only after the corresponding methodology and contracts are
stable. Until then, manual evidence and review are authoritative.

## Manual User Validation

Use a manual test file after repository fixture validation when a skill needs
an independent user replay, practical review on controlled project material,
or both. Keep it directly usable and complete it during or immediately after
the test.

Manual test files:

- do not replace permanent scenarios or quality checklists;
- do not become Golden Outputs automatically;
- must not contain committed confidential client information;
- record practical usefulness, friction, terminology, and improvement needs;
- may support a later skill change only when feedback is traceable and
  reviewed.

The current
[Project Framing and Project Canvas Document](manual/project-framing.md) file
contains four fixture replay cases and one controlled real-project case for
validating `project-framing` followed by `document-project-canvas`. Preserve
and evaluate the business artefact and final document separately. Results
remain pending until the user completes and returns them.
