# Minimal Normalized Project Model

- Version: 0.1
- Status: Defined
- Scope: Current normalized project understanding

## Purpose

The Project Model represents the coherent current understanding of a project
after relevant knowledge has been consolidated.

It sits between the evidence-preserving Knowledge Model and future skills:

```text
Knowledge Model
        |
        v
Project Model
        |
        v
Skills
```

The model consumes version 0.1 of the
[Minimal Knowledge Model](../knowledge-model/README.md) and uses version 0.1
of the
[Canonical Domain Model](../terminology/canonical-domain-model.md) as its
semantic contract.

This document defines conceptual responsibilities only. It does not define
fields, identifier formats, cardinalities, schemas, serialization,
normalization algorithms, persistence, change workflows, or skill
methodologies.

## Model Boundary

The Project Model answers:

- What is the current normalized understanding of the Project?
- Which canonical project elements are represented?
- Which information is established, provisional, or unresolved?
- Does an element concern an existing condition, a target condition, or a
  transition?
- How are normalized project elements related?
- Which Knowledge Assertions support, qualify, or oppose each normalized
  element or relationship?

The Project Model does not:

- replace source documents or the Knowledge Model;
- preserve every original assertion or its complete epistemic profile;
- choose between conflicting assertions without an authorized basis;
- create missing project information by inference;
- generate documents, backlogs, designs, or other artefacts;
- execute framing, functional, technical, backlog, or output methodology;
- define platform, storage, or integration behavior.

## Minimal Structure

The model contains six conceptual constructions:

```text
Project View
    |
    +-- Project Element
    |     +-- Normalization Status
    |     +-- Lifecycle Perspective
    |     +-- Knowledge Basis
    |
    +-- Project Relationship
          +-- Normalization Status
          +-- Lifecycle Perspective
          +-- Knowledge Basis
```

These constructions belong to the Project Model. They are not new Canonical
Domain Model concepts and do not modify Knowledge Model responsibilities.

### Project View

**Definition:** A coherent snapshot of the current normalized understanding
of one Project for a declared knowledge baseline and review context.

**Purpose:** Give every future skill the same project-wide frame instead of
letting each skill derive its own truth from source documents.

A Project View:

- is anchored by one normalized `Project` element;
- contains the relevant Project Elements and Project Relationships;
- records unresolved information that materially affects its use;
- identifies the Knowledge Model baseline from which it was normalized;
- represents current understanding, not necessarily the existing operational
  state of the organization or solution.

The word "current" refers to the latest accepted understanding within the
view. Existing, target, and transition conditions are distinguished by
Lifecycle Perspective.

A view may be partial. Its existence does not claim that the project is
complete, approved, or ready for delivery. A later normalization may produce
a revised view, but identity and version representation remain outside
version 0.1.

Examples:

- A view of the Service Request Workspace can contain a provisional Project,
  Objective, and target Capabilities while keeping ownership, Scope, and
  terminology unresolved.
- A view of the Case Ledger modernization can contain existing System
  Elements, target Objectives, and unresolved Transition choices together.

### Project Element

**Definition:** An independently referenceable normalized instance of one
Canonical Domain Model concept within a Project View.

**Purpose:** Represent project information in stable shared vocabulary rather
than as duplicated source wording.

A Project Element expresses one coherent project meaning. It:

- uses exactly one of the 22 canonical concepts as its primary meaning;
- states the normalized project information in context;
- carries a Normalization Status;
- uses a Lifecycle Perspective when state distinction matters;
- links to its Knowledge Basis;
- relates to other Project Elements through Project Relationships.

One Knowledge Assertion may contribute to several Project Elements, and one
Project Element may consolidate several assertions. The Project Element does
not copy every assertion, confidence assessment, validation state, or source
location; those remain in the Knowledge Model.

When source language spans several canonical meanings, normalization creates
the necessary elements and relationships instead of inventing a composite
canonical concept.

Examples:

- "Reduce lost requests" can become an `Objective` element linked to a
  `Need`, rather than remaining a sentence copied from the
  [incomplete-project context note](../../tests/fixtures/incomplete-project/context-note.md).
- The proposed calendar synchronization in the
  [new-application roadmap](../../tests/fixtures/new-application/mvp-and-roadmap.md)
  can become an `Option` element related to an `Integration` element; it must
  not become established target Scope merely because it was mentioned.
- Case Ledger, its database, scheduled jobs, and attachment share can become
  distinct `System Element` instances at the granularity justified by the
  [system inventory](../../tests/fixtures/application-modernization/technical/system-inventory.md).

### Project Relationship

**Definition:** An independently referenceable normalized connection between
Project Elements.

**Purpose:** Preserve project-wide meaning that depends on how canonical
concepts interact.

Relationships reuse the semantics described by the Canonical Domain Model,
for example:

- an `Objective` addresses a `Need`;
- a `Requirement` refines a `Capability`;
- a `Business Rule` governs a `Process`;
- an `Integration` connects `System Element` instances;
- a `Transition` changes a `Process` or `System Element`;
- a `Decision` selects or rejects an `Option`.

A relationship may also carry Normalization Status, Lifecycle Perspective,
and Knowledge Basis when the connection itself is provisional or unresolved.
Direction, cardinality, and storage representation are deliberately deferred.

A dependency remains a relationship between elements rather than a new
canonical concept.

Examples:

- The relationship between department membership and an approving manager is
  unresolved because the
  [technical assumptions](../../tests/fixtures/contradictory-project/technical-assumptions.md)
  state that the identity team has not confirmed it.
- The relationships from the nightly directory `Integration` element to its
  source and target `System Element` instances can be established or
  provisional, depending on review of the
  [interface notes](../../tests/fixtures/application-modernization/technical/interface-notes.md).
- The target approval `Business Rule` governs the place-request `Process` in
  the
  [new-application service rules](../../tests/fixtures/new-application/service-rules.md).

### Normalization Status

**Definition:** The degree to which a Project Element or Project Relationship
can serve as the coherent current project view.

**Purpose:** Let skills consume normalized information without mistaking a
working position or known gap for established project direction.

The minimal statuses are:

- **Established:** accepted as the current normalized project understanding
  for the view's context, supported by reviewed and applicable knowledge with
  sufficient authority or by an authorized Decision;
- **Provisional:** an explicit working position is available but remains
  conditional on validation, an Assumption, an Open Question, or limited
  authority;
- **Unresolved:** no coherent current position can be established because
  information is missing, ambiguous, contradictory, or awaiting an
  authoritative decision.

Normalization Status is distinct from Knowledge Model Validation Status:

- Knowledge validation asks whether an assertion has been reviewed;
- normalization asks how consolidated project information may be used.

A validated assertion can still contribute to an `Unresolved` element when
another validated assertion contradicts it. A `Provisional` element requires
an explicit working basis; the Project Model must not invent one merely to
avoid an unresolved state.

`Rejected` and `Superseded` are not Project Model statuses in version 0.1.
Rejected project choices are represented through `Option` and `Decision`
elements when relevant, while assertion rejection and supersession remain in
the Knowledge Model.

An `Unresolved` status is also distinct from the canonical `Open Question`
concept. The status qualifies normalized information; an `Open Question`
element represents an actionable project need for information or decision.
Create an Open Question element when that need matters to the project, not
automatically for every unresolved element.

### Lifecycle Perspective

**Definition:** An optional qualification indicating whether normalized
information concerns an existing condition, a target condition, or the change
between them.

**Purpose:** Prevent current-state observations, future intentions, and
transition work from being combined into one ambiguous project view.

The minimal perspectives are:

- **Existing:** the current or as-is organization, process, behavior, or
  solution condition;
- **Target:** the intended future or to-be condition;
- **Transition:** the change path between existing and target conditions.

Project-wide elements such as the Project, Organization, or an enduring
Objective need no perspective when the distinction is not meaningful. If the
perspective is material but unknown, the information remains unresolved
rather than receiving a guessed perspective.

Lifecycle Perspective does not change canonical meaning. A `Process` remains
a Process in existing and target perspectives. The canonical `Transition`
concept describes a coordinated change, while the Transition perspective
qualifies any element or relationship that belongs to that change context.

Examples:

- The shared mailbox and spreadsheet workflow in the
  [incomplete-project workshop](../../tests/fixtures/incomplete-project/discovery-workshop.md)
  has Existing perspective, while request submission through a future
  workspace has Target perspective.
- The current Case Ledger application, interfaces, issues, and support
  practices have Existing perspective.
- Migration sequencing, rollback, training, and parallel operation in the
  [modernization constraints](../../tests/fixtures/application-modernization/migration/constraints.md)
  have Transition perspective.

### Knowledge Basis

**Definition:** The traceable set of Knowledge Assertions or Assertion Groups
used to establish, qualify, dispute, or leave unresolved a Project Element or
Project Relationship.

**Purpose:** Preserve the audit path through normalization without duplicating
the evidence layer.

The minimal evidence roles are:

- **Supporting:** knowledge that supports the normalized meaning or selected
  position;
- **Qualifying:** knowledge that limits its scope, applicability, certainty,
  or interpretation;
- **Opposing:** knowledge that materially conflicts with or disputes the
  normalized meaning.

The Knowledge Basis also explains the normalization rationale when several
assertions are consolidated or when an authorized Decision resolves a
conflict. The rationale does not become new source evidence.

Every material Project Element and Project Relationship must have a Knowledge
Basis. For an unresolved element, the basis preserves all material
alternatives and gaps through references to the Knowledge Model. For an
established resolution, the basis retains relevant opposing knowledge and
identifies the authorized support for the selected view.

The mapping supports both traceability directions:

```text
Project Element or Relationship
        |
        v
Supporting, Qualifying, and Opposing Knowledge
        |
        v
Source artefact locations

Knowledge Assertion or Assertion Group
        |
        v
Derived Project Elements and Relationships
```

This derivation mapping belongs to the Project Model boundary. It does not
require a modification to the frozen Knowledge Model. Stable reference and
reverse-index representation are deferred.

## Normalization Rules

1. Normalize project meaning, not document wording.
2. Use the canonical concept definitions without renaming, merging, or
   extending them.
3. Consolidate equivalent or refining assertions only when their contexts are
   compatible.
4. Never select a winner because a source is newer, more numerous, or
   expressed with higher confidence.
5. Establish a disputed position only when reviewed, applicable, and
   sufficiently authoritative knowledge or an authorized Decision justifies
   the resolution.
6. Use `Provisional` only for an explicit working position and preserve its
   condition, Assumption, Open Question, and Risk where relevant.
7. Use `Unresolved` when gaps or conflicts prevent a coherent position;
   summarize material alternatives without copying every assertion.
8. Keep materially opposing knowledge linked even after an authorized
   resolution.
9. Distinguish Existing, Target, and Transition perspectives whenever mixing
   them could change meaning.
10. Do not create placeholders for every absent concept. Absence from the
    Project View means "not represented"; it does not mean "known absent,"
    "not applicable," or "unresolved."
11. Represent a material known gap as an unresolved element or related Open
    Question only when the Knowledge Model or declared consumption purpose
    justifies it.
12. New project information enters through source documents and the Knowledge
    Model before it changes the Project View.

## Consolidation Outcomes

Knowledge can produce four useful outcomes without adding more statuses:

| Knowledge condition | Project Model outcome |
| --- | --- |
| Compatible, reviewed, applicable, and sufficiently authoritative knowledge supports one meaning | Established element or relationship |
| An explicit working assumption or limited-authority position exists | Provisional element or relationship |
| Material conflict lacks authorized resolution | Unresolved element or relationship with alternatives in its Knowledge Basis |
| Material information is known to be missing | Unresolved element or related Open Question, without invented content |

Knowledge that is irrelevant to the current Project View remains in the
Knowledge Model. The Project Model is a normalized representation, not a
second evidence archive.

## Traceability Contract

The complete traceability chain remains:

```text
Generated statement
        |
        v
Project Element or Relationship
        |
        v
Knowledge Assertion or Assertion Group
        |
        v
Source artefact and location
```

Every generated material statement must be traceable to a referenceable
Project Element or Project Relationship. Every material Project Element and
Project Relationship must be traceable through its Knowledge Basis.

If a skill produces a proposal, decision record, or other artefact that later
changes the project understanding, human acceptance does not mutate the
Project Model directly. The accepted artefact re-enters a later cycle as a
source document, becomes Knowledge Assertions, and is then normalized.

## Consumption by Future Skills

All future skills consume the same Project View. They may select relevant
elements and relationships, but they must not create private competing
versions of normalized project truth.

- `project-framing` consumes Project, Organization, Stakeholder, Objective,
  Scope, Constraint, Assumption, Decision, Open Question, Risk, Issue, and
  Transition elements.
- `functional-design` consumes Actor, Need, Capability, Process, Requirement,
  Business Rule, Scope, Decision, and Open Question elements and their
  relationships.
- `technical-design` consumes Requirement, Constraint, System Element,
  Integration, Transition, Risk, Issue, Option, and Decision elements across
  Existing, Target, and Transition perspectives.
- `product-backlog` consumes normalized Scope, Need, Capability, Requirement,
  Business Rule, Risk, Decision, and related traceability.
- `document-output` consumes the selected Project View without changing its
  normalized meaning or status.

Consumption rules are consistent:

- `Established` information may be used as the current normalized view;
- `Provisional` information must retain its condition and must not be
  presented as established;
- `Unresolved` information must remain visible and may block or qualify an
  output according to the future skill methodology;
- Knowledge Basis references remain available for audit and explanation.

Skill-specific readiness, required sections, prioritization, acceptance
criteria, and presentation rules remain outside the Project Model.

## Completeness and Readiness

The Project Model does not define one universal `Complete` status. Completeness
depends on a declared purpose: a framing review, functional design, technical
design, backlog preparation, and document output require different subsets of
project information.

A Project View can represent a project that is complete for a declared
purpose when:

- every project element and relationship required by that purpose is
  represented;
- unresolved blockers for that purpose have been resolved or explicitly
  accepted by an authorized Stakeholder;
- provisional information remains visible and is acceptable for that use;
- traceability is complete.

The same structures represent incomplete projects. Future skills define their
own required concept sets and blocking conditions without changing the shared
model.

None of the permanent fixtures claims to be a fully complete project. The
model's ability to represent completeness is therefore validated
structurally, while the fixtures validate incomplete, contradictory,
modernization, and new-application states empirically.

## Fixture Validation

The following examples demonstrate representability. They are not approved
Project Models for the fictional fixtures.

### Incomplete Project

The model can represent the Service Request Workspace Project, Organization,
Objective, Existing Process, and proposed target Capabilities while leaving
ownership, final Scope, Requirements, integrations, service targets, and
Domain Terms provisional or unresolved.

Known gaps such as monthly volume and retention become unresolved elements or
Open Questions only when material. Ambiguous terms remain unresolved Domain
Term elements. No missing value is invented.

### Contradictory Project

The model can consolidate compatible project context while keeping retention,
approval, eligibility, response time, reporting interface, rollout, cutover,
and priority positions unresolved.

For example, one unresolved `Business Rule` element can summarize that the
retention period is not normalized, while its Knowledge Basis links the two-,
three-, five-, and seven-year assertions. A later authorized Decision can
establish one position without deleting the opposing knowledge.

### Application Modernization

Existing-perspective System Elements, Processes, Integrations, Issues, and
operational Constraints can coexist with target Objectives and Requirements
and transition-perspective Options, Risks, Constraints, and Open Questions.

The reopening rule remains unresolved while the 2019 guide, advisor practice,
and support observations conflict. Migration strategy remains unresolved
until a Decision selects among replacement, sequencing, parallel-operation,
and history-treatment options.

### New Application

The Project View can normalize the Organization, Stakeholders, Actors,
Objectives, target Capabilities, Processes, Business Rules, and Requirements.
The proposed MVP remains provisional Scope until authorized. Future ideas are
Option elements rather than commitments.

Product ownership, rollout, volume, waiting lists, approval delegation,
calendar scope, retention, support, hosting, and language selection remain
Open Questions or unresolved related elements.

### Complete Project

A purpose-complete Project View uses the same constructions with all required
elements and relationships represented, no unaccepted unresolved blockers,
and complete Knowledge Basis links. No separate model variant or speculative
concept is required.

## Main Architectural Decisions

### Normalize Canonical Instances, Not Assertions

Project Elements represent consolidated project meaning. Assertions remain in
the Knowledge Model and are referenced through Knowledge Basis.

### Use Three Normalization Statuses

`Established`, `Provisional`, and `Unresolved` cover the corpus without
combining review status, confidence, approval, or history into one lifecycle.

### Do Not Force Resolution

A coherent model can state coherently that a matter is unresolved. This is
safer than choosing an unsupported value and still gives skills a consumable
project state.

### Separate View Currency from Lifecycle Perspective

The Project View is the current understanding. Existing, Target, and
Transition indicate what condition an element describes. Keeping these
dimensions separate is essential for modernization.

### Keep Evidence Roles Minimal

Supporting, Qualifying, and Opposing links provide sufficient normalization
traceability without copying Knowledge Model relationships or epistemic
profiles.

### Make Completeness Purpose-Relative

A universal completeness flag would either be misleading or embed every skill
methodology in the shared model. Skills will evaluate readiness against one
shared Project View.

## Architecture Compliance

- Canonical Domain Model concepts added: **NONE**
- Canonical Domain Model concepts removed: **NONE**
- Canonical Domain Model concepts modified: **NONE**
- Knowledge Model constructions modified: **NONE**
- Knowledge Model responsibilities modified: **NONE**

Project View, Project Element, Project Relationship, Normalization Status,
Lifecycle Perspective, and Knowledge Basis are Project Model constructions.
They implement responsibilities explicitly reserved for this layer by the
Canonical Domain Model and the Information Architecture ADR.

## Assumptions

- Human validation and authorized Decisions remain the basis for resolving
  material conflicts.
- The Knowledge Model can provide stable-enough references during conceptual
  review even though identifier representation is deferred.
- One Project View covers one bounded Project; cross-project portfolio
  modeling is outside version 0.1.
- Skills can consume selected portions of a shared view without changing its
  normalized meaning.
- Complete means complete for a declared consumption purpose, not universally
  free of risk, assumptions, or open questions.

## Unresolved Questions

- What representation will provide stable identities and versions for Project
  Views, Elements, Relationships, and Knowledge Basis links?
- Which roles may establish, accept provisionally, or reopen normalized
  project information?
- How are changes in Knowledge Assertions propagated to affected Project
  Elements and generated artefacts?
- When should an unresolved concern be one Project Element, several candidate
  elements, or an Open Question related to them?
- Which canonical relationships require controlled direction or kinds?
- How will skill-specific readiness rules declare required elements and
  blocking statuses?

## Recommendations for Future Evolution

No Canonical Domain Model or Knowledge Model change is required by this
iteration.

Future representation work should define stable identity, versioning, reverse
derivation lookup, and change impact only after project-framing demonstrates
how the model is consumed. Previously deferred questions about `Measure`,
`Data Entity`, `System Element` kinds, and canonical relationship direction
remain candidates for explicit architectural review rather than implicit
Project Model extensions.

## Next Iteration

Iteration 8 should implement the first complete `project-framing`
methodology. It should consume the Project Model without re-normalizing source
knowledge, define purpose-specific readiness and blocking rules, and validate
its output against all four permanent fixtures.
