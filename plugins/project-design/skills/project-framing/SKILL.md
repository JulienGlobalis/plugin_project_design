---
name: project-framing
description: Transform project briefs, discovery notes, source documents, or an existing Project View into a concise, traceable project-framing document covering context, objectives, scope, stakeholders, existing, target and transition concerns, constraints, assumptions, dependencies, decisions, risks, issues, unresolved questions, and next steps. Use for application or software project discovery, initiation, alignment, clarification, or reframing before functional design, technical design, or backlog preparation.
---

# Project Framing

## Status

IMPLEMENTED - methodology version 0.1.

## Purpose

Establish a shared, evidence-aware understanding of an application or
software project before detailed functional design, technical design, or
backlog decomposition.

Produce a concise framing document that a consultant can review and share
with stakeholders after appropriate validation.

## Inputs

Accept any useful combination of:

- a normalized Project View;
- Knowledge Assertions or structured project information;
- briefs, workshop notes, messages, policies, specifications, inventories,
  decision logs, or other source artefacts;
- user clarifications supplied during the interaction;
- requested audience, language, framing purpose, and output constraints.

Do not require the user to prepare the shared models manually.

## Required References

Apply these contracts without redefining them:

- [Project Model](../../shared/project-model/README.md)
- [Knowledge Model](../../shared/knowledge-model/README.md)
- [Canonical Domain Model](../../shared/terminology/canonical-domain-model.md)
- [Shared terminology](../../shared/terminology/README.md)
- [Quality rules](../../shared/quality-rules/README.md)

Read the
[framing structure reference](references/framing-structure.md) before
composing the document.

When French output is requested, also read the
[French canonical terminology](../../shared/terminology/canonical-terms.fr.md).

## Workflow

### 1. Establish the Request Context

Identify:

- the project or initiative being framed;
- the available inputs;
- the intended audience and immediate use when supplied;
- the requested output language;
- whether an existing Project View is available.

Infer language and audience from the request when clear. Do not ask the user
to confirm information that is already evident.

Use English when no language is requested and no interaction language clearly
indicates another choice. When a requested language resource is missing,
state the limitation and obtain an explicit fallback choice; never silently
use an unrelated localized language.

### 2. Prepare the Working Project View

When a Project View is supplied:

- use it as the normalized input;
- preserve its Project Elements, Relationships, Normalization Status,
  Lifecycle Perspective, and Knowledge Basis;
- use linked knowledge or sources to explain qualifications and conflicts;
- report a material discrepancy with new sources instead of silently
  overriding the supplied view.

When only raw or partially structured sources are supplied:

- organize the available information according to the Knowledge Model and
  Project Model contracts;
- distinguish source assertions from normalized project meaning;
- consolidate compatible information without copying every source statement;
- assign `Established`, `Provisional`, or `Unresolved` only as justified;
- distinguish `Existing`, `Target`, and `Transition` when state changes
  meaning;
- retain supporting, qualifying, and opposing source paths;
- do not create a framing-specific competing truth or a new shared model.

Treat this preparation as use of the shared contracts, not as a separate
deliverable or methodology layer.

### 3. Select Framing-Relevant Information

Select information needed to explain:

- project context and current situation;
- problem, opportunity, Needs, Objectives, and expected outcomes;
- known Scope and explicit exclusions;
- Stakeholders, Actors, users, authority, and ownership;
- target vision and material Capabilities;
- Transition considerations;
- Constraints, Assumptions, and dependencies;
- Decisions and unresolved Options;
- Risks and confirmed Issues;
- Open Questions and next clarification activities.

Include framing-relevant Requirements and Business Rules only when they
materially affect objectives, boundaries, feasibility, governance, risk, or
the next phase. Hand detailed behavior to `functional-design` and detailed
quality or solution concerns to `technical-design`.

Represent dependencies as relationships between project elements. Do not
introduce a new canonical Dependency concept.

### 4. Assess Information Quality

For every material statement:

- preserve its normalization status;
- preserve its lifecycle perspective when relevant;
- retain a traceable source or Knowledge Basis;
- distinguish Stakeholder from Actor;
- distinguish Need from Requirement;
- distinguish Risk from confirmed Issue;
- distinguish Assumption from established information;
- distinguish Option from Decision.

Do not:

- infer approval from confident wording;
- prefer a source only because it is newer or more detailed;
- merge conflicting values into a false compromise;
- turn a proposal or future idea into Scope;
- turn missing information into a negative fact;
- invent owners, dates, priorities, volumes, constraints, or requirements.

When an authorized Decision resolves a conflict, present the normalized
position and retain the material opposing evidence in the traceability basis.
Otherwise keep the matter unresolved.

### 5. Decide Whether to Ask Before Drafting

Produce a useful first framing without a preliminary questionnaire whenever
possible.

Ask before drafting only when a small amount of information is necessary to
identify the project, understand its basic purpose, select the requested
deliverable, or avoid a materially misleading frame.

When questions are necessary:

- ask at most three high-value questions at a time;
- explain briefly why each answer matters;
- never repeat a question already answered by the inputs;
- let the user decline or defer an answer;
- continue with an explicitly incomplete framing when the user chooses.

Do not delay the first draft for details that can be recorded as unresolved.

### 6. Compose the Framing

Use the structure selection rules in
[the framing structure reference](references/framing-structure.md).

Keep the default document concise:

- lead with project purpose, context, and the most consequential boundaries;
- include only justified sections;
- merge closely related sections when that improves readability;
- use tables for comparison, status, ownership, or action registers;
- use prose for context, rationale, and target vision;
- avoid repeating the same information in summaries and registers.

Make status visible where misunderstanding would matter. Do not expose
internal canonical identifiers or model mechanics in normal client-facing
prose.

For French output:

- use the preferred French terminology as guidance;
- favor natural consulting language over literal model labels;
- preserve project-specific Domain Terms from the sources;
- adapt a preferred label in prose when necessary for naturalness without
  changing its meaning;
- keep English canonical references internal.

### 7. Classify Clarification Needs

Separate unresolved matters into:

- **required before framing approval**: prevents reliable agreement on
  purpose, material boundaries, authority, or a critical constraint;
- **required before the next design phase**: does not prevent review of the
  framing but blocks responsible functional, technical, or backlog work;
- **can be deferred**: useful later but not currently blocking.

Prioritize questions by decision impact, risk, and dependency. Identify an
owner or decision authority only when known. Recommend a concrete next action
without inventing dates or commitments.

### 8. Verify Before Delivery

Check the output against:

- the source material and Knowledge Basis;
- the shared quality rules;
- the
  [project-framing quality checklist](references/quality-checklist.md).

Confirm that:

- every material claim is supportable;
- opposing information remains visible;
- empty or unjustified sections are absent;
- known Scope, exclusions, stakeholders, and uncertainty are represented;
- Existing, Target, and Transition are not conflated;
- Risks and Issues are separate;
- questions are useful, non-duplicative, and proportionate;
- next steps are actionable;
- no detailed functional, technical, or backlog design was introduced.

## Output Contract

Produce one reviewable project-framing document in the requested language.

The document should normally contain a suitable selection of:

- executive framing;
- context and existing situation;
- problem or opportunity;
- Objectives and expected outcomes;
- Scope and explicit exclusions;
- Stakeholders, Actors, and users;
- target vision;
- Transition considerations;
- Constraints, Assumptions, and dependencies;
- Decisions and Options;
- Risks and confirmed Issues;
- unresolved questions;
- recommended next steps;
- concise evidence or source references.

Do not force this exact order or create empty headings. Preserve meaning over
template uniformity.

## Traceability

Keep each material framing statement traceable through:

```text
Framing statement
    -> Project Element or Relationship
    -> Knowledge Assertion or Assertion Group
    -> Source location
```

Use concise source references suitable for review. Do not overload a
client-facing document with internal identifiers unless the user requests an
audit-oriented output.

A reviewed framing document does not automatically become source evidence.
If stakeholders approve or amend it, treat the accepted artefact as a new
source in a later Knowledge Model and Project Model update.

## Boundaries

- Remain independently callable without the `project-design` orchestrator.
- Remain fully usable without GitHub Spec Kit.
- Do not produce detailed functional specifications, screens, exhaustive user
  journeys, technical architecture, implementation design, or a complete
  Product Backlog.
- Do not invent Business Rules, Requirements, Decisions, or project facts.
- Do not resolve contradictions without sufficient authority and evidence.
- Do not treat Assumptions, Options, or proposed Scope as approved direction.
- Do not modify the Canonical Domain Model, Knowledge Model, Project Model, or
  localized terminology.

## Downstream Handoffs

Identify, without performing, the appropriate next work:

- send behavior, journeys, detailed Requirements, and Business Rules to
  `functional-design`;
- send architecture, System Elements, Integrations, quality Requirements, and
  technical Options to `technical-design`;
- send validated Scope, Capabilities, Requirements, and priorities to
  `product-backlog`;
- send approved framing content and presentation constraints to
  `document-output`.
