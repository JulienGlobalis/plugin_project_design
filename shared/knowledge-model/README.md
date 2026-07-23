# Minimal Knowledge Model

- Version: 0.1
- Status: Defined
- Scope: Extracted project knowledge

## Purpose

The Knowledge Model preserves what a project corpus says before any
normalization decides what the project should treat as its coherent working
view.

It sits between source documents and the future Project Model:

```text
Source documents
        |
        v
Knowledge Model
        |
        v
Project Model
```

The model uses the
[Canonical Domain Model](../terminology/canonical-domain-model.md) as its
semantic contract. It does not add to, remove from, rename, merge, split, or
redefine the 22 canonical concepts in version 0.1.

This document defines conceptual responsibilities only. It does not define
fields, identifiers, cardinalities, schemas, serialization, extraction
algorithms, confidence calculations, persistence, or runtime behavior.

## Model Boundary

The Knowledge Model answers:

- What assertion was extracted or derived from the reviewed corpus?
- Which canonical concept or concepts does it concern?
- Which source and location support the assertion?
- How confidently was the source meaning extracted or interpreted?
- What remains uncertain?
- What is the assertion's review status?
- Which assertions support, contradict, refine, duplicate, or supersede it?

The Knowledge Model does not:

- establish normalized project truth;
- choose between competing assertions;
- silently merge similar statements;
- resolve open questions or contradictions;
- create Project Model instances;
- generate implementation or delivery artefacts;
- define skill methodology.

## Minimal Structure

The model contains six conceptual constructions:

```text
Knowledge Corpus
    |
    +-- Assertion
    |     +-- Canonical Concept Reference
    |     +-- Provenance
    |     +-- Epistemic Profile
    |     +-- Assertion Relationship
    |
    +-- Assertion Group
```

These constructions belong to the Knowledge Model. They are not new
Canonical Domain Model concepts.

### Assertion

**Definition:** An individually referenceable statement that preserves one
meaning extracted from a source or one explicitly qualified interpretation of
the reviewed corpus.

**Purpose:** Preserve source meaning at a granularity that can be traced,
qualified, compared, and later considered during normalization.

An assertion should be atomic enough that its provenance, confidence,
uncertainty, validation status, and relationships can be assessed without
also assessing unrelated meanings. It need not be reduced to an artificial
single clause when the source meaning depends on its context.

An assertion records what a source presents or what a reviewer concludes
about a bounded corpus. It is not automatically accepted project truth.

Examples:

- The
  [Member Service Portal charter](../../tests/fixtures/contradictory-project/project-charter.md)
  states that closed requests and attachments must remain searchable for five
  years.
- The
  [service policy extract](../../tests/fixtures/contradictory-project/service-policy-extract.md)
  states a seven-year retention period.
- The
  [technical intake](../../tests/fixtures/incomplete-project/technical-intake.md)
  does not supply data retention requirements. This may support a
  corpus-scoped interpretation that retention is unresolved in the reviewed
  material; it does not prove that no retention rule exists.

### Canonical Concept Reference

**Definition:** A reference from an assertion to the applicable concepts
defined by the Canonical Domain Model.

**Purpose:** Connect source language to the plugin's shared vocabulary without
turning an assertion into normalized project information.

References use canonical concept names and meanings exactly as defined. More
than one reference is allowed when an assertion genuinely concerns several
concepts. For example, a statement about a proposed calendar connection may
concern both `Integration` and `Option`.

A reference classifies the meaning involved; it does not create a canonical
project instance, assert identity between two source expressions, or decide
the normalized interpretation. If no canonical concept can be justified, the
assertion remains preserved and explicitly unclassified; the gap is recorded
as a recommendation for a future architectural review rather than repaired
inside the Knowledge Model.

Examples:

- "Single sign-on is preferred" in the
  [incomplete-project technical intake](../../tests/fixtures/incomplete-project/technical-intake.md)
  can reference `Integration` and `Assumption`.
- The proposed calendar synchronization in the
  [new-application roadmap](../../tests/fixtures/new-application/mvp-and-roadmap.md)
  can reference `Integration` and `Option`.
- The unapproved migration sequencing in the
  [modernization constraints](../../tests/fixtures/application-modernization/migration/constraints.md)
  can reference `Transition`, `Option`, and `Open Question`.

### Provenance

**Definition:** The source path that explains where an assertion came from
and the context needed to assess that source.

**Purpose:** Make every assertion auditable and prevent extracted or inferred
information from losing its origin.

Provenance includes a source artefact and a precise location within it.
Source date, version, author or role, authority, and relevant context are
preserved when available. Unknown provenance attributes remain explicitly
unknown.

Source authority and freshness describe the source context. They do not
automatically determine whether the assertion is correct. An approved but old
guide and a recent workshop observation can both remain valid evidence while
their relationship is investigated.

A corpus-level assertion, such as "no current data dictionary was found,"
must cite the reviewed corpus scope or the source that records the search. It
must not turn absence from the available material into a universal claim.

Examples:

- The
  [2019 user-guide extract](../../tests/fixtures/application-modernization/documentation/user-guide-extract-2019.md)
  is explicitly dated and approved, but no later revision was supplied.
- The
  [support observations](../../tests/fixtures/application-modernization/operations/support-observations.md)
  report more recent operational behavior without establishing formal
  authority.
- The
  [new-application integration notes](../../tests/fixtures/new-application/integration-notes.md)
  identify several unknown interface details and the teams expected to
  confirm them.

### Epistemic Profile

**Definition:** The qualifications that describe the nature, confidence,
uncertainty, and validation status of an assertion.

**Purpose:** Keep different kinds of knowledge from being treated as equally
established.

The profile keeps four dimensions separate.

#### Nature

The assertion nature describes how the content enters the knowledge base:

- **Fact:** a source presents the statement as an established fact;
- **Interpretation:** a reviewer derives a bounded conclusion from one or more
  sources;
- **Assumption:** the statement is treated as true for reasoning without
  sufficient validation;
- **Proposal:** the statement suggests a possible future choice or action;
- **Decision:** the source records that an authorized choice was made;
- **Open Question:** the statement records information or a decision still
  required.

Nature does not certify truth. `Assumption`, `Decision`, and `Open Question`
also exist as canonical concepts when the assertion concerns those domain
meanings. `Proposal` is an epistemic classification; when it describes a
candidate course of action, it normally references the canonical `Option`
concept.

#### Confidence

Confidence expresses how reliably the source meaning was extracted or how
well an interpretation is supported. The minimal qualitative states are
`High`, `Medium`, `Low`, and `Unknown`, always accompanied by a reason when an
assessment is made.

Confidence is not:

- a probability that the source statement is true;
- a substitute for source authority;
- a validation decision;
- a mechanism for choosing between contradictions.

Qualitative states avoid false numeric precision while the methodology is
still conceptual.

#### Uncertainty

Uncertainty records a known limit affecting an assertion. Corpus-justified
examples include incomplete information, ambiguous terminology, missing
verification, unknown authority, unknown or outdated freshness, and unclear
scope.

Multiple uncertainty reasons may coexist. The absence of a recorded
uncertainty does not prove certainty.

#### Validation Status

Validation status records the review state of an assertion:

- `Unreviewed`;
- `Under Review`;
- `Validated`;
- `Rejected`;
- `Unknown`.

Validation indicates governance or review state, not source truth. A validated
assertion may accurately preserve a source statement that another source
contradicts. Rejection does not delete the assertion or its provenance.
Evolution is represented through assertion relationships rather than by
overwriting history.

Examples:

- The
  [incomplete-project vocabulary notes](../../tests/fixtures/incomplete-project/vocabulary-notes.md)
  make ambiguity about `request`, `ticket`, and `case` explicit.
- The
  [new-application roadmap](../../tests/fixtures/new-application/mvp-and-roadmap.md)
  identifies future ideas as proposals rather than approved commitments.
- The
  [modernization decision history](../../tests/fixtures/application-modernization/governance/decision-history.md)
  records decisions while also stating that their current applicability is
  unknown.

### Assertion Relationship

**Definition:** An explicit, qualified relationship between two assertions.

**Purpose:** Preserve how assertions interact without resolving them.

The minimal relationship set is:

- **Supports:** one assertion provides compatible evidence for another;
- **Contradicts:** two assertions cannot both apply under the recorded
  context;
- **Equivalent:** two assertions preserve materially the same meaning;
- **Refines:** one assertion adds precision without replacing the other;
- **Supersedes:** evidence explicitly indicates that one assertion replaces
  another for a defined context.

Relationships include the comparison context and rationale when needed. A
contradiction is not inferred merely because wording differs. `Supersedes`
must not be inferred from a later date alone. All related assertions remain
available, including rejected or superseded ones.

Examples:

- The five-year retention assertion in the
  [project charter](../../tests/fixtures/contradictory-project/project-charter.md)
  and seven-year assertion in the
  [service policy](../../tests/fixtures/contradictory-project/service-policy-extract.md)
  can be related as `Contradicts` for the same records and period of
  applicability.
- The 2019 statement that closed cases cannot be reopened and the
  [user workshop](../../tests/fixtures/application-modernization/business/user-workshop.md)
  statement that advisors reopen cases require a contradiction relationship;
  recency alone does not establish supersession.
- The new-application business objective to make approvals visible is
  supported and refined by the
  [manager interview](../../tests/fixtures/new-application/stakeholder-interviews.md).

### Assertion Group

**Definition:** A comparison set that keeps multiple assertions about the same
project concern together.

**Purpose:** Allow competing, complementary, evolving, or duplicate assertions
to coexist without selecting a winner or prematurely creating a Project Model
element.

Grouping is justified by shared subject and comparison context, supported by
canonical references and source language. Group membership does not imply
equivalence, consistency, or common authority; those meanings require
explicit assertion relationships.

Examples:

- The retention group in `contradictory-project` can retain the two-, three-,
  five-, and seven-year statements.
- The rollout group can retain September pilot, October launch, 15 October
  launch, November pilot, gradual rollout, and single-cutover assumptions.
- A reopening group in `application-modernization` can retain the approved
  2019 guide, advisor practice, and recent support observation.

## Information Preservation Rules

1. Preserve each materially different assertion and its provenance.
2. Keep source wording and reviewer interpretation distinguishable.
3. Record unknown information as unknown; do not complete it by invention.
4. State corpus absence as a scoped interpretation, not a universal fact.
5. Keep confidence, uncertainty, validation, source authority, and freshness
   separate.
6. Represent conflict through relationships; do not choose a correct
   assertion in this model.
7. Retain history when an assertion is rejected or superseded.
8. Use canonical concepts for semantic reference without creating normalized
   project instances.
9. Leave normalization, conflict resolution, and approval consequences to the
   future Project Model and governance rules.

## Traceability

The Knowledge Model supports the middle of the accepted traceability chain:

```text
Future generated statement
        |
        v
Future Project Model information
        |
        v
Knowledge assertion
        |
        v
Source artefact and location
```

The model therefore requires assertions and source locations to remain
referenceable. The mechanism for stable identity and versioning is deferred
until representation and serialization are designed.

## Fixture Validation

### Incomplete Project

The model preserves known objectives and capabilities alongside unknown
owners, volume, rules, scope, service targets, integrations, and definitions.
Ambiguous terms can remain separate assertions with explicit uncertainty.
Missing information becomes a corpus-scoped interpretation or open question,
not invented project information.

### Contradictory Project

The model retains all assertions about eligibility, approval, response time,
retention, reporting, rollout, cutover, and priorities. Assertion groups make
them comparable, while `Contradicts`, `Supports`, or `Refines` relationships
describe their interaction without selecting a source of truth.

### Application Modernization

The model preserves outdated approved documentation, recent observations,
historical decisions, technical inventory, and unknown current authority.
Freshness, authority, confidence, and validation remain separate. Historical
assertions remain available even when later evidence refines or explicitly
supersedes them.

### New Application

The model distinguishes stated objectives and rules from proposed MVP scope,
future ideas, assumptions, and open decisions. Unknown interface contracts,
manager relationships, volumes, retention, ownership, and rollout remain
unresolved without blocking extraction of the known information.

All four fixtures can be represented without modifying the Canonical Domain
Model and without forcing premature normalization.

## Main Architectural Decisions

### Use Assertions as the Minimum Knowledge Unit

Document fragments are too coarse to qualify precisely, while isolated tokens
lose meaning. An individually referenceable assertion is the smallest useful
unit demonstrated by the corpus.

### Keep Qualification Dimensions Independent

Nature, confidence, uncertainty, validation, authority, and freshness answer
different questions. Combining them into one score would hide useful
distinctions and encourage unsupported ranking.

### Preserve Contradictions as Relationships

Contradiction belongs between assertions and depends on comparison context.
It is not an error state on one assertion and does not authorize automatic
resolution.

### Group Without Normalizing

Assertion Groups support comparison and coexistence while stopping short of
canonical project identity. This keeps normalization in the Project Model.

### Prefer Qualitative Confidence

The corpus justifies an explainable assessment of extraction or
interpretation quality, but it does not justify numeric probabilities or
automated scoring.

## Canonical Domain Model Compliance

- Canonical concepts added: **NONE**
- Canonical concepts removed: **NONE**
- Canonical concepts modified: **NONE**
- Canonical definitions modified: **NONE**

Assertion, Canonical Concept Reference, Provenance, Epistemic Profile,
Assertion Relationship, and Assertion Group are Knowledge Model constructions,
not additions to the canonical vocabulary.

## Assumptions

- Source artefacts can be cited at a stable-enough location for review.
- Human review remains authoritative for validation and project decisions.
- Assertions may be extracted directly or recorded as explicitly marked,
  corpus-scoped interpretations.
- Stable identifiers and versions will be required eventually, but their
  representation is not needed to define the conceptual model.
- A source may be authoritative for one context and not another.

## Unresolved Questions

- What representation will provide stable assertion and source-location
  identity?
- Which validation transitions require authorization, and by whom?
- When should two differently worded assertions share an Assertion Group?
- How should changes to source artefacts invalidate or re-review assertions?
- Which source-authority descriptors are useful across organizations without
  imposing one governance method?
- How will the Project Model cite supporting, qualifying, and opposing
  assertions while preserving unresolved alternatives?

## Recommendations for Future Canonical Evolution

No Canonical Domain Model change is required by this iteration.

The previously recorded questions about `Measure`, `Data Entity`, and
controlled `System Element` kinds remain candidates for a future explicit
architectural review. The Knowledge Model does not create or redefine those
concepts.

## Next Iteration

Iteration 7 should define the minimal normalized Project Model. It should
consume Knowledge Assertions through the unchanged Canonical Domain Model,
represent unresolved alternatives without erasing evidence, and define the
forward and reverse traceability boundary between normalized information and
supporting, qualifying, or opposing assertions.
