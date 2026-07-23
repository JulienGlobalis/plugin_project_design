# Project Framing Structure Reference

Use this reference to select and compose framing sections. Do not treat it as
a mandatory template.

## Contents

- [Selection principles](#selection-principles)
- [Recommended structure](#recommended-structure)
- [Registers and tables](#registers-and-tables)
- [Question priority](#question-priority)
- [Status and language](#status-and-language)

## Selection Principles

- Start with the smallest structure that makes the project understandable.
- Include a section only when source or normalized project information
  justifies it.
- Merge context, problem, and existing situation for a simple new project.
- Keep Existing, Target, and Transition separate for modernization or
  replacement.
- Keep Scope, exclusions, and unresolved Scope visibly distinct.
- Prefer one uncertainty register over repeated warnings in every section.
- Preserve a concise source basis for material claims.

## Recommended Structure

### Title and Review Context

State the project name, framing purpose, audience, requested language, and
review context when known.

Indicate plainly when the document contains provisional or unresolved
information. Do not invent a maturity score.

### Executive Framing

Summarize:

- why the project exists;
- the problem or opportunity;
- the intended outcome;
- the most consequential Scope boundary;
- the most important unresolved matter.

Keep this section short and avoid introducing information that does not appear
later.

### Context and Existing Situation

Describe the organization, current process or solution, observed Issues, and
relevant operating context. For a new application, describe the current
business handling without inventing a legacy system.

### Objectives and Expected Outcomes

List Objectives and the outcomes they are intended to produce. Keep missing
measures or targets visible. Do not convert an expected outcome into a
validated benefit or metric.

### Scope

Separate:

- established or provisional in-scope items;
- explicit exclusions;
- unresolved boundaries;
- future Options that are not commitments.

Use a status column when Scope authority or approval is material.

### Stakeholders, Actors, and Users

Keep governance and system interaction distinct. A person or role may be both
a Stakeholder and an Actor, but do not assume one role from the other.

Record authority, ownership, or representation gaps only when supported.

### Target Vision

Describe the intended target condition and high-level Capabilities. Avoid
screens, detailed journeys, acceptance criteria, and architecture choices.

### Transition Considerations

Include this section when migration, rollout, cutover, continuity, adoption,
training, data treatment, or retirement affects framing.

Keep Transition Options separate from Decisions.

### Constraints, Assumptions, and Dependencies

Separate non-negotiable Constraints from provisional Assumptions.

Describe dependencies as relationships or external reliance. Do not invent a
dependency owner or classify a preference as a Constraint.

### Decisions and Options

List material Decisions already made, their authority when known, and the
direction they establish. List unresolved Options separately.

Do not present a historical Decision as still binding when applicability is
unknown.

### Risks and Confirmed Issues

Use separate lists or tables:

- Risk: uncertain event or condition;
- confirmed Issue: currently observed problem or deficiency.

Do not add probability, impact, severity, or owner values unless the sources
or user provide them.

### Unresolved Questions

Phrase each question as a concrete information or decision need. Include:

- why it matters;
- priority category;
- known owner or authority;
- recommended next clarification action.

Do not repeat questions already answered elsewhere in the framing.

### Recommended Next Steps

Prioritize practical clarification, validation, and downstream design work.
Name an owner or date only when known.

Recommend a downstream skill without performing its methodology.

### Evidence and Source Basis

Provide a compact source list or section-level references. Preserve material
supporting, qualifying, and opposing sources.

Use human-readable source names and locations. Keep internal model identifiers
out of normal stakeholder-facing output.

## Registers and Tables

Use only the tables that improve review.

### Scope Register

| Area | Position | Status | Basis or qualification |
| --- | --- | --- | --- |
| Example | In, out, or unresolved | Established, Provisional, or Unresolved | Source or condition |

### Participant Register

| Party or role | Stakeholder interest or authority | Actor interaction | Status or gap |
| --- | --- | --- | --- |
| Example | Known governance role | Known system role | Established, provisional, or unresolved |

### Constraint and Assumption Register

| Type | Statement | Status or validation need | Basis |
| --- | --- | --- | --- |
| Constraint or Assumption | Concise statement | Applicable qualification | Source |

### Decision and Option Register

| Type | Position | Authority or status | Consequence |
| --- | --- | --- | --- |
| Decision or Option | Concise statement | Known authority or unresolved status | Framing impact |

### Risk and Issue Register

| Type | Statement | Potential or observed effect | Basis |
| --- | --- | --- | --- |
| Risk or confirmed Issue | Concise statement | Do not invent severity | Source |

### Clarification Register

| Question | Why it matters | Priority | Owner or authority | Next action |
| --- | --- | --- | --- | --- |
| Concrete question | Decision or design impact | Approval, next phase, or deferred | Known or unresolved | Practical action |

## Question Priority

Use these meanings:

- **Required before framing approval:** purpose, material boundary, authority,
  or critical Constraint cannot be agreed reliably without the answer.
- **Required before the next design phase:** the framing remains reviewable,
  but responsible functional, technical, or backlog work needs the answer.
- **Can be deferred:** the answer is useful later and does not currently
  change framing decisions.

Do not call every unknown item blocking. Explain the consequence of delay.

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
