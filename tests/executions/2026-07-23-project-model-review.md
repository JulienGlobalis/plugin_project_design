# Minimal Normalized Project Model Review

- Date: 2026-07-23
- Reviewer: Codex
- Platform: Platform independent
- Invocation: Conceptual model review
- Source commit: WORKTREE, uncommitted
- Skills: All future skills
- Scenarios: All four permanent fixtures
- Golden output: NONE

## Overall Status

PASS

## Objective Achieved

Defined version 0.1 of the
[Minimal Normalized Project Model](../../shared/project-model/README.md) as the
coherent project representation consumed by future skills.

The model consolidates Knowledge Assertions into normalized canonical
elements and relationships while preserving established, provisional, and
unresolved states and complete traceability to the Knowledge Model.

## Project Model Summary

- Conceptual constructions: 6
- Constructions: Project View, Project Element, Project Relationship,
  Normalization Status, Lifecycle Perspective, Knowledge Basis
- Normalization statuses: Established, Provisional, Unresolved
- Lifecycle perspectives: Existing, Target, Transition
- Knowledge Basis roles: Supporting, Qualifying, Opposing
- Canonical concepts reused: 22
- Schemas or serialization introduced: NONE
- Skill methodology introduced: NONE

Main decisions:

- normalize canonical project instances rather than copying assertions;
- use one shared Project View for all future skills;
- distinguish normalization status from Knowledge validation;
- preserve unresolved information without forcing a winner;
- distinguish current-view currency from Existing, Target, and Transition
  perspectives;
- keep completeness relative to a declared consumption purpose.

## Architecture Compliance

| Check | Result |
| --- | --- |
| Canonical Domain Model file changed | PASS: NO |
| Canonical concepts added | PASS: NONE |
| Canonical concepts removed | PASS: NONE |
| Canonical concepts modified | PASS: NONE |
| Knowledge Model file changed | PASS: NO |
| Knowledge Model constructions modified | PASS: NONE |
| Knowledge Model responsibilities modified | PASS: NONE |

Frozen foundation SHA-256 values before and after this iteration:

- Canonical Domain Model:
  `8ba605e6b3b437d27181e04458069a2cdda57862252cb8d36a7373aff76b84f5`
- Minimal Knowledge Model:
  `45edcc2479191d6172ccd48f2b5c8f9990fd38b2cf6762c98af702832c475aee`

Project Model constructions implement responsibilities already assigned to
this layer by the Information Architecture ADR. They do not extend either
frozen foundation.

## Fixture Validation

| Fixture | Normalization pressure | Result |
| --- | --- | --- |
| `incomplete-project` | Useful context alongside missing ownership, scope, rules, requirements, integrations, measures, and terminology | PASS: known elements coexist with provisional and unresolved information without invention |
| `contradictory-project` | Competing retention, approval, eligibility, response, reporting, rollout, cutover, and priority positions | PASS: unresolved elements summarize alternatives and retain supporting and opposing knowledge |
| `application-modernization` | Existing application state, target intent, technical debt, historical decisions, and unresolved transition | PASS: Existing, Target, and Transition perspectives remain separate and traceable |
| `new-application` | Objectives, requirements, proposed MVP, future options, and open decisions | PASS: target elements, provisional Scope, Options, and unresolved information retain distinct status |

A purpose-complete project is structurally representable using the same
Project View, elements, relationships, statuses, perspectives, and Knowledge
Basis. No permanent fixture claims to be fully complete, so completeness is
validated structurally rather than presented as a fixture fact.

## Future Skill Consumption

| Skill | Consistent Project Model input | Result |
| --- | --- | --- |
| `project-framing` | Foundation, governance, scope, uncertainty, and transition elements | PASS |
| `functional-design` | Actors, needs, capabilities, processes, rules, and requirements | PASS |
| `technical-design` | Requirements, constraints, system elements, integrations, risks, and transition perspectives | PASS |
| `product-backlog` | Scope, needs, capabilities, requirements, rules, risks, decisions, and traceability | PASS |
| `document-output` | Selected shared view with unchanged meaning and status | PASS |

No skill owns normalization or creates a private competing Project View.

## Repository Impact

Created:

- `tests/quality-checklists/project-model.md`
- `tests/executions/2026-07-23-project-model-review.md`

Modified:

- `README.md`
- `PLAN.md`
- `SPEC.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `shared/project-model/README.md`
- `shared/project-model/information-architecture.md`
- `shared/quality-rules/README.md`
- `shared/schemas/README.md`
- `tests/quality-checklists/README.md`

Removed:

- NONE

## Validation

- Four-fixture corpus review: PASS
- Complete-project structural representation: PASS
- Common Information Architecture ADR alignment: PASS
- Canonical Domain Model version 0.1 compliance: PASS
- Minimal Knowledge Model version 0.1 compliance: PASS
- Separation between evidence, normalization, and skills: PASS
- Bidirectional traceability boundary: PASS
- Project Model checklist: PASS

## CI and Quality Checks

| Check | Result |
| --- | --- |
| Documentation updated | PASS |
| Validation against four fixtures | PASS |
| Complete-project representation | PASS |
| Normalized canonical elements represented | PASS |
| Project relationships represented | PASS |
| Established, Provisional, and Unresolved states separated | PASS |
| Existing, Target, and Transition perspectives separated | PASS |
| Supporting, Qualifying, and Opposing knowledge traced | PASS |
| Contradictions preserved without unsupported resolution | PASS |
| Canonical Domain Model unchanged | PASS |
| Knowledge Model unchanged | PASS |
| Information Architecture ADR aligned | PASS |
| Repository consistency | PASS |
| Markdown validation | PASS |
| Local Markdown links | PASS |
| Plugin manifests | PASS |
| Skill foundations | PASS |
| Skills compatibility | PASS |
| Golden Outputs unchanged | PASS |
| Functional skill execution | NOT APPLICABLE |

Functional skill execution is not applicable because this iteration defines a
shared conceptual model and no detailed skill methodology consumes it yet.

## Assumptions

- Human validation and authorized Decisions govern material resolution.
- One Project View represents one bounded Project.
- Knowledge references are stable enough for conceptual validation while
  identifier representation remains deferred.
- Completeness is evaluated for a declared consumption purpose.
- Skills can select relevant elements without changing normalized meaning.

## Open Questions

- Stable Project View, Element, Relationship, and Knowledge Basis identity.
- Authorization rules for establishing, accepting provisionally, or reopening
  normalized information.
- Change propagation from Knowledge Assertions to Project Elements and
  generated artefacts.
- Representation of unresolved concerns as one element, several candidates,
  or related Open Questions.
- Controlled direction and kinds for selected canonical relationships.
- Skill-specific readiness and blocking rules.

## Future Evolution Recommendations

No change to the Canonical Domain Model or Knowledge Model is required.

Stable identity, versioning, reverse derivation lookup, change impact, and
schemas should be designed only after `project-framing` validates real
consumption. Deferred `Measure`, `Data Entity`, `System Element` kinds, and
relationship-direction questions remain candidates for a future explicit
architectural decision.

## Recommendation

Iteration 8 should implement `project-framing`. It is the next logical step
because the plugin now has stable semantic, evidence, and normalization
foundations. The skill should consume the shared Project View, define
purpose-specific readiness, and validate framing outputs against all four
fixtures without re-normalizing source knowledge.

## Git Status

Changes are local only. No commit or push was performed.

## Result

PASS
