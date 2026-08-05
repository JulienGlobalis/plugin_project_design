---
name: project-framing
description: Transform project briefs, discovery notes, source documents, or an existing Project View into a traceable Project Canvas that clarifies the business context, objectives and value, stakeholders, users, MVP and non-MVP scope, known technical constraints, risks, decisions, unresolved questions, and success criteria. Use as the first project-design step for application or software discovery, initiation, alignment, clarification, or reframing before functional design, technical design, or backlog preparation.
---

# Project Framing

## Status

IMPLEMENTED - methodology version 0.2. Manual user validation is required.

## Purpose

Act as the first project-design step. Rework, clarify, and structure the
expression of need into a shared, evidence-aware Project Canvas before
detailed functional design, technical design, or backlog decomposition.

Do more than summarize sources: reconcile compatible information, expose
material conflicts and gaps, make project boundaries understandable, and
prepare responsible downstream work without inventing missing content.

## Inputs

Accept any useful combination of:

- a normalized Project View;
- Knowledge Assertions or structured project information;
- briefs, workshop notes, messages, policies, specifications, inventories,
  decision logs, or other source artefacts;
- user clarifications supplied during the interaction;
- requested audience, language, review purpose, and output constraints.

Do not require the user to prepare the shared models manually.

## Required References

Apply these contracts without redefining them:

- [Project Model](../../shared/project-model/README.md)
- [Knowledge Model](../../shared/knowledge-model/README.md)
- [Canonical Domain Model](../../shared/terminology/canonical-domain-model.md)
- [Shared terminology](../../shared/terminology/README.md)
- [Quality rules](../../shared/quality-rules/README.md)

Before composing or revising a Project Canvas, read the
[Project Canvas reference](references/project-canvas.md). Read the
[framing structure reference](references/framing-structure.md) when selecting
tables, registers, visible status, or presentation order.

When an example would help interpret the required structure, status handling,
or level of detail, read the
[short fictional Project Canvas example](references/project-canvas-example.md).
Treat it as a structural illustration, never as a template for project facts.

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

### 3. Rework the Expression of Need

Identify the information needed to make the project understandable and usable
for the next design steps:

- business context, existing situation, Issues, opportunities, dependencies,
  and material business, organizational, contractual, or regulatory
  Constraints;
- Objectives, expected outcomes, and supported business, user, or
  organizational value;
- Stakeholders, authority, ownership, contributors, and affected groups;
- direct and indirect users, their known roles, Needs, context, rights, and
  responsibilities;
- functional Scope split into MVP, outside MVP, deferred Options, explicit
  exclusions, and unresolved boundaries;
- technical Constraints already known at framing time, without designing a
  solution;
- Risks, Decisions, Open Questions, and project-level success criteria.

Include framing-relevant Capabilities, Requirements, Business Rules,
Processes, System Elements, Integrations, and Transition concerns only when
they clarify the Canvas or materially affect feasibility, boundaries,
governance, risk, or handoff.

Represent dependencies as relationships between project elements. Do not
introduce a new canonical Dependency concept.

### 4. Assess Information Quality

For every material statement:

- preserve its normalization status;
- preserve its lifecycle perspective when relevant;
- retain a traceable source or Knowledge Basis;
- distinguish Stakeholder from Actor or user;
- distinguish Need from Requirement;
- distinguish Risk from confirmed Issue;
- distinguish Assumption from established information;
- distinguish Option or preference from Decision.

Do not:

- infer approval from confident wording;
- prefer a source only because it is newer or more detailed;
- merge conflicting values into a false compromise;
- invent value, Objectives, success criteria, owners, dates, priorities,
  volumes, Constraints, Business Rules, Requirements, or Decisions;
- classify an item as MVP or outside MVP without a source-supported position;
- turn missing information into a negative fact.

When an authorized Decision resolves a conflict, present the normalized
position and retain the material opposing evidence in the traceability basis.
Otherwise keep the matter unresolved.

### 5. Decide Whether to Ask Before Drafting

Produce a useful first Project Canvas without a preliminary questionnaire
whenever possible.

Ask before drafting only when a small amount of information is necessary to
identify the project, understand its basic purpose, select the requested
deliverable, or avoid a materially misleading Canvas.

When questions are necessary:

- ask at most three high-value questions at a time;
- explain briefly why each answer matters;
- never repeat a question already answered by the inputs;
- let the user decline or defer an answer;
- continue with an explicitly incomplete Canvas when the user chooses.

Do not delay the first draft for details that can remain unresolved.

### 6. Compose the Project Canvas

Follow the required content and filling rules in the
[Project Canvas reference](references/project-canvas.md).

Represent all ten sections, in this order unless a clearly better reading
order preserves them:

1. Business Context;
2. Objectives and Expected Value;
3. Project Stakeholders;
4. Users;
5. Functional Scope, split into MVP and Outside MVP;
6. Technical Constraints;
7. Risks;
8. Decisions;
9. Questions;
10. Success Criteria.

If a required section lacks sufficient information, keep the section and
state what is unknown, unsupported, contradictory, or awaiting a Decision.
Do not fill it with generic content.

Keep the default Canvas concise, autonomous, reviewable, and reusable. Use
tables only when they improve comparison, status, ownership, or actionability.
Do not repeat the same information across sections.

For French output:

- use the preferred French terminology as guidance;
- favor natural consulting language over literal model labels;
- preserve project-specific Domain Terms from the sources;
- adapt a preferred label in prose when necessary for naturalness without
  changing its meaning;
- keep English canonical references internal.

### 7. Assess Readiness and Classify Questions

Treat the intended 80-90% reliability as a qualitative business expectation,
never as a calculated score, confidence percentage, or permission to complete
gaps.

The Canvas is ready for downstream use when all material supplied information
has been used, important contradictions and unknowns are explicit, Decisions
remain distinct from Assumptions and Options, boundaries are understandable,
and the next skill can proceed without repeating the complete framing effort.

Classify each question as:

- blocking further progress;
- required before `functional-design`;
- required before `technical-design`;
- required before backlog preparation;
- deferrable.

A question may name more than one affected stage. Prioritize by decision
impact, Risk, and dependency. Identify an owner or decision authority only
when known. Recommend a concrete clarification action without inventing dates
or commitments.

### 8. Verify Before Delivery

Check the output against:

- the source material and Knowledge Basis;
- the shared quality rules;
- the
  [project-framing quality checklist](references/quality-checklist.md).

Confirm that:

- every material claim is supportable;
- every required Canvas section is present or explicitly not sufficiently
  informed;
- opposing information remains visible;
- MVP, outside MVP, explicit exclusions, future Options, and unresolved Scope
  are not conflated;
- Stakeholders and users remain distinct;
- Existing, Target, and Transition are not conflated;
- Risks and Issues are separate;
- Decisions and proposals are separate;
- success criteria are source-supported or explicitly unresolved;
- questions are project-specific, classified, non-duplicative, and
  proportionate;
- no detailed functional, technical, backlog, or document methodology was
  introduced;
- the result can support the next applicable design step without concealing
  its limits.

## Output Contract

Produce one Project Canvas in the requested language. Markdown is the native
and mandatory default format.

The Canvas must be autonomous, readable, structured, versionable, traceable,
and suitable as input to `functional-design` and `technical-design`. It owns
the framing content, not document-format conversion.

Google Docs or Microsoft Word are future optional presentation targets only
when the user supplies a compatible template. Do not claim, simulate, or
implement those conversions in this methodology.

## Traceability

Keep each material Canvas statement traceable through:

```text
Project Canvas statement
    -> Project Element or Relationship
    -> Knowledge Assertion or Assertion Group
    -> Source location
```

Use concise source references suitable for review. Do not overload a
client-facing Canvas with internal identifiers unless the user requests an
audit-oriented output.

A reviewed Canvas does not automatically become source evidence. If
stakeholders approve or amend it, treat the accepted artefact as a new source
in a later Knowledge Model and Project Model update.

## Later Adjustments

`functional-design` or `technical-design` may expose reliable information
that requires a later Canvas revision. Any adjustment must be traceable,
justified by new or corrected evidence, limited to a founded enrichment,
clarification, or correction, and must never silently rewrite validated
information or Decisions.

## Boundaries

- Remain independently callable without the `project-design` orchestrator.
- Remain fully usable without GitHub Spec Kit.
- Do not produce detailed modules, features, data models, exception flows,
  exhaustive journeys, acceptance criteria, architecture, APIs, component
  designs, deployment plans, or a complete Product Backlog.
- Do not invent Business Rules, Requirements, Decisions, success criteria,
  or project facts.
- Do not resolve contradictions without sufficient authority and evidence.
- Do not treat Assumptions, Options, preferences, or proposed Scope as
  approved direction.
- Do not modify the Canonical Domain Model, Knowledge Model, Project Model,
  or localized terminology.
- Do not depend on development-only resources or a platform-specific
  integration.

## Downstream Handoffs

Identify, without performing, the appropriate next work:

- send products, modules, features, users, Processes, journeys, detailed
  Requirements, Business Rules, functional data, exceptions, and functional
  dependencies to `functional-design`;
- send architecture, technologies, System Elements, Integrations, APIs,
  flows, security, performance, deployment, technical Decisions, and
  technical Risks to `technical-design`;
- send designed and validated Scope, Capabilities, Requirements, Business
  Rules, and related traceability to `product-backlog`;
- send validated domain artefacts and presentation constraints to the future
  applicable document skill, directly or through the provisional
  `document-output` orchestrator.
