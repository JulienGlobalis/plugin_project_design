# Stateful Guided Workflow Review

Date: 2026-08-11

## Scope

Replace instruction-only sequencing with a persistent, deterministic state
machine for the implemented `project-design -> project-framing ->
document-project-canvas` chain. Keep business and document methodologies in
their specialized skills.

## State Contract

`_project-design/project-design-state.json` stores only:

- consent and timestamps;
- current phase and next-action context;
- selected stage, output format, template mode and reference;
- input-presence flags;
- framing iteration counts;
- Canvas approval and delivery references;
- transition history.

It stores no description, source content, question or answer text, Canvas
statement, Decision, or other project knowledge.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Unit tests | PASS | 16 tests cover initialization and all implemented gates |
| Ordered transitions | PASS | Commands reject unexpected current phases |
| Resume behavior | PASS | Existing state is returned without reset |
| Input and template gates | PASS | Missing inputs and invalid local or Drive templates are rejected |
| Legacy iteration guard | PASS | The then-current bounded-round rule was enforced; it is superseded by the pending-answer workflow |
| Canvas gate | PASS | Explicit approval and non-empty Markdown required |
| Document gate | PASS | Verified Word path or native Google Docs URL required |
| Skill validation | PASS | All nine skills pass official validation |
| Plugin validation | PASS | Official plugin validator passes |
| Patch hygiene | PASS | `git diff --check` passes |

## Manual Test Alignment

The Markdown grid and Google Sheet `Recette`, tab `project-framing`, contain 39
criteria. Five new rows test persistence, phase enforcement, state privacy,
iteration limits, and completion gates. Connector readback confirms the native
result dropdowns and preservation of existing rows and results.

## Result

PASS WITH RESERVATIONS — technical and connector validation pass. A user replay
in a new Codex thread remains required to evaluate model adherence to each
returned `next_action` and native spreadsheet appearance.
