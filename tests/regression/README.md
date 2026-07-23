# Regression Procedure

Use this procedure whenever a skill, shared contract, fixture, scenario, or
quality rule changes.

## Procedure

1. Identify affected skills and scenarios.
2. Run each scenario with unchanged source material.
3. Preserve the raw candidate output.
4. Evaluate it with the common and skill-specific checklists.
5. Compare it with the approved golden output when available.
6. List every meaningful difference.
7. Classify each difference.
8. Correct regressions and rerun affected scenarios.
9. Record unresolved issues and required decisions.
10. Complete manual validation before requesting any golden-output update.

## Difference Classes

- `IMPROVEMENT`: stronger methodology with no loss of validated information.
- `ACCEPTABLE VARIATION`: equivalent meaning and quality expressed
  differently.
- `REGRESSION`: missing, distorted, invented, inconsistent, untraceable, or
  out-of-bound content.
- `UNRESOLVED ISSUE`: a difference requiring further evidence or a human
  decision.

Stylistic differences alone are acceptable variation.

## Regression Record

For each difference, record:

| Field | Value |
| --- | --- |
| Scenario | |
| Skill | |
| Candidate run | |
| Reference | `NONE` when no golden output exists |
| Difference | |
| Classification | |
| Evidence | |
| Decision or correction | |
| Reviewer | |
| Date | |

When no approved golden output exists, evaluate the candidate against the
checklists and scenario observations, and record that reference comparison was
not available.
