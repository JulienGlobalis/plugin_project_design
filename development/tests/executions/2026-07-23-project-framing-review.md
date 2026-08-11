# Project Framing Skill Review

- Date: 2026-07-23
- Reviewer: Codex
- Platform: Platform independent
- Invocation: Four independent skill executions and repository validation
- Source commit: WORKTREE, uncommitted
- Skill: `project-framing` version 0.1
- Scenarios: All four permanent fixtures
- Golden output: NONE

## Overall Status

PASS

## Objective Achieved

Implemented the first complete business skill of the plugin.
`project-framing` now transforms an existing Project View or available project
sources into a concise, traceable, uncertainty-aware framing document without
performing downstream functional, technical, backlog, or document-production
methodologies.

## Project Framing Summary

- Methodology version: 0.1
- Main workflow stages: 8
- Shared foundations consumed: Canonical Domain Model, Knowledge Model, Project
  Model, shared terminology, and quality rules
- Supported inputs: Project View, Knowledge Assertions, structured project
  information, and raw source artefacts
- Supported output languages: requested language when terminology support is
  available, with English as the internal canonical reference
- Preliminary questions: focused high-value questions, only
  when needed before drafting
- Clarification priorities: before framing approval, before the next design
  phase, or deferrable
- Golden Outputs created or modified: NONE

Main decisions:

- produce a useful first framing before requesting exhaustive clarification;
- preserve Established, Provisional, and Unresolved information;
- preserve Existing, Target, and Transition perspectives;
- keep Stakeholder and Actor, Need and Requirement, Risk and Issue, and Option
  and Decision distinct;
- select sections according to the project rather than force a fixed template;
- retain concise traceability without exposing internal model mechanics in a
  normal client document;
- keep dependencies as relationships rather than introducing a new canonical
  concept;
- keep French prose natural while retaining English canonical references
  internally.

## Architecture Compliance

| Check | Result |
| --- | --- |
| Canonical Domain Model changed | PASS: NO |
| Knowledge Model changed | PASS: NO |
| Project Model changed | PASS: NO |
| French canonical terminology changed | PASS: NO |
| New shared model or processing layer introduced | PASS: NO |
| Skill consumes the shared information architecture | PASS |
| Framing statements remain traceable to knowledge and sources | PASS |

Frozen foundation SHA-256 values before and after this iteration:

- Canonical Domain Model:
  `8ba605e6b3b437d27181e04458069a2cdda57862252cb8d36a7373aff76b84f5`
- Minimal Knowledge Model:
  `45edcc2479191d6172ccd48f2b5c8f9990fd38b2cf6762c98af702832c475aee`
- Minimal Normalized Project Model:
  `a21e78e961a294b8b2406f308128ce69f7ea93ab4bd9a4016a0f142fbf553612`
- French canonical terminology:
  `c84ce988a30f269bc5aa8919e5bc23ecf6e6ee58eb6f20cf8dc58db7e23bed16`

## Fixture Validation

Each fixture was executed independently from the skill instructions and source
artefacts. The generated drafts were reviewed against the scenario and
project-framing checklists.

| Fixture | Main validation pressure | Result |
| --- | --- | --- |
| `incomplete-project` | Missing ownership, boundaries, rules, measures, and technical facts | PASS: produced a useful incomplete framing, avoided invention, and prioritized clarification |
| `contradictory-project` | Conflicting approval, eligibility, retention, rollout, reporting, and cutover positions | PASS: preserved competing positions and did not manufacture an authorized resolution |
| `application-modernization` | Existing application, target intent, historical Decisions, and Transition concerns | PASS: kept Existing, Target, and Transition distinct and reopened historical Decisions where applicability was unknown |
| `new-application` | Proposed MVP, future Options, open Decisions, and French output | PASS: retained provisional scope, explicit exclusions, unresolved choices, and natural French terminology |

The executions also confirmed that the skill remains independently callable
without the future `project-design` orchestrator.

## Localized Terminology Compliance

| Check | Result |
| --- | --- |
| English remains the internal canonical reference | PASS |
| French companion reused without duplicating the canonical model | PASS |
| Project-specific terms preserved from sources | PASS |
| No silent language fallback introduced | PASS |
| French status labels used consistently where useful | PASS |
| Natural prose preferred over rigid literal labels | PASS |

The French execution used `Problème avéré` as a precise section label and
`problème constaté` naturally in prose without changing the canonical
meaning.

## Repository Impact

Created:

- `skills/project-framing/references/framing-structure.md`
- `development/tests/manual/README.md`
- `development/tests/manual/project-framing.md`
- `tests/executions/2026-07-23-project-framing-review.md`

Modified:

- `README.md`
- `PLAN.md`
- `SPEC.md`
- `CHANGELOG.md`
- `skills/project-framing/SKILL.md`
- `tests/README.md`
- `development/tests/TESTING.md`
- `tests/quality-checklists/project-framing.md`
- `tests/scenarios/incomplete-project.md`
- `tests/scenarios/contradictory-project.md`
- `tests/scenarios/application-modernization.md`
- `tests/scenarios/new-application.md`

Removed:

- NONE

## Validation

- Independent four-fixture skill execution: PASS
- Incomplete information handling: PASS
- Contradiction preservation: PASS
- Modernization lifecycle separation: PASS
- French-language framing: PASS
- Framing boundaries and downstream handoffs: PASS
- Manual real-project workbook: PASS, ready for use
- Golden Outputs: unchanged

## CI and Quality Checks

| Check | Result |
| --- | --- |
| Documentation updated | PASS |
| Validation against four fixtures | PASS |
| `project-framing` functional executions | PASS: 4/4 |
| Project-framing checklist | PASS |
| Manual test workbook present | PASS |
| Canonical Domain Model unchanged | PASS |
| Knowledge Model unchanged | PASS |
| Project Model unchanged | PASS |
| French canonical terminology unchanged | PASS |
| Plugin manifest validator | PASS |
| Claude strict plugin validator | PASS |
| All six skill validators | PASS |
| Repository consistency | PASS |
| Markdown validation | PASS: 90 files |
| Local Markdown links | PASS |
| Whitespace and patch validation | PASS |
| Fixture corpus unchanged | PASS |
| Golden Outputs unchanged | PASS |

## Manual Validation to Perform

Run one real, non-confidential or appropriately controlled project through
`project-framing`, then complete the
[manual test file](../manual/project-framing.md).

The manual review should focus on:

1. factual fidelity and absence of invented project information;
2. usefulness and proportionality of questions;
3. accuracy of scope, uncertainty, and lifecycle distinctions;
4. natural French terminology when French is requested;
5. practical value for preparing or conducting a framing workshop;
6. whether the default level of detail is concise enough for the audience.

Record `PASS`, `PASS WITH RESERVATIONS`, or `FAIL` with concrete examples.
This manual validation complements the permanent fixture suite and does not
create a second automated testing system.

## Assumptions

- A useful Project View or source corpus is available at invocation time.
- The interaction language is sufficient to infer the output language when
  the user does not state it explicitly.
- A source proposal remains Provisional when approval authority is absent.
- Detailed output length may scale with source complexity while remaining
  selective and non-repetitive.
- Completed client workbooks containing confidential information remain
  outside the repository.

## Open Questions

- What default document length is most useful for real client reviews?
- Which French labels require contextual alternatives after repeated field
  use?
- Will real projects require stable traceability identifiers in the delivered
  document, or are concise source references sufficient?
- Which framing questions most often prove unnecessary during live use?

## Future Evolution Recommendations

Do not modify the shared models based on this iteration. First collect
evidence through the manual real-project workbook.

Potential improvements should be limited to observed needs, especially default
document length, question prioritization, French wording, and the amount of
visible traceability in client-facing outputs.

## Recommendation

Perform the manual real-project validation before freezing
`project-framing` version 0.1 for broad reuse. The next development iteration
should then implement `functional-design`, consuming the approved framing and
shared Project View without duplicating the framing methodology.

## Git Status

Changes are local only. No commit or push was performed.

## Result

PASS
