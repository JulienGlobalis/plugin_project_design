# Information Architecture Review

- Date: 2026-07-23
- Reviewer: Codex
- Platform: Platform independent
- Invocation: Architectural review
- Source commit: WORKTREE, uncommitted
- Skills: All future skills
- Scenarios: All four permanent fixtures
- Golden output: NONE

## Decision Under Test

Adopt the layered Source Documents, Knowledge Model, Project Model, Skills,
and Generated Artefacts architecture defined in
[`plugins/project-design/shared/project-model/information-architecture.md`](../../../plugins/project-design/shared/project-model/information-architecture.md).

## Corpus Coverage

| Fixture | Architectural pressure | Validation |
| --- | --- | --- |
| `incomplete-project` | Missing information, ambiguous terms, unresolved assumptions, and absent authority must survive without invention. | PASS: the Knowledge Model preserves extracted and missing knowledge; the Project Model exposes unresolved normalized information. |
| `contradictory-project` | Competing eligibility, approval, timing, retention, reporting, cutover, and priority statements must coexist. | PASS: conflicts remain relationships between extracted statements until an authorized decision supports normalization. |
| `application-modernization` | Outdated documentation, observations, historical decisions, technical inventory, and uncertain current behavior need source context. | PASS: source date, authority, context, and knowledge state remain distinct from existing-state and target-state normalization. |
| `new-application` | Objectives, rules, proposed MVP scope, future ideas, assumptions, and open decisions must remain distinct. | PASS: knowledge classification precedes normalization and prevents proposals from becoming approved project truth. |

## Architecture Criteria

| Criterion | Result | Evidence |
| --- | --- | --- |
| Conceptual simplicity | PASS | Option B adds one explicit layer and avoids hiding two responsibilities inside the Project Model. |
| Implementation complexity | PASS | Complexity is moderate, acknowledged, and deferred; no schema or runtime is introduced. |
| Maintainability | PASS | Evidence preservation and normalization can evolve independently behind explicit boundaries. |
| Scalability | PASS | Multiple sources, competing statements, and all future skills are supported without skill-owned models. |
| Traceability | PASS | Generated statement to Project Model to Knowledge Model to source location is mandatory. |
| Conflict management | PASS | Conflicts remain first-class knowledge relationships until authorized resolution. |
| Uncertainty handling | PASS | Unknown, assumed, proposed, and validated information remain distinguishable. |
| Future AI reasoning | PASS | Skills receive normalized context while retaining access to qualifications and provenance. |
| Compatibility with all skills | PASS | Every future skill consumes the shared Project Model and preserves evidence links. |
| Spec Kit compatibility | PASS | The Project Model is the adapter boundary; the Knowledge Model remains optional evidence context. |
| Long-term evolution | PASS | Option B supports new source types and integrations without requiring a graph architecture now. |

## Repository Checklist

- Source fidelity: PASS
- Traceability: PASS
- Consistency: PASS
- Completeness for an architecture decision: PASS
- Assumptions and questions: PASS
- Skill boundaries: PASS
- Methodological quality: NOT APPLICABLE

No skill methodology or detailed model has been implemented.

## Option Disposition

| Option | Assessment | Decision |
| --- | --- | --- |
| A: Single Project Model | Suitable for simple and consistent inputs, insufficient for the permanent corpus | Rejected because evidence and normalization responsibilities would be mixed. |
| B: Knowledge Model + Project Model | Best balance of simplicity, traceability, and extensibility | Accepted as the simplest architecture satisfying all criteria. |
| C: Unified evidence graph with projections | Capable but disproportionate to demonstrated needs | Rejected for now because its complexity is not justified by current evidence. |

## Structural Validation

- Four-fixture corpus unchanged: PASS
- Golden Outputs unchanged: PASS
- Skill methodologies unchanged: PASS
- Spec Kit remains optional: PASS
- Platform independence preserved: PASS

## Unresolved Issues

- Minimal unit of extracted knowledge.
- Confidence and reliability semantics.
- Source authority and freshness.
- Validation states and transitions.
- Identity and versioning across layers.
- Conflict, equivalence, and supersession relationships.
- Downstream invalidation after model changes.

These issues are inputs to the next iteration and do not block the architecture
decision.

## Result

PASS

The architecture decision is validated against all four permanent fixtures.
Knowledge Model and Project Model implementations remain pending.
