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

- presents the current validated project position;
- makes project boundaries understandable;
- excludes proposals, assumptions, and unsupported information from the
  definition of the Project;
- identifies only unresolved Decisions that condition a downstream stage;
- can be consumed by decision-makers and the next design steps without
  repeating the analysis process.

Keep evidence, source identifiers, Normalization Status, conflicting
formulations, and arbitration history in the internal analysis. Include them
only in a separate audit deliverable explicitly requested by the user.

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

Cover validated Objectives, desired results, and supported business, user, or
organizational value. Include measurable Objectives only when an authorized
position justifies the measure or target. Use `To be defined` when an
indispensable element is unavailable.

Do not convert a proposed solution, Capability, or metric into an Objective.

### 3. Project Stakeholders

Identify validated sponsors, decision-makers, business and technical owners,
contributors, teams, partners, external bodies, and materially affected
groups. State `To be defined` for an indispensable ownership gap.

Do not infer system interaction from stakeholder status.

### 4. Users

Identify validated direct and indirect user populations, their known roles,
principal Needs, usage context, rights, and responsibilities. Do not include a
population that is merely proposed as if it defined the Project.

Do not invent personas or enrich sparse user information into unsupported
profiles.

### 5. Functional Scope

Use concise subsections or bullets for:

- **MVP:** validated Capabilities, populations, Processes,
  applications, modules, and known limits included in the first useful
  target;
- **Outside MVP:** authorized exclusions and validated deferred items.

Do not include proposed or undecided Capabilities in either list. Turn an
indispensable Scope Decision into a concise Question; otherwise omit it.

### 6. Technical Constraints

Include only technical Constraints already known during framing, such as
imposed existing systems, mandatory or prohibited technologies, hosting,
security, technical compliance, interoperability, existing interfaces,
performance expectations, compatibility, data or infrastructure limits, and
operational restrictions.

Do not propose an architecture, technology stack, API design, component
model, or deployment solution.

### 7. Risks

Identify validated business, organizational, functional, technical,
dependency, data, regulatory, and schedule Risks. Preserve known potential
impacts and already decided responses.

Keep confirmed Issues in Business Context or a clearly labelled companion
register; never recast them as uncertain Risks. Do not invent probability,
severity, owner, or mitigation.

### 8. Decisions

Include only current authoritative Decisions. State each result directly and
concisely. Do not reproduce its former formulations, source identifiers,
opposing positions, rationale history, rejected alternatives, or arbitration
history. Keep preferences, proposals, Assumptions, and unresolved Options out
of this section.

### 9. Questions

Record only concise project-specific Decisions that condition
`functional-design`, `technical-design`, or backlog preparation. State the
question directly, without narrating contradictory formulations or prior
exchanges. Avoid generic questionnaires, deferrable details, and questions
already answered by an authorized Decision.

During an active guided question batch, keep every unanswered question in this
section. Remove a question only after its answer has been incorporated into the
current Canvas position. Keep an explicitly deferred question when its Decision
still conditions validation or a downstream stage. The workflow state may
count these questions but never contains their wording.

### 10. Success Criteria

Describe source-supported project or MVP success criteria, which may concern
business results, adoption, service quality, compliance, performance,
process improvement, Risk reduction, user satisfaction, Scope, delivery, or
global acceptance.

Do not invent numeric thresholds, baselines, measures, or targets. When
criteria are not defined, state the gap and add the necessary questions.

## Filling Rules

1. Normalize project meaning rather than copying each document statement.
2. Project only the current validated position. Never display `Established`,
   `Provisional`, or `Unresolved` in the standard Canvas.
3. Use `Existing`, `Target`, and `Transition` whenever mixing them could
   change meaning.
4. Preserve Knowledge Basis and source references internally; never display
   source identifiers such as `S1`, `S2`, or `S3` in the standard Canvas.
5. Include all material supplied information once, in the section where it
   best supports review.
6. State a meaningful gap concisely; do not populate it with generic advice.
7. Keep the Canvas autonomous, concise, and understandable without the source
   corpus open beside it.
8. Prefer short prose and bullets. Use a table only when it materially improves
   comprehension; never add one for status, evidence, or history.
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
- Keep a required section visible with a brief `To be defined` statement when
  its indispensable information is missing.
- Preserve material conflicting positions and their source basis internally.
- Do not choose the newest, most detailed, or most confidently worded source
  without sufficient authority.
- When an authorized Decision resolves a conflict, present only its current
  result in the Canvas. Retain the opposing basis internally.
- When no authorized Decision resolves an indispensable conflict, ask one
  concise decision question without describing the contradiction.
- Turn a material information or Decision need into a concrete question only
  when it affects review or downstream use.

## MVP and Outside MVP

- Classify an item as MVP only when an explicit source-supported working or
  approved position exists.
- Exclude proposed MVP content until the required authority is evidenced.
- Keep explicit exclusions distinct from future Options and deferred work.
- Never infer that a future idea is outside MVP merely because it is not
  listed in the proposed MVP.
- Turn a disputed or undecided item into a concise Question only when the
  Decision conditions a downstream stage.
- Do not create a complete MVP split to fill a template.

## Downstream Readiness

A Canvas may be usable while retaining concise gaps. It is sufficiently
reliable for a downstream stage when:

- all material current validated information relevant to that stage is
  represented;
- the current validated position and boundaries are understandable;
- no unsupported content fills a gap;
- questions identify what the stage must resolve or defer;
- the downstream skill need not repeat the complete framing analysis.

Report readiness per applicable stage outside the ten Canvas sections when it
is useful to the interaction. Do not declare universal completeness. A
blocking question may prevent all further work; another gap may block only
functional design, technical design, or backlog preparation.

## Later Adjustments

Functional or technical design may reveal reliable new information. Revise
the Canvas only when the change is:

- supported by a new or corrected source or Project View;
- justified as an enrichment, clarification, or correction;
- limited to the affected statements and relationships;
- reflected as the new current Scope, Decision, or lifecycle perspective.

Preserve change history in the internal Project View or a separately requested
audit deliverable, not in the standard Canvas. An approved or amended Canvas
re-enters the information cycle as a source artefact before a later Project
View is normalized.
