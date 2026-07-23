# Execution History

Store one Markdown record per completed test run. Use a filename such as:

```text
YYYY-MM-DD-<skill>-<scenario>-<platform>.md
```

Do not store temporary fixture data or unapproved golden outputs here.

## Record Template

```markdown
# Test Run

- Date:
- Reviewer:
- Platform:
- Invocation:
- Source commit:
- Skill:
- Scenario:
- Fixture:
- Golden output: NONE

## Validation Results

- Repository checklist:
- Skill checklist:
- Scenario observations:
- Structural validation:

## Differences

| Difference | Classification | Evidence | Decision |
| --- | --- | --- | --- |

## Unresolved Issues

- NONE

## Result

PASS, FAIL, or BLOCKED
```

An execution record is evidence of review, not automatic approval of a golden
output.
