# Canonical Domain Model Review

- Date: 2026-07-23
- Reviewer: Codex
- Platform: Platform independent
- Invocation: Conceptual model review
- Source commit: WORKTREE, uncommitted
- Skills: All future skills
- Scenarios: All four permanent fixtures
- Golden output: NONE

## Objective

Validate version 0.1 of the
[Canonical Domain Model](../../shared/terminology/canonical-domain-model.md)
as the minimum shared vocabulary for the Knowledge Model, Project Model, and
future skills.

## Model Summary

- Retained concepts: 22
- Concept groups: Project Foundation, Domain and Behavior, Governance and
  Uncertainty, Solution and Change
- Verified corpus citations: 42
- Processing pipeline impact: NONE
- Schemas or serialization introduced: NONE

## Fixture Validation

| Fixture | Main concepts exercised | Result |
| --- | --- | --- |
| `incomplete-project` | Project, stakeholders, actors, objectives, needs, capabilities, process, assumptions, questions, terms, integrations, and missing scope | PASS |
| `contradictory-project` | Scope, rules, requirements, assumptions, options, decisions, constraints, integrations, and transition alternatives | PASS |
| `application-modernization` | Processes, system elements, issues, risks, requirements, integrations, historical decisions, and transition | PASS |
| `new-application` | Objectives, stakeholders, actors, needs, capabilities, scope, rules, requirements, constraints, integrations, options, and open decisions | PASS |

Every retained concept has at least one verified reference-corpus example.

## Canonical Domain Model Checklist

### Corpus Evidence

- Every retained concept has corpus evidence: PASS
- Every retained concept serves multiple skills or a shared-model boundary:
  PASS
- All four fixtures can use the model without unsupported concepts: PASS

### Concept Quality

- Definitions and purposes are explicit: PASS
- Aliases preserve one canonical meaning: PASS
- Relationships remain conceptual: PASS
- Overlaps are merged or justified: PASS
- Exclusions and deferred concepts are documented: PASS

### Separation of Concerns

- Project-specific instances excluded: PASS
- Knowledge Model responsibilities excluded: PASS
- Project Model lifecycle and identity excluded: PASS
- Skill-specific methodology and artefacts excluded: PASS
- Schemas, serialization, and runtime behavior excluded: PASS

### Architecture Compatibility

- Canonical model remains outside the processing pipeline: PASS
- Information Architecture ADR compatibility: PASS
- All future skills share the vocabulary: PASS
- Spec Kit remains optional: PASS
- Technology and methodology independence: PASS

## Main Decisions Reviewed

| Decision | Result |
| --- | --- |
| Keep Stakeholder separate from Actor | PASS |
| Keep Need separate from Requirement | PASS |
| Keep Capability separate from System Element | PASS |
| Use one Requirement concept with later kinds | PASS |
| Merge application, module, component, service, job, and data store into System Element | PASS |
| Keep Risk separate from Issue | PASS |
| Retain Transition as a shared concept | PASS |
| Treat Persona as an Actor representation | PASS |
| Keep epistemic proposal classification separate from canonical Option | PASS |

## CI and Quality Checks

| Check | Result |
| --- | --- |
| Documentation updated | PASS |
| Validation against four fixtures | PASS |
| Canonical concepts justified | PASS |
| Concept structure complete | PASS |
| Corpus references valid | PASS |
| Information Architecture ADR aligned | PASS |
| Repository consistency | PASS |
| Local Markdown links | PASS |
| Knowledge Model unchanged | PASS |
| Project Model implementation unchanged | PASS |
| Golden Outputs unchanged | PASS |
| Functional skill execution | NOT APPLICABLE |

Functional skill execution is not applicable because this iteration defines
vocabulary only and no skill methodology consumes implemented shared models
yet.

## Assumptions

- The domain covers software-project design rather than all project-management
  concepts.
- Canonical definitions precede detailed kinds, fields, and validation rules.
- A concept may be refined later only when corpus or cross-skill evidence
  justifies it.
- Localization does not change canonical meaning.

## Open Questions

- Separate Measure concept for objectives and requirements.
- Canonical kinds for System Element.
- Future shared responsibility for Data Entity.
- Direction and lifecycle semantics for selected relationships.
- Controlled kinds versus project-defined terminology.

These questions do not block version 0.1.

## Result

PASS

The Canonical Domain Model is ready to constrain the minimal Knowledge Model
in the next iteration.
