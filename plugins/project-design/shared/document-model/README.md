# Shared Document Model

- Version: 0.1
- Status: Defined
- Scope: Common contract for documentary restitution

## Purpose

The Shared Document Model defines the discipline-neutral contract between a
business artefact and its documentary representations. It is the common
foundation for every `document-<discipline>` skill.

The model establishes responsibilities and invariants only. It does not define
a business methodology, a discipline-specific artefact structure, a document
template, an executable generator, a storage model, or a platform integration.

## Core Flow

```text
Business artefact
        |
        v
Document skill
        |
        v
Document
```

This flow is one-way. A document skill transforms an existing business
artefact into a documentary representation. It does not create or revise the
business artefact.

## Business Artefact

### Definition

A business artefact is the structured, versionable, format-neutral result of
a business skill. It represents project knowledge for a declared scope and
baseline independently of any document format or page layout.

Examples include:

- Project Canvas;
- Functional Design;
- Technical Design;
- Product Backlog.

### Responsibilities

The business artefact owns:

- the project meaning and discipline-specific structure;
- the distinction between established, provisional, and unresolved content;
- Decisions, contradictions, questions, and other knowledge states;
- relationships and useful traceability to normalized project information,
  extracted knowledge, and sources;
- the business validation state and readiness for downstream use.

It does not own typography, branding, pagination, office-file behavior, or any
other presentation concern.

### Producer and Lifecycle

The corresponding business skill produces and revises the artefact. For
example, `project-framing` produces the Project Canvas. A document skill is
never its producer or owner.

An artefact may be drafted, reviewed, validated, revised from new or corrected
evidence, or superseded by a later baseline. Every material revision remains
under the business skill's rules and authority. Formatting a document,
approving its appearance, or converting it to another format does not change
the artefact lifecycle or silently validate its business content.

When stakeholders amend or approve information through a document review,
that feedback must return through the applicable evidence and business-skill
workflow before it becomes a revised business artefact. The document skill
must not apply the business change itself.

## Document

### Definition

A document is a human-facing representation of one business artefact for
reading, distribution, validation, and sharing.

A document may improve navigation and presentation, but it does not become
the business source of truth. The business artefact remains authoritative for
its meaning, structure, status, Decisions, contradictions, questions, and
traceability.

### Documentary Lifecycle

A document is generated from an identified artefact baseline. It may be
rendered, inspected, distributed, reviewed, or regenerated in another format.
A changed artefact requires a newly generated or explicitly revised document;
documentary edits must never become an untracked substitute for an artefact
revision.

Corrections limited to layout, styling, navigation, or faithful formatting
remain documentary changes. Any correction that changes business meaning is a
business-content issue and must be returned to the producing business skill.

## Documentary Generation

A document skill may:

- map artefact elements to document locations;
- apply a readable document structure without changing the business
  structure;
- apply presentation rules or a compatible template;
- produce the requested supported format;
- verify content preservation and the native result.

A document skill must never:

- modify, complete, reinterpret, approve, or reject business content;
- create new project knowledge;
- resolve a contradiction or an Open Question;
- make or alter a Decision;
- conceal uncertainty, status, authority, or non-readiness;
- repair an invalid artefact through documentary editing.

Reordering, summarizing, deduplicating, or rewriting is permitted only when it
preserves meaning, authority, qualification, structure, and traceability.

## Document Formats

A document format is a delivery support, never a semantic layer. Examples
include:

- Markdown;
- Microsoft Word;
- Google Docs;
- Google Sheets;
- Microsoft Excel;
- PDF.

Markdown is the native format of the plugin. Each document skill declares the
additional formats it actually supports; a format listed here is not by
itself an implemented capability.

Changing format must not change business content. External formats may require
a compatible user-supplied template and native platform tooling. A document
skill must not claim an external format unless the actual native result was
created and verified. If the requested format is unavailable, it must state
the limitation and may offer a validated Markdown representation.

## Templates

A template is a presentation constraint applied to a document. It may change:

- visual presentation and styles;
- headers and footers;
- logos and colors;
- pagination;
- tables of contents;
- annex presentation.

A template must never change:

- business meaning or discipline-specific structure;
- Decisions or their authority;
- contradictions or unresolved questions;
- knowledge or normalization statuses;
- lifecycle perspectives;
- traceability.

Blank fields are presentation slots, not permission to invent content. A
template is compatible only when it can represent every material artefact
element and qualification. If it cannot, the document skill must reject it,
request an authorized adaptation, or use a compatible default structure; it
must not omit or distort business content to fit the template.

## Traceability and Content Preservation

Every generated document must preserve the useful traceability carried by its
business artefact, including:

- Decisions and their known authority;
- questions and their classification;
- contradictions and opposing positions;
- material statuses and lifecycle perspectives;
- references needed for review or audit;
- readiness qualifications and explicit gaps.

Before generation, the document skill creates a content-preservation mapping
between material artefact elements and document locations. After generation,
it compares the result with that mapping. Every material element must appear
once or through an explicit cross-reference.

Traceability must survive format conversion. A visual simplification, template
limitation, cell layout, pagination rule, or export constraint never justifies
dropping a reference or qualification.

## Common Contract for Document Skills

Every `document-<discipline>` skill:

- consumes one validated business artefact governed by its corresponding
  business skill;
- produces one document representing that artefact;
- declares its supported formats and format-specific verification;
- applies only documentary structure, presentation, compatible templates,
  format generation, and document-level quality control;
- preserves all material meaning, status, Decisions, contradictions,
  questions, readiness, and traceability;
- reports business-content defects to the corresponding business skill;
- never produces a new business artefact;
- never replaces the business skill;
- never becomes the owner or source of project knowledge;
- remains independently callable without global orchestration.

Discipline-specific document skills may add stricter structure, formatting,
template-compatibility, and verification rules. They may not weaken or
redefine this common contract.

## Dependency Boundary

The dependency direction is:

```text
Shared Document Model
        ^
        |
Document skills
```

This model may use the shared terminology, project-model, asset, and quality
contracts. It does not depend on a particular business discipline, artefact,
or document skill. Document skills reference this model and their applicable
business-artefact contract. This one-way dependency prevents competing models
and circular documentary architecture.

## Related Shared Contracts

- [Minimal Normalized Project Model](../project-model/README.md)
- [Shared quality rules](../quality-rules/README.md)
- [Shared assets](../assets/README.md)
- [Shared terminology](../terminology/README.md)
