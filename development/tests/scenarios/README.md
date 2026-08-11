# Test Scenarios

Scenarios define how to exercise the permanent fixtures without encoding exact
wording or platform-specific behavior.

- [Incomplete information](incomplete-project.md)
- [Contradictory information](contradictory-project.md)
- [Current-view Canvas contract](project-canvas-current-view.md)
- [Application modernization](application-modernization.md)
- [New application](new-application.md)

## Shared Execution Rule

Replace `<selected-skill>` in the scenario request with the skill under test.
Use the platform's normal invocation syntax, but do not add the checklist or
expected observations to the request.

Record the exact invocation in the execution history. Evaluate the output with
the repository-wide checklist, the selected skill checklist, and the
scenario-specific observations.
