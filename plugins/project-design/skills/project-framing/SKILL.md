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

## Invocation Brief and Delivery

Before analysis, apply the shared
[Invocation Brief and Project Workspace Delivery contract](../../shared/quality-rules/README.md).
State briefly that `project-framing` is being used, which sources or Project
View are available, that one Project Canvas business artefact will be produced,
and that no document template is required. Save the durable Markdown artefact
to `_project-design/project-canvas.md` at the target project root unless an
explicit compatible project-qualified or versioned filename is needed.

When invoked directly and the target has no initialized `_project-design/`
workspace, briefly present the plugin workspace and obtain explicit consent
before creating it. Do not repeat this consent gate when `project-design` has
already completed it in the current project flow.

## Guided Workflow State

Remain independently callable, but when
`_project-design/project-design-state.json` exists or the user invoked the
guided plugin flow, use the state machine at
`../project-design/scripts/workflow.py`. Run `status` before framing and proceed
only when the phase is `framing_iterations`.

After every question-and-answer round, update
`_project-design/project-canvas.md`, then run `record-iteration` with the actual
number of questions and answers. Use `--ready-for-review` only when the Canvas
is ready for explicit review. Never edit the state file directly or record
question and answer content in it.

When the phase is `awaiting_canvas_approval`, wait for explicit user approval.
After approval, run `approve-canvas --confirmed`; do not invoke documentary
restitution unless the resulting phase is `awaiting_document`.

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
[framing structure reference](references/framing-structure.md) when organizing
artefact sections, registers, visible status, or logical order.

When an example would help interpret the required structure, status handling,
or level of detail, read the
[short fictional Project Canvas example](references/project-canvas-example.md).
Treat it as a structural illustration, never as a template for project facts.

When French output is requested, also read the
[French canonical terminology](../../shared/terminology/canonical-terms.fr.md).

## Workflow

### 1. Start the Guided Framing Conversation

Before analyzing project content, present `project-framing` as the first
project-design step and explain that its Markdown output is
`_project-design/project-canvas.md`. Name the ten Canvas chapters that will be
built:

1. Business Context;
2. Objectives and Expected Value;
3. Project Stakeholders;
4. Users;
5. Functional Scope;
6. Technical Constraints;
7. Risks;
8. Decisions;
9. Questions;
10. Success Criteria.

Then resolve the interaction in this order, unless `project-design` already
captured an answer:

1. Ask whether the user also wants a final Word or native Google Docs document
   in addition to the mandatory Markdown Canvas.
2. If yes, ask whether to use a supplied local template, a Google Drive
   template link, or the default professional structure. Record the choice for
   `document-project-canvas`; do not apply it during framing.
3. Ask whether source documents should remain at their original locations or
   be centralized in the optional `_sources/` workspace. If centralized, use
   the project-design source-workspace script and require explicit approval
   before copying each local file. Keep Drive-native sources as links.
4. Ask the user to provide either a project description directly in the
   conversation or one or more source documents. Accept both together.

This opening is a short intake, not an exhaustive questionnaire. Do not ask
about project substance before the user supplies the initial description or
sources.

### 2. Establish the Request Context

Identify:

- the project or initiative being framed;
- the available inputs;
- the intended audience and immediate use when supplied;
- the requested artefact language;
- whether an existing Project View is available.

Infer language and audience from the request when clear. Do not ask the user
to confirm information that is already evident.

Use English when no language is requested and no interaction language clearly
indicates another choice. When a requested language resource is missing,
state the limitation and obtain an explicit fallback choice; never silently
use an unrelated localized language.

### 3. Prepare the Working Project View

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

### 4. Rework the Expression of Need

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

### 5. Assess Information Quality

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

### 6. Co-construct the Canvas Through Iterations

After receiving the initial description or sources, prepare a useful working
Canvas from the available information. Then conduct focused question-and-answer
rounds to improve it progressively.

For every round:

- ask at most three high-value questions at a time;
- explain briefly why each answer matters;
- never repeat a question already answered by the inputs;
- let the user decline or defer an answer;
- update the affected Canvas chapters from the answers without rewriting
  unrelated validated content;
- summarize what changed and keep unresolved points visible;
- prioritize questions that change Scope, authority, value, Decisions, Risks,
  success criteria, or downstream readiness.

In a guided workflow, save the updated working Canvas and record the successful
iteration transition before starting another round. If the transition is
rejected, stop and follow the state machine's returned phase.

Continue until the user validates the Canvas for delivery, asks to stop, or
the remaining questions can be explicitly deferred. Do not demand complete
answers before producing a useful draft, and do not invent content to end the
conversation.

### 7. Compose the Project Canvas

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

### 8. Assess Readiness and Classify Questions

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

### 9. Verify Before Delivery

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
- the user was able to review the progressively updated Canvas and explicitly
  validate delivery or defer the remaining questions;
- no detailed functional, technical, backlog, or document methodology was
  introduced;
- the result can support the next applicable design step without concealing
  its limits.

## Artefact Contract

Produce one structured Project Canvas business artefact in the requested
language.

When filesystem delivery is available, the Markdown file governed by this
contract belongs under `_project-design/` according to the shared workspace
delivery rules. This storage convention does not turn the artefact into a
formatted final document or give `project-framing` document-format ownership.

The Canvas must be autonomous, structured, versionable, traceable, and
suitable as input to `functional-design`, `technical-design`,
`product-backlog`, and `document-project-canvas`. `project-framing` owns the
framing knowledge only. It does not select a document format, apply a
template, format a final document, convert, or export.

When the user requested Word or Google Docs, hand the validated Canvas and the
recorded format/template choice to `document-project-canvas` after saving the
Markdown business artefact. Do not delay or merge the Markdown Canvas into its
documentary representation.

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
- send the validated Project Canvas artefact and separately supplied document
  constraints to `document-project-canvas` when a final document is required.
