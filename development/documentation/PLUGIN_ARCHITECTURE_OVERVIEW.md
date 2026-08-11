# Plugin Architecture Overview v1.0

- Status: Official architecture overview
- Review iteration: 8.6
- Date: 2026-08-05
- Scope: `project-design` version 0.1.0 unreleased architecture

## Purpose

This document is the entry point for understanding the complete
`project-design` plugin architecture. It consolidates the current contracts
without replacing the normative shared models or skill instructions.

The repository remains authoritative in this order:

1. accepted architecture decisions and stable shared models;
2. implemented `SKILL.md` contracts and their runtime references;
3. the current specification and plan;
4. this consolidated overview;
5. historical reports and roadmap notes.

## Executive Summary

`project-design` is a methodology-first and Markdown-first plugin. It
separates evidence, normalized project understanding, discipline-specific
business artefacts, and human-facing documents.

The architecture has four stable shared foundations:

- the Canonical Domain Model defines shared meaning;
- the Knowledge Model preserves extracted evidence and epistemic state;
- the Project Model represents normalized project understanding;
- the Shared Document Model governs faithful documentary restitution.

Nine skills are installed. Two have implemented methodologies:

- `project-framing` produces the Project Canvas business artefact;
- `document-project-canvas` produces its documentary representation.

The other six specialized skills are explicit placeholders. A placeholder stabilizes
the architecture and discovery contract but provides no operational
methodology.

Every invocation also follows one shared interaction and workspace contract:
give a concise launch brief before execution, then group durable Markdown
outputs beneath `_project-design/` at the target project root.

## Architectural Layers

| Layer | Responsibility | Owns | Must not own |
| --- | --- | --- | --- |
| Source layer | Preserve received project material | Original source content and context | Plugin interpretation or normalized truth |
| Semantic contract | Define shared project vocabulary | Canonical meanings and relationships | Project instances or methodology |
| Evidence layer | Preserve extracted statements and epistemic state | Assertions, provenance, uncertainty, validation, assertion relationships | Normalized project truth |
| Normalization layer | Represent coherent current project understanding | Project View, Elements, Relationships, statuses, perspectives, Knowledge Basis | Source evidence or skill methodology |
| Business-skill layer | Apply one design methodology | One discipline-specific business artefact | Final-document formats or presentation logic |
| Documentary layer | Represent one validated business artefact | Document structure, presentation, supported format, document verification | Business knowledge or Decisions |
| Orchestration layer | Select and coordinate specialized skills | Future routing, artefact transmission, cross-step consistency | Specialized methodology, business content, or documents |
| Integration layer | Adapt stable boundaries to optional platforms | Platform-specific mapping and packaging | Core methodology or shared-model semantics |

## Global View

The simplified information-processing flow is:

```text
Source documents
        |
        v
Knowledge Model
        |
        v
Project Model
        |
        v
Business skills
        |
        v
Business artefacts
        |
        v
Document skills when requested
        |
        v
Documents
```

A linear reading shorthand covers the complete design vocabulary:

```text
Source documents
        -> Knowledge Model
        -> Project Model
        -> Project Framing
        -> Project Canvas
        -> Functional Design
        -> Technical Design
        -> Product Backlog
        -> Documents
```

This shorthand is a documentation index, not a mandatory execution order.

The precise design flow is not strictly linear. Functional and technical
design are complementary and may run in parallel when their inputs permit:

```text
Source documents
        |
        v
Knowledge Model -> Project Model -> project-framing -> Project Canvas
                                                     |       |       |
                                                     |       |       +-> document-project-canvas
                                                     |       |             -> Project Canvas document
                                                     |       |
                                                     |       +-> technical-design
                                                     |             -> Technical Design
                                                     |                    -> document-technical-design
                                                     |
                                                     +-> functional-design
                                                           -> Functional Design
                                                                  -> document-functional-design

Project Canvas + designed and validated functional and/or technical Scope
        |
        v
product-backlog -> Product Backlog -> document-product-backlog
```

Technical design may consume validated functional Requirements when they are
available. Neither technical design nor functional design silently rewrites
the Project Canvas or the other discipline's artefact.

## Model View

The Canonical Domain Model and Shared Document Model are contracts, not extra
runtime processing stages:

```text
Canonical Domain Model
        | defines vocabulary
        +---------------------> Knowledge Model
        +---------------------> Project Model
        +---------------------> Skills

Source documents -> Knowledge Model -> Project Model -> Business skills
                                              |
                                              +-> business artefacts

Project Model + shared quality/assets/terminology
        |
        v
Shared Document Model
        |
        v
Document skills -> documents
```

No shared model depends on a skill. No skill may redefine a shared model.

## Shared Model Contracts

### Canonical Domain Model

- **Role:** shared semantic vocabulary of 22 project concepts.
- **Status:** defined conceptually, version 0.1.
- **Architectural owner:** shared architecture governance.
- **Producer:** architecture work derived from the permanent corpus; no
  runtime producer.
- **Consumers:** Knowledge Model, Project Model, business skills, document
  skills through terminology and artefact semantics.
- **Inputs:** recurring cross-skill concepts evidenced by the four permanent
  fixtures.
- **Outputs:** canonical definitions, aliases, relationships, and explicit
  exclusions.
- **Direct dependencies:** corpus evidence only; it is not dependent on
  another runtime model.
- **Limits:** no project data, instances, evidence state, schemas,
  serialization, methodology, or presentation.

### Knowledge Model

- **Role:** preserve what sources say before normalization.
- **Status:** defined conceptually, version 0.1.
- **Architectural owner:** shared architecture governance.
- **Producer:** the evidence-extraction and review process. No standalone
  executable producer is implemented. `project-framing` can prepare a working
  knowledge basis from raw sources when necessary.
- **Consumers:** Project Model normalization and implemented skills that need
  evidence qualification or source traceability.
- **Inputs:** source artefacts and Canonical Domain Model semantics.
- **Outputs:** Assertions, Canonical Concept References, Provenance,
  Epistemic Profiles, Assertion Relationships, and Assertion Groups.
- **Direct dependencies:** source documents and Canonical Domain Model.
- **Limits:** does not establish normalized truth, resolve conflict, create
  Project Model instances, or generate artefacts.

### Project Model

- **Role:** represent the coherent current normalized understanding of one
  project.
- **Status:** defined conceptually, version 0.1.
- **Architectural owner:** shared architecture governance.
- **Producer:** the normalization and review process. No standalone
  executable producer is implemented. `project-framing` can prepare a working
  Project View from available knowledge when no view is supplied.
- **Consumers:** all business skills, future orchestration, optional adapters,
  and the Shared Document Model indirectly through business artefacts.
- **Inputs:** Knowledge Assertions or Groups and Canonical Domain Model
  semantics.
- **Outputs:** Project View, Project Elements, Project Relationships,
  Normalization Status, Lifecycle Perspective, and Knowledge Basis.
- **Direct dependencies:** Knowledge Model and Canonical Domain Model.
- **Limits:** does not replace sources, preserve every assertion, execute a
  methodology, generate an artefact, or define platform behavior.

### Shared Document Model

- **Role:** discipline-neutral contract between one business artefact and its
  documentary representations.
- **Status:** defined, version 0.1.
- **Architectural owner:** shared architecture governance.
- **Producer:** architecture governance; it has no runtime data producer.
- **Consumers:** all four `document-<discipline>` skills.
- **Inputs:** business-artefact invariants plus shared project, quality,
  asset, and terminology contracts.
- **Outputs:** common rules for documents, generation, formats, templates,
  content preservation, and traceability.
- **Direct dependencies:** Project Model, shared quality rules, shared assets,
  and shared terminology.
- **Limits:** does not define a discipline methodology, artefact structure,
  template, generator, storage model, or platform integration.

## Skill View

```text
project-design (stateful guided entry implemented; complete orchestration future)
        |
        +-> project-framing -> Project Canvas
        |        +-> document-project-canvas -> Project Canvas document
        |
        +-> functional-design -> Functional Design
        |        +-> document-functional-design -> Functional specifications
        |
        +-> technical-design -> Technical Design
        |        +-> document-technical-design -> Technical specifications
        |
        +-> product-backlog -> Product Backlog
                 +-> document-product-backlog -> Product Backlog document
```

The lines express routing and producer-consumer relationships, not ownership
by `project-design`. Every specialized skill remains independently callable.

## Skill Contracts

### `project-design`

- **Role:** stateful guided plugin entry now; future global orchestration and cross-step
  coordination.
- **Status:** consent, workspace initialization, persistent phase enforcement,
  stage selection, delivery choice, framing and approval gates, and
  specialized-skill handoff implemented; complete orchestration not implemented.
- **Inputs:** project request, sources, existing artefacts, requested scope,
  selected skills, and constraints.
- **Outputs:** initialized project delivery workspace, non-business workflow
  state, and selected-stage handoff; future routing plan and coordinated
  collection of artefacts.
- **Artefact produced or consumed:** will transmit artefacts but owns none.
- **Document produced or consumed:** may route a document request but owns and
  produces no document.
- **Direct dependencies:** Project Model, shared quality rules, terminology,
  and optional Spec Kit boundary.
- **Consumers:** the user or external workflow receiving coordinated results.
- **Responsibilities:** present capabilities, obtain initialization consent,
  create the workspace safely, persist and enforce the current phase, select
  the stage, capture delivery choices, gate approval and delivery, and hand
  off; future work will order or parallelize steps, transmit artefacts,
  preserve consistency, and route founded feedback upstream.
- **Excluded:** specialized methodology, business content, document content,
  persistence, external execution, and unsupported invention.

### `project-framing`

- **Role:** first business-design step; clarify the expression of need.
- **Status:** implemented methodology version 0.2; manual validation pending.
- **Inputs:** Project View, Knowledge Assertions, structured project data, raw
  sources, user clarifications, and output constraints.
- **Outputs:** one structured, versionable, traceable Project Canvas.
- **Artefact produced or consumed:** produces and solely owns the Project
  Canvas business artefact.
- **Document produced or consumed:** none.
- **Direct dependencies:** Canonical Domain Model, Knowledge Model, Project
  Model, shared terminology, shared quality rules, and its runtime references.
- **Consumers:** `functional-design`, `technical-design`, `product-backlog`,
  and `document-project-canvas`.
- **Responsibilities:** frame context, objectives, stakeholders, users,
  Scope, known technical Constraints, Risks, Decisions, Questions, success
  criteria, readiness, and traceability.
- **Excluded:** detailed functional design, technical design, backlog
  decomposition, document formatting, export, and unsupported resolution.

### `functional-design`

- **Role:** future functional design of products or applications and expected
  behavior.
- **Status:** installed placeholder; methodology and artefact structure not
  implemented.
- **Inputs:** Project Canvas, Project View, needs, Actors, terminology,
  Constraints, Business Rules, existing Requirements, and workflows.
- **Outputs:** future Functional Design business artefact.
- **Artefact produced or consumed:** consumes the Project Canvas and shared
  project context; will solely own Functional Design.
- **Document produced or consumed:** none.
- **Direct dependencies:** Project Model, future shared schemas, shared
  quality rules, and terminology.
- **Consumers:** `technical-design` when functional Requirements are useful,
  `product-backlog`, and `document-functional-design`.
- **Responsibilities:** modules, features, users, Processes, journeys,
  Business Rules, functional data, exceptions, dependencies, Requirements,
  and supported acceptance concerns.
- **Excluded:** architecture, implementation tasks, document formatting,
  complete reframing, unsupported Requirements, and silent Canvas revision.

### `technical-design`

- **Role:** future complementary or parallel technical design.
- **Status:** installed placeholder; methodology and artefact structure not
  implemented.
- **Inputs:** Project Canvas, Project View, functional Requirements when
  available, existing systems, technical Constraints, standards,
  Integrations, quality needs, Risks, and Decisions.
- **Outputs:** future Technical Design business artefact.
- **Artefact produced or consumed:** consumes the Project Canvas and relevant
  validated design context; will solely own Technical Design.
- **Document produced or consumed:** none.
- **Direct dependencies:** Project Model, future shared schemas, and shared
  quality rules.
- **Consumers:** `product-backlog` and `document-technical-design`.
- **Responsibilities:** architecture, technologies, components,
  Integrations, APIs, flows, security, performance, hosting, operations,
  deployment, technical Decisions, Risks, and non-functional Requirements.
- **Excluded:** runtime implementation, unsupported technology selection,
  document formatting, complete reframing, and silent Canvas revision.

### `product-backlog`

- **Role:** future transformation of designed and validated Scope into a
  traceable Product Backlog.
- **Status:** installed placeholder; backlog methodology and semantics not
  implemented.
- **Inputs:** Project Canvas, functional or technical design, existing backlog
  material, and supplied prioritization or estimation constraints.
- **Outputs:** future Product Backlog business artefact.
- **Artefact produced or consumed:** consumes framing and applicable validated
  design artefacts; will solely own the Product Backlog.
- **Document produced or consumed:** none.
- **Direct dependencies:** Project Model, future shared schemas, and shared
  quality rules.
- **Consumers:** `document-product-backlog` and future delivery workflows.
- **Responsibilities:** traceable Epics, Features, User Stories, technical
  tasks, dependencies, increments, and methodological organization when the
  future contract supports them.
- **Excluded:** new Requirements or Decisions, unsupported backlog items,
  invented priority, value, effort, estimates, or document formatting.

### `document-project-canvas`

- **Role:** documentary restitution of a validated Project Canvas.
- **Status:** implemented methodology version 0.1; combined manual validation
  pending.
- **Inputs:** validated Project Canvas plus optional audience, language,
  metadata, compatible template, and delivery constraints.
- **Outputs:** verified native Markdown, Microsoft Word, or Google Docs
  Project Canvas document.
- **Artefact produced or consumed:** consumes the Project Canvas; produces no
  business artefact.
- **Document produced or consumed:** solely owns the Project Canvas document
  representation and its documentary quality.
- **Direct dependencies:** Shared Document Model, Project Canvas contract,
  assets, quality rules, terminology, and its document references.
- **Consumers:** stakeholders, reviewers, and downstream sharing workflows.
- **Responsibilities:** content-preservation mapping, document structure,
  compatible-template application, native format creation, and verification.
- **Excluded:** source analysis, framing, business-content correction,
  knowledge creation, contradiction resolution, and Decision changes.

### `document-functional-design`

- **Role:** future documentary restitution of Functional Design.
- **Status:** installed non-operational placeholder.
- **Inputs:** future validated Functional Design plus presentation and format
  constraints.
- **Outputs:** future Markdown, Word, or Google Docs functional specifications.
- **Artefact produced or consumed:** consumes Functional Design; produces no
  business artefact.
- **Document produced or consumed:** will solely own the Functional Design
  document representation.
- **Direct dependencies:** Shared Document Model, assets, quality rules, and
  terminology.
- **Consumers:** human readers and sharing workflows.
- **Responsibilities:** future faithful documentary representation only.
- **Excluded:** functional design, Requirements or Business Rule creation,
  document generation in the placeholder state, scripts, and integrations.

### `document-technical-design`

- **Role:** future documentary restitution of Technical Design.
- **Status:** installed non-operational placeholder.
- **Inputs:** future validated Technical Design plus presentation and format
  constraints.
- **Outputs:** future Markdown, Word, or Google Docs technical specifications.
- **Artefact produced or consumed:** consumes Technical Design; produces no
  business artefact.
- **Document produced or consumed:** will solely own the Technical Design
  document representation.
- **Direct dependencies:** Shared Document Model, assets, quality rules, and
  terminology.
- **Consumers:** human readers and sharing workflows.
- **Responsibilities:** future faithful documentary representation only.
- **Excluded:** technical design, architecture or technology creation,
  document generation in the placeholder state, scripts, and integrations.

### `document-product-backlog`

- **Role:** future documentary restitution of a Product Backlog.
- **Status:** installed non-operational placeholder.
- **Inputs:** future validated Product Backlog plus presentation and format
  constraints.
- **Outputs:** future Markdown, Google Sheets, Microsoft Excel, Microsoft
  Word, or Google Docs backlog document.
- **Artefact produced or consumed:** consumes Product Backlog; produces no
  business artefact.
- **Document produced or consumed:** will solely own the Product Backlog
  document representation.
- **Direct dependencies:** Shared Document Model, assets, quality rules, and
  terminology.
- **Consumers:** human readers and backlog-sharing workflows.
- **Responsibilities:** future faithful documentary representation only.
- **Excluded:** backlog creation or modification, prioritization, estimation,
  document generation in the placeholder state, scripts, and integrations.

## Artefact and Document Ownership

| Business artefact | Sole owner | Primary consumers | Corresponding document owner |
| --- | --- | --- | --- |
| Project Canvas | `project-framing` | `functional-design`, `technical-design`, `product-backlog`, `document-project-canvas` | `document-project-canvas` |
| Functional Design | `functional-design` | `technical-design` when relevant, `product-backlog`, `document-functional-design` | `document-functional-design` |
| Technical Design | `technical-design` | `product-backlog`, `document-technical-design` | `document-technical-design` |
| Product Backlog | `product-backlog` | delivery workflows, `document-product-backlog` | `document-product-backlog` |

A business skill owns business meaning. A document skill owns only the
representation and documentary verification. Global orchestration owns
neither.

## End-to-End Flow Matrix

| Step | Inputs | Outputs | Next consumer |
| --- | --- | --- | --- |
| Evidence intake | Source artefacts and user clarifications | Addressable source corpus | Knowledge preparation |
| Knowledge preparation | Source corpus and canonical vocabulary | Assertions, provenance, epistemic state, relationships | Project normalization |
| Project normalization | Knowledge Model and canonical vocabulary | Project View and Knowledge Basis | Applicable business skills |
| Project framing | Project View, knowledge, or sources | Project Canvas | Functional design, technical design, backlog preparation when sufficiently designed, or Canvas documentation |
| Canvas documentation | Validated Project Canvas | Project Canvas document | Human review and sharing |
| Functional design | Project Canvas and relevant Project View | Functional Design | Technical design when useful, backlog preparation, or functional documentation |
| Functional documentation | Validated Functional Design | Functional specifications document | Human review and sharing |
| Technical design | Project Canvas, relevant Project View, and functional Requirements when available | Technical Design | Backlog preparation or technical documentation |
| Technical documentation | Validated Technical Design | Technical specifications document | Human review and sharing |
| Backlog preparation | Project Canvas and applicable validated functional or technical design | Product Backlog | Backlog documentation and delivery workflows |
| Backlog documentation | Validated Product Backlog | Backlog document | Human review, sharing, and external tools |

## Dependency Rules

### Direct Dependencies

- Knowledge Model depends on source documents and Canonical Domain Model.
- Project Model depends on Knowledge Model and Canonical Domain Model.
- Business skills depend on the Project Model and applicable shared quality,
  terminology, schema, and discipline references.
- Document skills depend on the Shared Document Model and their corresponding
  business-artefact contract.
- Optional integrations depend on stable core boundaries.

### Indirect Dependencies

- Every generated material statement indirectly depends on source evidence
  through Project Model and Knowledge Model traceability.
- Document skills indirectly depend on the project evidence chain carried by
  their input artefacts.
- Placeholder skills indirectly depend on canonical semantics through the
  Project Model even when they do not link the Canonical Domain Model
  directly.

### Forbidden Dependencies

- A shared model must not depend on a skill.
- A business skill must not depend on a document format, template, or
  document skill for its business artefact.
- A document skill must not extract or normalize raw project knowledge.
- An installable bundle file must not depend on `development/`.
- Core skills must not depend on Spec Kit or another platform integration.
- An artefact or document must not become evidence without re-entering a new
  source-to-knowledge-to-project cycle.

### Cycle Check

The bundle dependency graph is acyclic. Review of all bundle-local Markdown
links found 28 nodes and 73 direct local dependencies with no cycle.

The later acceptance of a generated artefact is not a dependency cycle. It is
a new evidence lifecycle: the accepted artefact becomes a new source, then
passes through Knowledge Model and Project Model review.

## Conventions

- `<discipline>` names the business skill and business artefact.
- `document-<discipline>` names the corresponding document skill.
- Markdown is the native document format.
- External formats are capabilities only when a skill explicitly implements
  and verifies them.
- English is the canonical internal language.
- Localized terminology changes presentation labels, never canonical meaning.
- `Established`, `Provisional`, and `Unresolved` remain distinct.
- `Existing`, `Target`, and `Transition` remain distinct.
- Assumption, Option, Decision, Open Question, Risk, and Issue must not be
  conflated.
- Every specialized skill remains callable without global orchestration.
- Runtime references belong inside the installable skill directory.
- Development fixtures, tests, reports, and draft examples never become
  runtime dependencies.
- Before execution, identify the skill or ordered skills, available and
  missing inputs, generated deliverables, and required or optional models or
  templates.
- Store durable business-artefact Markdown at `_project-design/<artefact>.md`
  and documentary Markdown at `_project-design/documents/<artefact>.md` in the
  target project.
- Treat `_project-design/` as a delivery workspace, not as a new semantic
  model, evidence source, orchestration layer, or ownership boundary.
- When the user explicitly selects centralized source intake, use the separate
  root-level `_sources/` workspace for approved local copies and remote source
  links. Keep it Git-ignored by default and treat originals as authoritative.
- Do not create output files for placeholder skills or silently overwrite an
  unrelated existing deliverable.

## Roadmap Readiness

The four shared architectural foundations are complete at their current
conceptual scope. No additional shared foundation is required before
`functional-design` methodology design begins.

The next logical methodology iteration is `functional-design`. Its detailed
prompt must define the Functional Design artefact, readiness rules, minimum
inputs, functional boundaries, traceability, and fixture validation without
changing the stable models.

The combined manual validation of `project-framing` and
`document-project-canvas` remains an outstanding quality gate. It does not
reveal a missing architectural foundation, but its results must remain visible
when assessing end-to-end maturity.

The minimum designed input required by `product-backlog` and the exact
coordination between functional and technical design remain deliberately
methodology-level decisions for their future iterations. They are not reasons
to add another shared model now.
