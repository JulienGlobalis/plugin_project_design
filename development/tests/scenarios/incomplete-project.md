# Incomplete Information Scenario

## Fixture

Use every source artefact listed in the
[incomplete-project fixture README](../fixtures/incomplete-project/README.md)
as project input. Do not provide the README itself.

## Request

```text
Use <selected-skill> to analyze and structure the supplied project material.
Produce the artefact supported by the current skill methodology and make
uncertainty visible.
```

## Applicable Skills

Run this scenario for `project-framing` and `project-design`, and for any skill
whose handling of missing information or unsupported invention changes.

## Expected Observations

- Supplied facts remain intact and attributable to the source.
- Missing information becomes explicit.
- Open questions are actionable and do not masquerade as requirements.
- Assumptions remain distinct from facts.
- Ambiguous user populations are not silently merged.
- No requirement, priority, volume, owner, or constraint is invented.
- The output stays within the selected skill's responsibility.

## Project Framing-Specific Observations

- A useful first framing is produced before requesting non-blocking details.
- Existing handling remains distinct from the proposed workspace.
- Final scope, ownership, terminology, measures, service targets, integrations,
  and governance remain provisional or unresolved.
- Ambiguous terms such as request, ticket, case, requester, and site are not
  normalized silently.
- Questions needed before framing approval are distinguished from details that
  can wait for functional or technical design.
- Recommended next steps prioritize scope authority, participant coverage,
  terminology, and critical information requirements without inventing a
  delivery plan.
