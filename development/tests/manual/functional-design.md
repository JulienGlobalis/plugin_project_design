# Functional Design Manual Tests

Use this file to review `functional-design` creation and controlled evolution.
Do not commit confidential project material, generated client artefacts, or
completed client test records.

Allowed results: `PASS`, `PASS WITH RESERVATIONS`, or `FAIL`.

## Common Procedure

1. Prepare a validated Project Canvas from the selected fixture or controlled
   project; do not give the functional-design checklist to the model.
2. Invoke `functional-design` directly and verify its launch brief, inputs,
   boundaries, and workspace consent behavior.
3. Generate `_project-design/functional-design.md` and evaluate it with the
   repository and functional-design checklists.
4. Verify actors and roles, global Processes, the feature inventory, every
   detailed feature subsection, global rules, and the annex message catalog.
5. Confirm stable cross-references and separate readiness conclusions for
   technical design and backlog preparation.
6. Supply one traceable correction or approved Decision, request an update,
   and verify that unaffected meaning and stable IDs remain unchanged while
   the change history records the affected IDs and reason.
7. Record concrete evidence and reservations outside committed client data.

## FD-MAN-001 — Incomplete Project

Use every source listed by the incomplete-project fixture plus its validated
Canvas. Verify that missing roles, rules, fields, and acceptance conditions
remain explicit, no permissions are invented, and readiness stays qualified.

## FD-MAN-002 — Contradictory Project

Use every source listed by the contradictory-project fixture plus its
validated Canvas. Verify that disputed access, approval, response, retention,
reporting, rollout, and cutover behavior remains unresolved and does not leak
into nominal scenarios or acceptance criteria.

## FD-MAN-003 — Application Modernization

Use every source listed by the application-modernization fixture plus its
validated Canvas. Verify separation of Existing, Target, and Transition
behavior, then revise one feature and confirm stable-ID preservation.

## FD-MAN-004 — New Application in French

Use every source listed by the new-application fixture plus its validated
Canvas. Request French output and verify the full structure, natural
terminology, message catalog references, and absence of future-scope leakage.

## FD-MAN-005 — Controlled Real Project

Use a non-confidential or sanitized real project with an approved Canvas.
Confirm that the artefact is useful for stakeholder review and that its
separate technical-design and backlog-readiness conclusions match the known
project position. Return the generated artefact and review record to the
project owner without committing them here.

| Case | Platform | Initial result | Update result | Reservations or evidence |
| --- | --- | --- | --- | --- |
| FD-MAN-001 |  |  |  |  |
| FD-MAN-002 |  |  |  |  |
| FD-MAN-003 |  |  |  |  |
| FD-MAN-004 |  |  |  |  |
| FD-MAN-005 |  |  |  |  |
