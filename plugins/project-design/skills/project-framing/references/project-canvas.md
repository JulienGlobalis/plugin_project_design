# Project Canvas Reference

Use this reference whenever `project-framing` creates or revises its primary
output.

## Contents

- [Purpose and role](#purpose-and-role)
- [Required structure](#required-structure)
- [Filling rules](#filling-rules)
- [Semantic safeguards](#semantic-safeguards)
- [Missing and contradictory information](#missing-and-contradictory-information)
- [MVP and outside MVP](#mvp-and-outside-mvp)
- [Downstream readiness](#downstream-readiness)
- [Later adjustments](#later-adjustments)

## Purpose and Role

The Project Canvas is the primary `project-framing` artefact. It transforms
the available expression of need into a shared project understanding that is
reliable enough to support functional and technical design without repeating
the complete framing effort.

It is not a source summary, requirements specification, technical
architecture, backlog, document template, or document-format conversion. Its
logical structure is format-neutral; final document structure and formatting
belong to `document-project-canvas`.

The intended 80-90% reliability is a qualitative business expectation. Never
calculate, display, or infer a percentage. Reliability means that the Canvas:

- uses all material information available in the supplied sources;
- makes material contradictions and unknowns visible;
- distinguishes Decisions from Assumptions, preferences, and Options;
- makes project boundaries understandable;
- preserves traceability;
- can be consumed by the next design steps without pretending to be complete.

## Required Structure

Represent every section below. The order may change only when another order
clearly improves readability without hiding a section. When information is
insufficient, state the gap explicitly instead of removing the heading.

### 1. Business Context

Cover the source-supported subset of:

- the situation that originated the Project;
- business concerns and relevant Existing conditions;
- confirmed Issues and opportunities;
- business, organizational, contractual, and regulatory Constraints;
- known structural dates or deadlines;
- important business dependencies.

Do not place purely technical solution choices here.

### 2. Objectives and Expected Value

Cover Objectives, desired results, and supported business, user, or
organizational value. Include measurable Objectives only when sources justify
the measure or target. Preserve divergences and missing Objectives, values,
baselines, or targets.

Do not convert a proposed solution, Capability, or metric into an Objective.

### 3. Project Stakeholders

Identify supported sponsors, decision-makers, business and technical owners,
contributors, teams, partners, external bodies, and materially affected
groups. Preserve known authority and ownership gaps.

Do not infer system interaction from stakeholder status.

### 4. Users

Identify direct and indirect user populations, their known roles, principal
Needs, usage context, rights, and responsibilities. Record populations that
remain insufficiently described.

Do not invent personas or enrich sparse user information into unsupported
profiles.

### 5. Functional Scope

Use distinct subsections or columns for:

- **MVP:** source-supported Capabilities, populations, Processes,
  applications, modules, and known limits included in the first useful
  target;
- **Outside MVP:** explicitly excluded items, deferred functions, later
  improvements, and Options not currently selected;
- **Unresolved Scope:** items awaiting authority or evidence.

Preserve the authority and Normalization Status of each position.

### 6. Technical Constraints

Include only technical Constraints already known during framing, such as
imposed existing systems, mandatory or prohibited technologies, hosting,
security, technical compliance, interoperability, existing interfaces,
performance expectations, compatibility, data or infrastructure limits, and
operational restrictions.

Do not propose an architecture, technology stack, API design, component
model, or deployment solution.

### 7. Risks

Identify source-supported business, organizational, functional, technical,
dependency, data, regulatory, and schedule Risks. Preserve known potential
impacts and already decided responses.

Keep confirmed Issues in Business Context or a clearly labelled companion
register; never recast them as uncertain Risks. Do not invent probability,
severity, owner, or mitigation.

### 8. Decisions

Include only authoritative, source-supported Decisions. Preserve, when known:

- subject and status;
- author or authority;
- rationale and date;
- consequences;
- documented rejected alternatives;
- provenance and current applicability.

Keep preferences, proposals, Assumptions, and unresolved Options outside this
section or label them explicitly as not decided.

### 9. Questions

Record project-specific unresolved information and decisions. For every
question, state why it matters and classify it as one or more of:

- blocking further progress;
- required before `functional-design`;
- required before `technical-design`;
- required before backlog preparation;
- deferrable.

Name an owner or authority only when known. Avoid generic questionnaires and
questions already answered by the inputs.

### 10. Success Criteria

Describe source-supported project or MVP success criteria, which may concern
business results, adoption, service quality, compliance, performance,
process improvement, Risk reduction, user satisfaction, Scope, delivery, or
global acceptance.

Do not invent numeric thresholds, baselines, measures, or targets. When
criteria are not defined, state the gap and add the necessary questions.

## Filling Rules

1. Normalize project meaning rather than copying each document statement.
2. Use `Established`, `Provisional`, and `Unresolved` according to the Project
   Model; show status where misunderstanding would matter.
3. Use `Existing`, `Target`, and `Transition` whenever mixing them could
   change meaning.
4. Preserve a concise Knowledge Basis or source reference for every material
   statement.
5. Include all material supplied information once, in the section where it
   best supports review.
6. State a meaningful gap concisely; do not populate it with generic advice.
7. Keep the Canvas autonomous, concise, and understandable without the source
   corpus open beside it.
8. Use prose for context and rationale; use tables for comparison, status,
   authority, or action registers.
9. Keep internal identifiers and model mechanics out of normal
   stakeholder-facing prose.
10. Preserve the requested language and governed terminology.

## Semantic Safeguards

Preserve these distinctions:

- Stakeholder versus Actor or user;
- Need versus Requirement;
- Objective versus expected value or measure;
- Constraint versus preference;
- Assumption versus established information;
- Option or proposal versus Decision;
- Risk versus confirmed Issue;
- proposed Scope versus approved Scope;
- Existing versus Target versus Transition.

Do not introduce detailed functional design merely to make the Canvas appear
complete. Products, modules, exhaustive features, full journeys, functional
data models, exception catalogs, and acceptance criteria belong downstream.

Do not introduce detailed technical design. Architecture, technology
selection, components, API contracts, data flows, deployment design, and
security design belong downstream.

## Missing and Contradictory Information

- Treat source absence as a scoped gap, not proof that information does not
  exist.
- Keep a required section visible with an explicit `Unresolved` statement
  when its information is materially missing.
- Preserve every material conflicting position and its source basis.
- Do not choose the newest, most detailed, or most confidently worded source
  without sufficient authority.
- When an authorized Decision resolves a conflict, present the current
  normalized position and retain the opposing basis for audit.
- Turn a material information or Decision need into a concrete question only
  when it affects review or downstream use.

## MVP and Outside MVP

- Classify an item as MVP only when an explicit source-supported working or
  approved position exists.
- Mark proposed MVP content `Provisional` until the required authority is
  evidenced.
- Keep explicit exclusions distinct from future Options and deferred work.
- Never infer that a future idea is outside MVP merely because it is not
  listed in the proposed MVP.
- Place disputed or undecided items in Unresolved Scope and connect them to a
  question or Decision need.
- Do not create a complete MVP split to fill a template.

## Downstream Readiness

A Canvas may be usable while retaining explicit gaps. It is sufficiently
reliable for a downstream stage when:

- all material supplied information relevant to that stage is represented;
- material contradictions and unknowns are visible;
- boundaries and authority are understandable;
- no unsupported content fills a gap;
- traceability is adequate for review;
- questions identify what the stage must resolve or defer;
- the downstream skill need not repeat the complete framing analysis.

State readiness per applicable stage. Do not declare universal completeness.
A blocking question may prevent all further work; another gap may block only
functional design, technical design, or backlog preparation.

## Later Adjustments

Functional or technical design may reveal reliable new information. Revise
the Canvas only when the change is:

- supported by a new or corrected source or Project View;
- traceable to that basis;
- justified as an enrichment, clarification, or correction;
- limited to the affected statements and relationships;
- explicit about changed status, Scope, Decision, or lifecycle perspective.

Never silently rewrite validated information or Decisions. An approved or
amended Canvas re-enters the information cycle as a source artefact before a
later Project View is normalized.
