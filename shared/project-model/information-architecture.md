# ADR-001: Common Information Architecture

- Status: Accepted
- Date: 2026-07-23
- Scope: Shared information architecture
- Implementation status: Knowledge Model v0.1 defined; Project Model TO BE
  DEFINED

## Decision Summary

Adopt **Option B: Knowledge Model + Project Model**.

```text
Source documents
        |
        v
Extracted Knowledge Model
        |
        v
Normalized Project Model
        |
        v
Skills
        |
        v
Generated artefacts
```

This decision defines responsibilities and boundaries only. It does not define
schemas, fields, identifiers, serialization, extraction rules, confidence
algorithms, conflict-resolution rules, or skill methodologies.

## Canonical Domain Model

The
[Canonical Domain Model](../terminology/canonical-domain-model.md)
defines the common vocabulary used by the Knowledge Model, Project Model, and
future skills.

It is not a processing layer and does not change the accepted information
flow. It defines the meaning of shared concepts while the Knowledge Model
defines evidence state and the Project Model defines normalized project
instances.

## Context from the Reference Corpus

The four permanent fixtures expose different architectural pressures:

- `incomplete-project` contains useful statements alongside missing owners,
  rules, constraints, integrations, definitions, and decisions. Unknown
  information must remain unknown.
- `contradictory-project` contains incompatible statements about eligibility,
  approval, response targets, rollout, retention, reporting, cutover, and
  priorities. Every statement must survive normalization until an authorized
  decision resolves it.
- `application-modernization` combines observations, outdated approved
  documentation, historical decisions, undocumented behavior, technical
  inventory, and uncertain migration constraints. Source date, authority, and
  context materially affect interpretation.
- `new-application` distinguishes objectives, requested capabilities, explicit
  rules, proposed MVP scope, future ideas, assumptions, and open decisions.
  These categories must not collapse into approved requirements.

A normalized project view is necessary for future skills, but normalization
alone cannot safely preserve every source statement, qualification, conflict,
or uncertainty exposed by this corpus.

## Evaluated Architectures

### Option A: Single Project Model

```text
Documents -> Project Model -> Skills
```

The Project Model would contain both normalized project concepts and the
source evidence required to justify them.

Advantages:

- Lowest initial conceptual and implementation cost.
- Short processing path.
- Direct consumption by skills.
- Straightforward mapping to external structured artefacts.

Drawbacks:

- Mixes source interpretation with normalized project information.
- Makes the Project Model responsible for raw claims, confidence, conflicts,
  validation state, and canonical concepts.
- Risks losing competing statements during normalization.
- Becomes increasingly complex as traceability and uncertainty requirements
  grow.
- Encourages skills to depend on evidence-handling details.

This option is adequate for small, consistent inputs but does not safely cover
the contradictory and modernization fixtures without turning the Project
Model into two models hidden inside one structure.

### Option B: Knowledge Model + Project Model

```text
Documents -> Knowledge Model -> Project Model -> Skills
```

The Knowledge Model preserves extracted statements and their epistemic state.
The Project Model provides normalized project information linked to that
knowledge.

Advantages:

- Separates evidence preservation from project normalization.
- Keeps contradictory and uncertain statements visible.
- Supports complete forward and reverse traceability.
- Gives all skills one stable, normalized project view.
- Allows extraction and normalization to evolve independently.
- Provides a clear integration boundary for external formats such as Spec Kit.

Drawbacks:

- Introduces one additional shared concept and lifecycle.
- Requires explicit rules for promoting or relating knowledge to normalized
  project information.
- Requires identity and versioning across layers.
- Can become over-engineered if the Knowledge Model expands beyond evidence
  and epistemic state.

This option adds justified complexity because the permanent corpus already
demonstrates the need for both evidence preservation and normalization.

### Option C: Unified Evidence Graph with Skill Projections

```text
Documents -> Evidence graph -> Skill-specific projections -> Artefacts
```

All source statements, project concepts, and relationships would live in one
graph. Each skill would consume a projection tailored to its responsibility.

Advantages:

- Strong relationship and conflict representation.
- Excellent scalability for dense cross-project relationships.
- Flexible traversal and impact analysis.
- Direct provenance paths.

Drawbacks:

- Highest conceptual and implementation complexity.
- Requires graph semantics, projection rules, and stronger tooling.
- Makes skill behavior depend on projection design.
- Is less natural for a Markdown-first, documentation-first repository.
- Complicates portability and mapping to document-oriented external systems.
- Solves scale and query problems not yet demonstrated by the corpus.

This option may become relevant if future evidence shows that graph traversal
is essential. It is not justified for the current plugin.

## Comparison

| Criterion | Option A: Single Model | Option B: Knowledge + Project | Option C: Evidence Graph |
| --- | --- | --- | --- |
| Conceptual simplicity | High initially | Medium | Low |
| Implementation complexity | Low initially, hidden growth | Medium and explicit | High |
| Maintainability | Medium | High with strict boundaries | Medium, tooling-dependent |
| Scalability | Medium | High | Very high |
| Traceability | Medium; easy to blur | High and explicit | High |
| Conflict management | Low to medium | High | Very high |
| Uncertainty handling | Medium | High | High |
| Future AI reasoning | Medium; mixed context | High; evidence and normalization separated | High but cognitively expensive |
| Compatibility with all skills | Medium | High | High through projections |
| Spec Kit compatibility | High for simple mappings, weaker provenance | High through the Project Model adapter boundary | Medium; graph translation required |
| Long-term evolution | Medium | High | High capability, high cost |

## Selected Responsibilities

### Source Documents

Source documents are the received artefacts. They preserve original content,
context, authorship or role when known, date or version when known, and a
stable location that can be cited.

They do not contain plugin interpretation or normalized project truth.
Source content remains unchanged by extraction and normalization.

### Extracted Knowledge Model

The Knowledge Model records what has been extracted from source documents
without prematurely deciding what the project truth should be.

Version 0.1 is defined in the
[Minimal Knowledge Model](../knowledge-model/README.md).

Its responsibility is to preserve:

- an extracted statement or observation;
- its source artefact and precise source location;
- its nature, such as fact, interpretation, assumption, proposal, decision, or
  open question;
- source authority, date, and context when available;
- confidence or reliability assessment only when justified, including the
  basis for that assessment;
- validation state;
- supporting, equivalent, superseding, or contradictory relationships;
- uncertainty and missing information;
- links to the normalized project information derived from it.

The Knowledge Model does not:

- resolve conflicts without an authorized decision;
- silently merge similar statements;
- define canonical project structure;
- contain skill-specific methodology;
- contain generated deliverables.

### Normalized Project Model

The Project Model represents the coherent, normalized project information
consumed by every skill.

Its responsibility is to:

- organize shared project concepts consistently;
- distinguish existing state, target state, and transition concerns;
- expose validated information and unresolved alternatives;
- preserve links to all supporting and opposing knowledge;
- represent project-wide relationships needed across skills;
- provide a stable boundary for skill inputs and external adapters;
- avoid coupling to a platform, document format, methodology, or integration.

The Project Model does not:

- replace source documents;
- store unqualified extracted statements as canonical truth;
- resolve uncertainty by inference alone;
- own a specialized skill's methodology;
- contain presentation-specific generated artefacts.

### Generated Artefacts

Generated artefacts are outputs produced by specialized skills or the
orchestrator. They present selected project information for a defined purpose
and audience.

Every material generated statement must reference one or more Project Model
elements. Those elements must reference the Knowledge Model statements that
support, qualify, or oppose them, and each knowledge statement must reference
its source location.

A generated artefact does not automatically become project evidence. If a
human review turns it into an approved input or decision record, it must enter
a later cycle as an explicit source artefact. This prevents circular
provenance.

## End-to-End Traceability

The required traceability chain is:

```text
Generated statement
        |
        v
Project Model information
        |
        v
Extracted knowledge statement(s)
        |
        v
Source artefact location(s)
```

Traceability must support multiple sources, competing sources, and unresolved
knowledge. Normalization must never erase a source path.

## Relationship with Future Skills

- `project-framing` consumes normalized context, objectives, scope,
  stakeholders, constraints, risks, assumptions, and unresolved questions
  while retaining evidence links.
- `functional-design` consumes normalized actors, needs, rules, scope, and
  decisions, and traces functional statements to supporting knowledge.
- `technical-design` consumes current-state evidence, functional needs,
  constraints, non-functional requirements, risks, and decisions without
  confusing proposals with approved choices.
- `product-backlog` consumes normalized scope, requirements, risks, and
  decisions, and keeps every backlog item traceable to project information.
- `document-output` assembles generated artefacts while preserving status,
  terminology, provenance, and unresolved issues.

No skill owns either shared model. A skill may consume a relevant view and
produce artefacts, but shared information responsibilities remain independent
from individual methodologies.

## Spec Kit Compatibility

Spec Kit remains optional. A future adapter should map approved Project Model
information to Spec Kit artefacts. The Knowledge Model remains available for
provenance, qualification, and conflict context but does not force Spec Kit to
adopt the plugin's internal evidence representation.

This keeps integration logic under `integrations/spec-kit/` and prevents Spec
Kit structures from leaking into shared models.

## Consequences

### Benefits

- Source fidelity survives normalization.
- Conflicts and uncertainty remain first-class concerns.
- Skills receive a consistent project view without parsing raw evidence
  independently.
- Generated content can be audited end to end.
- Platform and integration adapters depend on stable normalized information.

### Costs and Risks

- Two shared model lifecycles must remain synchronized.
- Promotion from knowledge to normalized project information needs clear,
  testable governance.
- Identity, versioning, and change impact must work across layers.
- Excessive confidence scoring or claim fragmentation could add noise without
  improving decisions.
- Duplicating the same concept in both models without a clear responsibility
  would erase the benefit of the separation.

## Repository Impact

The accepted architecture is documented here. The conceptual Knowledge Model
now has a dedicated `shared/knowledge-model/` location because its minimal
constructions and boundaries have been validated against all four fixtures.

No Knowledge Model schema or runtime implementation exists. The future
normalized Project Model remains in `shared/project-model/`.

## Assumptions

- Source artefacts remain available and can be addressed at a stable location.
- Human validation remains authoritative for decisions and Golden Outputs.
- Most future integrations consume normalized project information rather than
  raw extracted knowledge.
- The corpus represents the minimum diversity the architecture must support,
  not every future project type.

## Unresolved Questions

- How are stable identities and versions maintained across all layers?
- When does a normalized Project Model element remain unresolved rather than
  absent?
- How are model changes and downstream generated artefacts invalidated?
- Which validation transitions require authorization, and by whom?
- How does the Project Model reference supporting, qualifying, and opposing
  assertions?

These questions belong to model implementation and must be answered
incrementally from the corpus, not by adding speculative abstractions here.

## Next Iteration

Define the minimal normalized Project Model, consuming the
[Minimal Knowledge Model](../knowledge-model/README.md) through the unchanged
Canonical Domain Model.

This sequencing is now possible because source statements, provenance,
uncertainty, conflicts, and coexistence have been defined and validated
without assigning them to the Project Model.

The next iteration must test normalization and bidirectional traceability
against all four permanent fixtures before defining schemas or skill
methodology.
