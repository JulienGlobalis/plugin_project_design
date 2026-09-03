---
name: functional-design
description: Create, review, or evolve a traceable Functional Design artefact from a validated Project Canvas and project evidence. Use to define actors and roles, global processes, a product-module-feature inventory, detailed feature behavior, interfaces and fields, business rules, messages, exceptions, acceptance criteria, and unresolved decisions without prescribing technical architecture, implementation tasks, document formatting, or backlog priority.
---

# Functional Design

## Status

IMPLEMENTED — METHODOLOGY VERSION 0.1; FIXTURE AND MANUAL REPLAY PENDING

## Purpose

Turn a validated project position into a living, reviewable description of
expected functional behavior. Produce one business artefact that can evolve
through controlled additions, clarifications, corrections, and deprecations
without losing stable identities, current decisions, or change history.

Own functional design only. Do not own project framing, technical
architecture, implementation planning, backlog organization, document
formatting, or external-format delivery.

## Invocation Brief and Delivery

Before analysis, apply the shared
[Invocation Brief and Project Workspace Delivery contract](../../shared/quality-rules/README.md).
State briefly:

- that `functional-design` is being used and whether the request creates,
  reviews, or updates the artefact;
- which validated Project Canvas, existing Functional Design, Project View,
  and sources are available or missing;
- that `_project-design/functional-design.md` is the business artefact to be
  produced or updated;
- that no document template is required because final-document restitution
  belongs to `document-functional-design`, which is not implemented yet.

When invoked directly and the target has no initialized `_project-design/`
workspace, obtain explicit consent before creating it. An existing workspace
does not authorize silent overwrite. When revising an existing Functional
Design, preserve unaffected content and record the change rather than
rebuilding the artefact from scratch.

The current `project-design` state machine does not route this step yet. If a
guided state exists, inspect it without editing it and use `functional-design`
directly only when the user explicitly requests this implemented skill and a
validated Canvas is available. Do not invent workflow transitions or modify
`project-design-state.json`.

## Required Inputs

Require:

- a validated Project Canvas produced by `project-framing`, or an equivalent
  validated project position covering scope, actors, decisions, constraints,
  risks, questions, and success criteria;
- a declared target project and requested output language.

For an update, also require the current Functional Design artefact and a
traceable change input such as a new source, corrected information, approved
decision, review comment, or explicit user instruction.

Accept when available:

- a Project View or Knowledge Basis;
- existing requirements, process descriptions, policies, interface notes,
  message catalogs, prototypes, data definitions, and user clarification;
- an intended review purpose or downstream consumer.

Do not require the user to construct the shared models manually. Do not start
detailed functional design when the Canvas is explicitly not ready and its
blocking questions prevent responsible design. Report the blockers and return
them to `project-framing`.

## Required References

Apply these contracts without redefining them:

- [Project Model](../../shared/project-model/README.md)
- [Knowledge Model](../../shared/knowledge-model/README.md)
- [Canonical Domain Model](../../shared/terminology/canonical-domain-model.md)
- [Shared terminology](../../shared/terminology/README.md)
- [Quality rules](../../shared/quality-rules/README.md)

Before creating or updating the artefact, read the
[Functional Design structure reference](references/functional-design.md).
Before delivery, read the
[Functional Design quality checklist](references/quality-checklist.md).
Read the [short fictional example](references/functional-design-example.md)
only when it helps interpret the expected granularity, stable identifiers, or
cross-references. Never reuse its project facts.

When French output is requested, also read the
[French canonical terminology](../../shared/terminology/canonical-terms.fr.md).

## Working Modes

### Create

Create the first Functional Design from the validated Canvas and supporting
evidence. Establish stable identifiers only for elements actually represented.
Do not populate required-looking sections with invented behavior.

### Update

Compare the change input with the current artefact and identify affected
identifiers before editing. Classify each change as an addition,
clarification, correction, deprecation, or replacement. Preserve unaffected
sections, do not renumber stable identifiers, and append one concise change
record containing only known date, affected identifiers, reason or source,
and decision status.

Never silently replace a validated behavior or Decision. When authority is
insufficient, retain the current applicable behavior and add a focused Open
Question or a clearly provisional alternative.

### Review

Assess coverage, internal consistency, traceability, unresolved decisions,
and readiness for technical design or backlog preparation. Do not rewrite the
artefact unless the user also requests an update.

## Method

### 1. Establish the Functional Baseline

Read the Canvas first. Select the relevant Actor, Need, Capability, Process,
Requirement, Business Rule, Scope, Decision, and Open Question elements and
their relationships. Preserve Established, Provisional, and Unresolved status
internally and keep Existing, Target, and Transition behavior distinct.

Use raw sources to support or qualify the design, never to bypass a validated
Canvas boundary. Identify any founded Canvas correction separately for
traceable upstream review; do not silently change the Canvas from this skill.

### 2. Build the Functional Inventory

Identify actors and functional roles, then describe the target global
processes. Build the product-module-feature inventory as a navigation and
coverage table, not as a backlog.

Assign stable project-local identifiers to represented processes, products,
modules, features, rules, interfaces, fields, messages, and acceptance
criteria. Keep an existing identifier when an element is renamed or revised.
Never reuse or renumber an identifier merely to make a sequence tidy.

The inventory must distinguish product, module, and feature levels without
forcing all projects to use every level. A single-product project may omit a
meaningless product column or mark it once without inventing decomposition.

### 3. Specify Each Feature

For every feature in the inventory, provide only supported detail:

- identity, name, maturity, product or module, objective, target actors,
  prerequisites, postconditions, and functional dependencies;
- nominal scenario as observable actor and system behavior;
- alternative valid scenarios when the outcome is reached through another
  supported path;
- errors and exceptions with trigger, expected handling, resulting state, and
  visible feedback when known;
- acceptance criteria that are observable, testable, traceable, and free of
  invented thresholds;
- focused questions and Decisions still required;
- interfaces and fields with expected behavior and field-level rules;
- feature-specific Business Rules;
- references to messages from the shared catalog.

Do not turn a Capability into a feature automatically. Decompose only when
evidence and the requested functional granularity justify it. Do not describe
database schemas, APIs, frameworks, components, deployment, or visual styling.

### 4. Consolidate Cross-Cutting Content

Keep global Business Rules with the general specifications and reference them
from affected features. Keep every user-visible or transactional message in
one annex catalog with a stable message identifier; feature sections describe
the trigger and reference the catalog entry instead of duplicating message
content.

Centralize a functional glossary or data dictionary only when several
features need the same definitions. Do not create an exhaustive data model or
technical schema.

### 5. Manage Gaps and Decisions

Write `To be defined` or the natural requested-language equivalent when a
required field lacks validated content and does not justify an actionable
question. Create an Open Question only when its answer changes behavior,
scope, a rule, an interface, acceptance, technical-design readiness, or
backlog readiness.

Keep competing rules or behaviors unresolved until sufficient evidence and
authority establish a current position. Never select the most detailed,
recent, or convenient source by default.

### 6. Verify and Deliver

Verify that:

- every inventory feature has exactly one detailed specification or an
  explicit justified deferral;
- every detailed feature maps back to the inventory and validated scope;
- every referenced rule, field, interface, message, and acceptance criterion
  resolves to one stable identifier;
- nominal, alternative, error, and exception behavior are not conflated;
- global and feature-specific rules are not duplicated inconsistently;
- the change history explains updates without becoming a full evidence log;
- no technical solution, implementation task, priority, estimate, or backlog
  item has been invented.

Save the artefact to `_project-design/functional-design.md`. Report material
gaps and separately qualify whether the artefact can responsibly feed:

- technical design;
- product backlog preparation.

Readiness is purpose-specific and may be `Ready`, `Ready with reservations`,
or `Not ready`, or a natural equivalent. Do not calculate a completeness
score.

## Artefact Contract

The Functional Design is a format-neutral business artefact and remains the
source for its future documentary representation. It must preserve:

- stable element identifiers and cross-references;
- the current applicable functional behavior;
- known maturity or unresolved status without presenting proposals as
  Decisions;
- the reason and affected identifiers for later changes;
- traceability to the Project Canvas, Project View, Decisions, and supporting
  evidence;
- explicit gaps and downstream readiness.

The structure may grow with the project, but existing identifiers and meaning
must not be silently rewritten. A document template, layout, export format, or
visual identity must not influence functional content.

## Boundaries and Handoffs

- Return framing defects or scope changes to `project-framing`.
- Hand architecture, integrations, APIs, security mechanisms, infrastructure,
  performance design, and deployment to `technical-design`.
- Hand epics, user stories, tasks, prioritization, estimation, and increments
  to `product-backlog`.
- Hand final-document formatting to `document-functional-design` only after
  that documentary methodology is implemented.
- Remain independently callable, Spec Kit independent, and free of runtime
  dependency on repository development resources.
- Do not modify the Canonical Domain Model, Knowledge Model, Project Model, or
  Project Canvas silently.
