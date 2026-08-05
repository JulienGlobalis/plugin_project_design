# Project Canvas Presentation Reference

Use this reference to present the required Project Canvas content clearly.
The content contract remains defined by
[the Project Canvas reference](project-canvas.md).

## Contents

- [Presentation principles](#presentation-principles)
- [Review context](#review-context)
- [Section presentation](#section-presentation)
- [Registers and tables](#registers-and-tables)
- [Question classification](#question-classification)
- [Readiness statement](#readiness-statement)
- [Status and language](#status-and-language)

## Presentation Principles

- Represent every required Canvas section or state explicitly that its
  information is insufficient.
- Use the required order unless another order clearly improves readability.
- Keep Existing, Target, and Transition visibly distinct for modernization or
  replacement.
- Keep MVP, outside MVP, explicit exclusions, future Options, and unresolved
  Scope distinct.
- Prefer one concise uncertainty or question register over repeated warnings.
- Preserve a compact source basis for material statements.
- Avoid repeating the same fact in an executive summary and every section.
- Keep the default Canvas concise enough for stakeholder review while
  retaining the information needed by downstream skills.

## Review Context

Start with the project name and, when known:

- Canvas purpose and intended audience;
- requested language;
- source or Project View baseline;
- review date or context;
- explicit warning that provisional or unresolved information remains.

Do not publish a maturity, completeness, or reliability percentage.

An optional short opening paragraph may summarize why the Project exists, its
most consequential boundary, and its most important unresolved matter. It
must not replace or introduce information absent from the ten sections.

## Section Presentation

### Business Context

Use short prose for the situation, relevant Existing state, main Issues, and
business rationale. Use a register only when Constraints or dependencies need
comparison.

### Objectives and Expected Value

Use bullets or a table when Objectives have different statuses, owners, or
measures. Keep unapproved value claims and missing success measures explicit.

### Project Stakeholders and Users

Keep these as separate sections. A combined participant table is acceptable
only if its columns still distinguish project interest or authority from
system interaction.

### Functional Scope

Always display MVP, Outside MVP, and Unresolved Scope separately. A status
column is useful when authority is material.

### Technical Constraints

List known framing-time Constraints and their source or qualification. State
that the section is unresolved when no technical Constraint was supplied;
do not fill it with design recommendations.

### Risks

List Risks separately from confirmed Issues. Confirmed Issues may be
referenced from Business Context or shown in a companion register when this
improves clarity.

### Decisions

Use a Decision register when authority, date, applicability, alternatives, or
consequences require comparison. Keep unresolved Options outside the Decision
list.

### Questions

Use a register that makes impact classification and the next clarification
action visible. Do not name an owner or date when unknown.

### Success Criteria

Present supported criteria and explicitly identify missing baselines,
measures, targets, or approval. Never add numeric thresholds to make the
section look complete.

## Registers and Tables

Use only the registers that improve review.

### Scope Register

| Area | Position | Status | Basis or qualification |
| --- | --- | --- | --- |
| Example | MVP, outside MVP, or unresolved | Established, Provisional, or Unresolved | Source, authority, or condition |

### Participant Register

| Party or role | Stakeholder interest or authority | User or Actor interaction | Status or gap |
| --- | --- | --- | --- |
| Example | Known governance role | Known system role | Established, provisional, or unresolved |

### Constraint Register

| Constraint | Domain | Status or applicability | Basis |
| --- | --- | --- | --- |
| Concise statement | Business, organizational, regulatory, or technical | Qualification | Source |

### Decision Register

| Decision | Authority and date | Consequence | Status or applicability | Basis |
| --- | --- | --- | --- | --- |
| Concise authoritative choice | Known or not supplied | Framing impact | Established, provisional, or unresolved applicability | Source |

### Risk and Issue Register

| Type | Statement | Potential or observed effect | Basis |
| --- | --- | --- | --- |
| Risk or confirmed Issue | Concise statement | Do not invent severity | Source |

### Question Register

| Question | Why it matters | Classification | Owner or authority | Next action |
| --- | --- | --- | --- | --- |
| Project-specific question | Decision or design impact | Blocking, functional, technical, backlog, or deferrable | Known or unresolved | Practical action |

### Success Register

| Criterion or direction | Measure or evidence | Status | Gap or next clarification |
| --- | --- | --- | --- |
| Source-supported result | Known or unresolved | Established, Provisional, or Unresolved | Do not invent a target |

## Question Classification

Use these meanings:

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
- **Deferrable:** the answer is useful later and does not currently change a
  framing or downstream decision.

A question may carry more than one classification. Do not call every unknown
item blocking. Explain the consequence of delay.

## Readiness Statement

End with a short downstream-readiness statement when the next use matters.
Assess `functional-design`, `technical-design`, and backlog preparation
separately. State:

- what can proceed;
- which explicit gaps qualify or block it;
- which Canvas information should be handed off;
- why the next stage need not repeat the complete framing effort.

Do not claim that the Project is universally complete or publish a numeric
reliability score.

## Status and Language

Use internal English canonical references for reasoning. Present natural
labels in the requested output language.

For English, use `Established`, `Provisional`, and `Unresolved` when status
labels are useful.

For French, use `Établi`, `Provisoire`, and `Non résolu` where explicit status
is needed, but prefer natural prose in client-facing passages. For example,
`Problème avéré` is a precise register label for `Issue`; use `problème
constaté` in prose when it reads more naturally and preserves the same
meaning.

Never translate a project-specific Domain Term without source or approved
glossary authority.
