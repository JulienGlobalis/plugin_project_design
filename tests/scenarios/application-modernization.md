# Application Modernization Scenario

## Fixture

Use every source artefact listed in the
[application-modernization fixture README](../fixtures/application-modernization/README.md)
as project input. Do not provide the README itself.

## Request

```text
Use <selected-skill> to analyze and structure the supplied project material.
Produce the artefact supported by the current skill methodology and make
uncertainty visible.
```

## Applicable Skills

Run this scenario for every specialized skill when its methodology exists. Run
it for `project-design` when orchestration or a shared contract changes.

## Expected Observations

- Existing state, observed behavior, and target intent remain distinct.
- Incomplete documentation is not treated as authoritative or exhaustive.
- Existing users, workarounds, continuity, data migration, rollback, adoption,
  and reporting risks remain visible.
- Unconfirmed behavior, including case reopening, remains unresolved.
- Proposals are not represented as approved migration decisions.
- Technical debt remains connected to source evidence.
- The output stays within the selected skill's responsibility.
