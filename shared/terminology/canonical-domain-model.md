# Canonical Domain Model

- Version: 0.1
- Status: Defined conceptually
- Implementation: Not applicable
- Derived from: The four permanent reference fixtures

## Purpose

The Canonical Domain Model defines the minimum shared business vocabulary used
by the Knowledge Model, the Project Model, and every future skill.

It is not part of the information-processing pipeline:

```text
Documents -> Knowledge Model -> Project Model -> Skills -> Generated artefacts

Canonical Domain Model:
  - defines vocabulary for the Knowledge Model
  - defines vocabulary for the Project Model
  - defines vocabulary for every skill
```

The model defines concepts and meaningful relationships. It does not contain
project data, extracted statements, normalized instances, generated content,
schemas, fields, identifiers, cardinalities, serialization, or methodology.

## Selection Rule

A concept is retained only when it is:

- evidenced by the permanent corpus;
- useful across more than one future skill or required at a shared-model
  boundary;
- understandable without a specific platform, methodology, or technology;
- meaningfully distinct from the other retained concepts.

Concepts are merged when a distinction would serve only one skill or require
implementation detail that the corpus does not yet justify.

## Conceptual Levels

The same domain concept may appear at different information levels without
changing its canonical meaning:

```text
Canonical concept
    Requirement

Extracted knowledge
    "The charter states that every request requires manager approval."

Normalized project information
    Approval requirement with unresolved conflicting evidence

Generated artefact
    A framing, functional, technical, backlog, or document statement
```

The Canonical Domain Model defines `Requirement`. The Knowledge Model defines
how the extracted statement is classified and traced. The Project Model
defines how a project-specific requirement is normalized. A skill defines how
it is used in a deliverable.

## High-Level Organization

### Project Foundation

- Project
- Organization
- Stakeholder
- Actor
- Objective
- Scope

### Domain and Behavior

- Domain Term
- Need
- Capability
- Process
- Requirement
- Business Rule

### Governance and Uncertainty

- Constraint
- Assumption
- Option
- Decision
- Open Question
- Risk
- Issue

### Solution and Change

- System Element
- Integration
- Transition

## Relationship Overview

```text
Organization hosts or sponsors Project
Project has Stakeholders, Objectives, Scope, Risks, Issues, and Transitions
Stakeholders express Needs and make Decisions
Actors participate in Processes and interact with System Elements
Objectives address Needs and guide Scope
Capabilities address Needs and are realized by Processes and System Elements
Requirements refine Needs, Capabilities, Objectives, and Constraints
Business Rules govern Processes, Capabilities, and Requirements
Options respond to Open Questions and are selected or rejected by Decisions
Assumptions influence project information and may create Risks
Integrations connect System Elements
Transitions change Processes and System Elements toward a target condition
Domain Terms define the vocabulary used by every concept
```

These relationships express shared meaning only. Their detailed direction,
cardinality, lifecycle, and implementation remain outside this iteration.

## Retained Concepts

### Project

**Definition:** A bounded initiative undertaken to understand, design, change,
or deliver a software-supported outcome.

**Purpose:** Provide the common context that connects objectives, scope,
participants, decisions, risks, solution concerns, and generated artefacts.

**Aliases:** Initiative; engagement when referring to the consulting context.

**Relationships:** Situated within one or more Organizations; involves
Stakeholders and Actors; pursues Objectives; defines Scope; contains or is
affected by every other project-level concept.

**Corpus examples:**

- The Service Request Workspace initiative in
  `incomplete-project/context-note.md`.
- The Case Ledger modernization in
  `application-modernization/business/application-overview.md`.

### Organization

**Definition:** A business, institution, organizational unit, or external
party that provides project context, authority, resources, or affected users.

**Purpose:** Anchor ownership, governance, operating context, and boundaries
that cannot be attributed to an individual person or system.

**Aliases:** Enterprise; institution; organizational unit when used at a
smaller boundary.

**Relationships:** Hosts or sponsors Projects; contains or represents
Stakeholders and Actors; owns or uses System Elements; participates in
Integrations.

**Corpus examples:**

- Willow Brook Services in `incomplete-project/context-note.md`.
- Kitewood Learning Collective in `new-application/business-brief.md`.

### Stakeholder

**Definition:** A person, role, group, or organization that influences,
governs, supplies information to, or is materially affected by a Project.

**Purpose:** Represent interests, authority, accountability, and viewpoints
even when the stakeholder never interacts with the future system.

**Aliases:** Interested party. Sponsor, owner, manager, reviewer, and subject
matter expert are stakeholder roles rather than separate canonical concepts.

**Relationships:** Participates in a Project; expresses Needs; owns or
validates Objectives, Scope, Requirements, Options, and Decisions; may also be
an Actor.

**Corpus examples:**

- The service manager and unidentified governance representatives in
  `incomplete-project/context-note.md`.
- The people-development director and accessibility representative in
  `new-application/business-brief.md`.

### Actor

**Definition:** A person, role, group, or external system that participates in
a Process or interacts with a System Element.

**Purpose:** Describe observable participation and behavior independently from
project authority or interest.

**Aliases:** User; participant; external actor. A persona is a representation
of an Actor, not a separate canonical concept.

**Relationships:** May also be a Stakeholder; expresses Needs; performs or
participates in Processes; uses System Elements; is governed by Business
Rules and Requirements.

**Corpus examples:**

- Advisors, supervisors, and administrators in
  `application-modernization/business/application-overview.md`.
- Staff members, training coordinators, managers, and support analysts in
  `new-application/personas.md`.

### Objective

**Definition:** A desired result that gives the Project direction and explains
why change is valuable.

**Purpose:** Connect the project purpose to scope, needs, capabilities,
requirements, decisions, and later measures of success.

**Aliases:** Goal; intended outcome.

**Relationships:** Belongs to a Project; addresses Needs; guides Scope;
motivates Capabilities and Requirements; may be threatened by Risks or Issues.

**Corpus examples:**

- Reduce lost requests and improve workload understanding in
  `incomplete-project/context-note.md`.
- Make learning sessions easier to discover and reduce manual coordination in
  `new-application/business-brief.md`.

### Scope

**Definition:** The explicit boundary of what the Project includes, excludes,
or reserves for possible future consideration.

**Purpose:** Prevent objectives, needs, options, and future ideas from being
treated as approved commitments without a boundary decision.

**Aliases:** Project boundary; perimeter.

**Relationships:** Belongs to a Project; includes or excludes Capabilities,
Processes, Requirements, System Elements, Integrations, and Transitions; is
changed by Decisions and constrained by Constraints.

**Corpus examples:**

- Initial portal scope in `contradictory-project/project-charter.md`.
- Proposed MVP, explicit exclusions, and future ideas in
  `new-application/mvp-and-roadmap.md`.

### Domain Term

**Definition:** A word or phrase with project-specific meaning that must be
understood consistently.

**Purpose:** Preserve vocabulary, aliases, ambiguity, and agreed definitions
across sources, models, skills, and generated artefacts.

**Aliases:** Term; glossary entry; business term.

**Relationships:** Describes or names any canonical concept; may have aliases;
may remain ambiguous until a Decision or validated definition resolves it.

**Corpus examples:**

- `request`, `ticket`, and `case` in
  `incomplete-project/vocabulary-notes.md`.
- `closed`, `completed`, and `resolved` in the same fixture.

### Need

**Definition:** A problem, expectation, or desired improvement expressed from
the perspective of a Stakeholder or Actor.

**Purpose:** Preserve why a capability or requirement may be useful before
turning it into a normalized solution commitment.

**Aliases:** Stakeholder need; user need; business need.

**Relationships:** Expressed by a Stakeholder or Actor; supports an Objective;
may be addressed by Capabilities, Processes, Requirements, or Options.

**Corpus examples:**

- Coordinators need one place to see work in
  `incomplete-project/service-team-message.md`.
- Managers need one list of pending approvals in
  `new-application/stakeholder-interviews.md`.

### Capability

**Definition:** An ability the organization, process, or solution needs in
order to address a Need or Objective.

**Purpose:** Describe what must be possible without prematurely defining a
specific workflow, interface, or technical implementation.

**Aliases:** Ability; business capability; product capability. `Feature` may
be used informally but is not always equivalent.

**Relationships:** Addresses Needs and Objectives; belongs inside or outside
Scope; is realized by Processes and System Elements; is refined by
Requirements and governed by Business Rules.

**Corpus examples:**

- Request submission, assignment, search, workload summary, and notifications
  in `incomplete-project/discovery-workshop.md`.
- Session management and place-request handling in
  `new-application/functional-expectations.md`.

### Process

**Definition:** An ordered set of activities through which Actors and System
Elements produce or change a business result.

**Purpose:** Represent current or target behavior at a level shared by
framing, functional design, technical design, and backlog preparation.

**Aliases:** Workflow; business process. Journey may be used when the same
process is described from an Actor's perspective.

**Relationships:** Performed by Actors; realizes Capabilities; is governed by
Business Rules and Requirements; uses System Elements and Integrations; may be
changed by a Transition.

**Corpus examples:**

- Current request handling in
  `incomplete-project/discovery-workshop.md`.
- Place request, approval, withdrawal, and attendance handling in
  `new-application/functional-expectations.md`.

### Requirement

**Definition:** A necessary condition, behavior, or quality that the Project
or solution is expected to satisfy.

**Purpose:** Provide a shared expression of expected behavior or quality that
can be traced to needs, objectives, rules, constraints, and decisions.

**Aliases:** Functional requirement; non-functional requirement; quality
requirement are kinds of Requirement, not separate canonical concepts.

**Relationships:** Refines Needs, Objectives, and Capabilities; may derive from
Business Rules, Constraints, Decisions, Risks, or Issues; may apply to
Processes, System Elements, Integrations, or Transitions.

**Corpus examples:**

- Availability, accessibility, performance, security, and recovery
  expectations in `new-application/non-functional-requirements.md`.
- Searchable history and continuity expectations in
  `application-modernization/migration/constraints.md`.

### Business Rule

**Definition:** A statement that governs or constrains business behavior,
eligibility, calculation, authorization, or state change.

**Purpose:** Keep domain policy distinct from desired capabilities, technical
constraints, and implementation choices.

**Aliases:** Domain rule; service rule; policy rule.

**Relationships:** Governs Actors, Processes, Capabilities, and Requirements;
may be sourced from a Decision or policy; may conflict with another rule at
the Knowledge Model level.

**Corpus examples:**

- Approval, eligibility, response, and retention rules in
  `contradictory-project/service-policy-extract.md`.
- Session publication, approval, withdrawal, and attendance rules in
  `new-application/service-rules.md`.

### Constraint

**Definition:** A limitation or boundary condition that restricts acceptable
scope, options, requirements, design, delivery, or operation.

**Purpose:** Make non-negotiable or externally imposed limits visible without
confusing them with objectives or chosen solutions.

**Aliases:** Limitation; boundary condition.

**Relationships:** Constrains Projects, Scope, Options, Requirements, System
Elements, Integrations, and Transitions; may create Risks or influence
Decisions.

**Corpus examples:**

- Maximum two-hour interruption in
  `application-modernization/migration/constraints.md`.
- Organizational identity, accessibility, and language constraints in
  `new-application/non-functional-requirements.md`.

### Assumption

**Definition:** A premise treated as provisionally true for reasoning or
planning but not yet validated.

**Purpose:** Permit progress while preventing uncertain information from being
represented as fact or decision.

**Aliases:** Hypothesis when used as an unvalidated project premise.

**Relationships:** May concern any concept; influences Options, Requirements,
Scope, and Transitions; should be linked to an Open Question or validation
need; may create a Risk if false.

**Corpus examples:**

- The expectation that department membership identifies an approving manager
  in `contradictory-project/technical-assumptions.md`.
- Beliefs about identity attributes in
  `new-application/integration-notes.md`.

### Option

**Definition:** A candidate course of action, interpretation, scope choice, or
solution considered before an authoritative Decision.

**Purpose:** Preserve alternatives without presenting them as commitments.

**Aliases:** Proposal; alternative; candidate approach.

**Relationships:** Responds to an Open Question; is evaluated against
Objectives, Constraints, Risks, Issues, and Requirements; may be selected,
rejected, or deferred by a Decision.

**Corpus examples:**

- Single cutover, phased rollout, and parallel operation across
  `contradictory-project/delivery-plan.md` and
  `contradictory-project/technical-assumptions.md`.
- Transformed history or read-only archive in
  `application-modernization/migration/constraints.md`.

### Decision

**Definition:** An authoritative choice that establishes, changes, confirms,
rejects, or defers a project direction.

**Purpose:** Separate approved direction from needs, assumptions, options, and
informal source statements.

**Aliases:** Resolution; approved choice.

**Relationships:** Resolves an Open Question; selects or rejects Options;
changes Scope, Requirements, Business Rules, Transitions, or System Elements;
is made or owned by a Stakeholder.

**Corpus examples:**

- Historical attachment-storage and local-administration choices in
  `application-modernization/governance/decision-history.md`.

### Open Question

**Definition:** An explicit unresolved need for information, clarification, or
an authoritative decision.

**Purpose:** Keep missing information and unresolved choices visible and
actionable.

**Aliases:** Decision request; clarification request; information need.

**Relationships:** May concern any concept; may test an Assumption; may expose
a Risk; may have Options; is resolved by validated information or a Decision.

**Corpus examples:**

- Missing ownership, delivery, funding, support, and scope information in
  `incomplete-project/discovery-workshop.md`.
- Undecided product ownership, retention, integrations, and service ownership
  in `new-application/open-decisions.md`.

### Risk

**Definition:** An uncertain event or condition that could affect an
Objective, Scope, delivery, operation, or solution.

**Purpose:** Represent potential impact separately from current problems and
confirmed constraints.

**Aliases:** Threat when only negative effects are considered.

**Relationships:** Threatens or affects Projects, Objectives, Scope,
Requirements, System Elements, Integrations, or Transitions; may arise from an
Assumption, Issue, Constraint, or Option; may influence a Decision.

**Corpus examples:**

- Duplicate case updates during parallel operation in
  `application-modernization/migration/constraints.md`.
- Unconfirmed identity and calendar capabilities in
  `new-application/integration-notes.md`.

### Issue

**Definition:** A current observed problem, deficiency, or adverse condition
requiring attention.

**Purpose:** Distinguish an existing problem from a possible future Risk.

**Aliases:** Problem; defect; current concern.

**Relationships:** Affects Projects, Processes, Requirements, System Elements,
Integrations, or Transitions; may motivate Needs, Requirements, Options, or
Decisions; may create Risks.

**Corpus examples:**

- Failed queues, duplicate reminders, and unusable attachments in
  `application-modernization/operations/support-observations.md`.
- Unsupported runtime, limited tests, and unowned jobs in
  `application-modernization/technical/system-inventory.md`.

### System Element

**Definition:** A bounded functional or technical part of the current or
target solution landscape.

**Purpose:** Provide one shared concept for solution structure without fixing
technical granularity before technical design.

**Aliases:** Application, system, module, component, service, job, and data
store are contextual kinds of System Element rather than separate canonical
concepts in version 0.1.

**Relationships:** Realizes Capabilities; supports Processes; is governed by
Requirements and Constraints; connects through Integrations; may contain
other System Elements; may be affected by Issues, Risks, Decisions, and
Transitions.

**Corpus examples:**

- Case Ledger, its scheduled jobs, database, and attachment store in
  `application-modernization/technical/system-inventory.md`.
- Organizational identity and messaging services in
  `new-application/integration-notes.md`.

### Integration

**Definition:** A managed interaction or exchange between System Elements or
organizational boundaries.

**Purpose:** Represent cross-boundary communication and dependency without
prematurely prescribing protocol or implementation.

**Aliases:** Interface; connection; external interface.

**Relationships:** Connects System Elements; supports Processes and
Capabilities; is governed by Requirements, Business Rules, and Constraints;
may have Risks, Issues, Assumptions, Options, and Decisions.

**Corpus examples:**

- Directory synchronization, document archive transfer, finance data, and
  reporting exports in
  `application-modernization/technical/interface-notes.md`.
- Identity, messaging, calendar, and people-data expectations in
  `new-application/integration-notes.md`.

### Transition

**Definition:** A coordinated change from a current condition toward a target
condition.

**Purpose:** Represent migration, rollout, cutover, adoption, and continuity
concerns independently from current and target solution structure.

**Aliases:** Migration, rollout, cutover, and adoption are forms or aspects of
a Transition rather than separate canonical concepts.

**Relationships:** Changes Processes, Requirements, Business Rules, System
Elements, Integrations, and Scope; is constrained by Constraints; has Options,
Decisions, Risks, Issues, and affected Actors.

**Corpus examples:**

- Data migration, parallel operation, rollback, training, and archive options
  in `application-modernization/migration/constraints.md`.
- Pilot, phased rollout, single cutover, and mailbox transition proposals in
  the `contradictory-project` fixture.

## Main Design Decisions

### Keep Stakeholder and Actor Separate

A sponsor or security reviewer may influence the Project without interacting
with the solution. An advisor or external system may act in a Process without
having project authority. Merging these concepts would lose a distinction used
by project-framing, functional-design, technical-design, and product-backlog.

### Keep Need and Requirement Separate

A Need explains a stakeholder problem or expectation. A Requirement expresses
a condition the project or solution is expected to satisfy. This prevents
informal requests from becoming approved requirements during extraction.

### Keep Capability and System Element Separate

Capability describes what must be possible. System Element describes a
functional or technical part that may realize it. This preserves
technology-independent reasoning before technical design.

### Use One Requirement Concept

Functional, non-functional, quality, transition, and integration requirements
share the same canonical responsibility. Their detailed kinds belong to later
models and methodologies.

### Merge Application, Module, Component, and Service

The corpus uses several levels of solution structure, but no stable shared
rule yet distinguishes them. `System Element` preserves the distinction as
contextual kind or granularity without creating a premature hierarchy.

### Keep Risk and Issue Separate

An Issue already exists; a Risk is uncertain. The modernization fixture
contains both, and treating current production problems as future uncertainty
would weaken planning and traceability.

### Retain Transition as a Shared Concept

Migration and rollout affect framing, functional continuity, technical design,
backlog planning, and documents. Treating transition only as technical work
would not cover the modernization corpus.

### Treat Persona as a Representation

A persona describes a representative Actor. It does not introduce a new kind
of project participant and therefore remains an artefact-level representation,
not a canonical concept.

### Treat Proposal Carefully

`Option` is retained when a candidate project choice must be compared and
decided. Whether a source statement is classified epistemically as a proposal
belongs to the Knowledge Model.

## Excluded Concepts

### Knowledge Model Responsibilities

The following are excluded because they describe evidence or epistemic state,
not the project domain:

- Source Artefact;
- Source Location;
- Knowledge Statement or Claim;
- Fact;
- Interpretation;
- Confidence or Reliability Assessment;
- Validation State;
- Evidence Link;
- Contradiction, Support, Equivalence, and Supersession relationships.

They must be defined by the Knowledge Model using the canonical vocabulary
where appropriate.

### Project Model Responsibilities

The following are excluded because they concern normalized instances,
lifecycle, or storage rather than canonical meaning:

- canonical instance identifiers;
- version and change history;
- resolution status;
- current-state and target-state markers;
- relationship cardinalities;
- model validation rules.

### Skill-Specific Concepts

The following remain outside version 0.1 because they primarily belong to one
methodology or generated artefact:

- Backlog Item;
- User Story;
- Acceptance Criterion;
- Priority;
- Effort Estimate;
- Architecture Decision Record;
- Document Section;
- Document Template;
- Export Format.

Future iterations may promote one of these concepts only if several skills or
shared-model boundaries demonstrate the need.

### Deliberately Merged or Deferred Concepts

- Role is represented through the context in which a Stakeholder or Actor
  participates.
- Persona remains a representation of an Actor.
- Feature remains a possible expression of Capability.
- Application, System, Module, Component, Service, Job, and Data Store are
  represented by System Element.
- Interface is represented by Integration.
- Workflow and Journey are represented by Process when they share the same
  behavioral meaning.
- Metric, Indicator, and Target remain associated with Objective or
  Requirement until the corpus justifies a separate shared concept.
- Dependency remains a relationship between concepts rather than a standalone
  concept.
- Data Entity remains deferred until the shared models demonstrate a
  cross-skill responsibility that cannot be represented through Domain Term,
  Requirement, Process, or System Element.

## Fixture Validation Summary

| Fixture | Canonical concerns exercised |
| --- | --- |
| `incomplete-project` | Project, stakeholders, actors, objectives, needs, capabilities, process, assumptions, questions, terms, integrations, and missing scope |
| `contradictory-project` | Scope, rules, requirements, assumptions, options, decisions, constraints, integrations, and transition alternatives |
| `application-modernization` | Existing processes and system elements, issues, risks, requirements, integrations, historical decisions, and transition |
| `new-application` | Objectives, stakeholders, actors, needs, capabilities, scope, rules, requirements, constraints, integrations, options, and open decisions |

All 22 retained concepts are supported by the corpus and serve multiple future
skills or a shared-model boundary.

## Assumptions

- The model describes software-project design rather than every concept in
  general project management.
- English canonical names provide stable labels at the conceptual level;
  localization is a presentation and terminology concern.
- Detailed kinds and specializations should be introduced only when the
  Knowledge Model, Project Model, or multiple skills require them.
- Relationships may carry project-specific qualification later without
  changing the canonical definitions.

## Open Questions

- Should Objective eventually have a separate Measure concept?
- Should System Element kinds become canonical after technical-design is
  implemented?
- Does Data Entity become shared once functional and technical models exist?
- Which relationships need explicit direction or lifecycle semantics?
- Which concepts require controlled kinds rather than free project
  terminology?

These questions do not block version 0.1. They must be answered through future
model and skill implementation evidence.

## Next Iteration

Implement the minimal Knowledge Model using this vocabulary.

The Knowledge Model should define source references, extracted statements,
epistemic classification, confidence or reliability, validation state,
uncertainty, and evidence relationships. It must be tested against all four
permanent fixtures without redefining the canonical domain concepts.
