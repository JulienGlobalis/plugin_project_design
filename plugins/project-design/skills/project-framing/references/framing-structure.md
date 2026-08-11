# Project Canvas Artefact Structure Reference

Use this reference to organize the required Project Canvas business content.
The content contract remains defined by
[the Project Canvas reference](project-canvas.md).

## Structure Principles

- Represent all ten required sections in their required order.
- Write `To be defined` when an indispensable section has no validated content.
- Keep Existing, Target, and Transition visibly distinct for modernization or
  replacement.
- Keep validated MVP and authorized exclusions distinct.
- Omit proposals, assumptions, and non-authorized Options from the project
  definition.
- Keep only concise Questions that condition a downstream stage.
- Avoid repeating the same fact in an executive summary and every section.
- Prefer short paragraphs and bullets; avoid tables when they add no material
  clarity.
- Keep evidence and analysis mechanics outside the standard Canvas.

## Review Context

Start with the project name. Add only a short business-oriented opening when
it improves comprehension.

Do not publish a maturity, completeness, or reliability percentage.

An optional short opening paragraph may summarize why the Project exists, its
most consequential boundary, and its most important unresolved matter. It
must not replace or introduce information absent from the ten sections.

## Section Organization

### Business Context

Represent the situation, relevant Existing state, main Issues, and business
rationale. Use a logical register when Constraints or dependencies need
comparison.

### Objectives and Expected Value

Present validated Objectives and value. Use `To be defined` for an
indispensable missing measure; do not expose status mechanics.

### Project Stakeholders and Users

Keep these as separate sections. A combined participant table is acceptable
only if its columns still distinguish project interest or authority from
system interaction.

### Functional Scope

Display validated MVP content and authorized Outside MVP content separately.
Do not create an Unresolved Scope register; move only a consequential decision
need to Questions.

### Technical Constraints

List validated framing-time Constraints. Write `To be defined` when none is
available; do not fill the section with design recommendations.

### Risks

List Risks separately from confirmed Issues. Confirmed Issues may be
referenced from Business Context or shown in a companion register when this
improves clarity.

### Decisions

State each current Decision result directly. Do not display authority history,
dates, former alternatives, rejected formulations, or source references.

### Questions

Use a short bullet list. Retain only Decisions required before functional
design, technical design, or backlog preparation, without displaying an
impact-classification label.

### Success Criteria

Present validated criteria. Write `To be defined` when indispensable criteria
are unavailable. Never add numeric thresholds to make the section look
complete.

## Registers and Tables

Do not use a register by default. Prefer a few bullets or sentences. A table is
acceptable only when several current validated items share dimensions that a
reader must compare. Never create columns for status, source, evidence,
authority history, contradictions, or arbitration history.

## Question Classification

Use these meanings internally to decide whether a Question belongs in the
Canvas; do not display the classification label by default:

- **Blocking further progress:** a reliable shared frame or any responsible
  next design work cannot continue without the answer.
- **Required before functional design:** Actors, Needs, Processes, Scope,
  Business Rules, functional data, or detailed behavior cannot be designed
  responsibly without the answer.
- **Required before technical design:** architecture, System Elements,
  Integrations, quality concerns, security, deployment, or technical
  feasibility cannot be designed responsibly without the answer.
- **Required before backlog preparation:** validated Scope, ordering inputs,
  or traceability is insufficient for backlog transformation.
- **Deferrable:** omit it from the standard Canvas because it does not
  currently change a framing or downstream decision.

A question may affect more than one stage. Keep its wording direct and do not
narrate the source disagreement or clarification history.

## Readiness Statement

Do not add an eleventh Canvas section. Report downstream readiness separately
in the interaction when useful. The Questions section itself carries the
decisions that condition the next stages.

## Status and Language

Use internal English canonical references for reasoning. Present natural
labels in the requested output language.

Use `Established`, `Provisional`, and `Unresolved` internally when normalizing
information. Never display these labels, or their French equivalents `Établi`,
`Provisoire`, and `Non résolu`, in the standard Canvas. Express only the
current validated meaning in natural business language.

Never translate a project-specific Domain Term without source or approved
glossary authority.
