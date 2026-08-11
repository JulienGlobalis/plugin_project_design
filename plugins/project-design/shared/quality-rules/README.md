# Shared Quality Rules

## Status

IMPLEMENTED - common verification contract version 0.1.

This directory defines common quality principles and traceability rules.
Skill-specific criteria remain in each implemented skill and will expand as
the remaining methodologies are defined.

Under the accepted
[common information architecture](../project-model/information-architecture.md),
the Knowledge Model distinguishes:

- Fact
- Interpretation
- Assumption
- Proposal
- Decision
- Open Question

Version 0.1 of these responsibilities, including provenance, confidence,
uncertainty, validation, and assertion relationships, is defined in the
[Minimal Knowledge Model](../knowledge-model/README.md).

The shared models and future methodologies must prohibit unsupported
invention, preserve source traceability, and prevent unresolved assumptions
from being represented as validated decisions.

Version 0.1 of the
[Minimal Normalized Project Model](../project-model/README.md) distinguishes
Established, Provisional, and Unresolved project information; Existing,
Target, and Transition perspectives; and Supporting, Qualifying, and Opposing
Knowledge Basis links.

Canonical meanings for Assumption, Option, Decision, and Open Question are
defined in the
[Canonical Domain Model](../terminology/canonical-domain-model.md). Fact,
Interpretation, and epistemic Proposal classification remain Knowledge Model
responsibilities.

## Common Verification Contract

Every installable methodology must:

- support material statements with source evidence or an explicit Knowledge
  Basis;
- preserve provenance and material opposing evidence;
- keep Established, Provisional, and Unresolved information distinct;
- keep Existing, Target, and Transition perspectives distinct;
- preserve unresolved contradictions until sufficient evidence and authority
  support a resolution;
- keep canonical distinctions such as Assumption, Option, Decision, Risk,
  Issue, Need, Requirement, Stakeholder, and Actor;
- avoid inventing owners, dates, measures, priorities, Constraints,
  Requirements, Business Rules, or Decisions;
- make missing information and uncertainty visible without treating source
  absence as proof that information does not exist;
- keep generated statements traceable through normalized project information
  and extracted knowledge to source artefacts;
- remain within the responsibility and downstream boundaries of the invoked
  skill.

Localized outputs must use the preferred terminology for the requested
language while preserving canonical distinctions. The initial mapping and
fallback rules are defined by the
[French terminology companion](../terminology/canonical-terms.fr.md).

Each implemented skill must keep its methodology-level quality contract inside
its installable directory. Development tests validate these contracts but are
not runtime dependencies.

## Invocation Brief

Before executing any `project-design` skill, give the user one short launch
brief that states:

- the selected skill or ordered set of skills and its immediate purpose;
- the inputs already available and any required input still missing;
- the business artefact, document, or other deliverable that will be produced;
- every model or template the user must provide, distinguishing required,
  optional, and replaced by a built-in default.

Keep this brief operational and concise. Do not restate the methodology. When
several skills are requested, present one combined brief in execution order.
Proceed without asking for redundant confirmation when all required inputs and
choices are available, except for the mandatory `project-design` consent gate
before workspace initialization. Ask only when consent or a missing required
input, format, or template choice would materially change or block the result.

For a placeholder skill, the brief must state that the methodology is not yet
implemented, name the forecast inputs and outputs, and clearly say that no
artefact or document will be generated.

## Project Workspace Delivery

When a skill generates a durable Markdown artefact or document for a target
project, create or reuse `_project-design/` at the root of that target project
only after the user has explicitly agreed to use the plugin for their project
specifications. A direct specialized-skill invocation must obtain this consent
before initializing a missing workspace; an existing workspace counts as a
prior project-level initialization but never as authorization to overwrite.
Never create this directory inside the installed plugin or Codex cache merely
because the skill is running from there.

The guided `project-design` workflow stores its non-business control state at
`_project-design/project-design-state.json`. Create and update it only through
the bundled state-machine script. It may contain consent, phase, choices,
input-presence flags, iteration counts, approval, delivery references, and
transition timestamps. It must never contain project descriptions, source
contents, question or answer text, Canvas statements, Decisions, or other
business knowledge.

Use these stable default paths:

```text
_project-design/
├── project-design-state.json
├── project-canvas.md
├── functional-design.md
├── technical-design.md
├── product-backlog.md
└── documents/
    ├── project-canvas.md
    ├── functional-design.md
    ├── technical-design.md
    └── product-backlog.md
```

External document files use the same documentary directory, for example
`_project-design/documents/project-canvas.docx`. A native Google Doc remains in
Google Drive and is delivered by link; do not represent its link as a local
document file.

Only create files supported by an implemented skill and actually requested or
generated. Keep temporary notes, source copies, binaries, and confidential raw
inputs out of this directory. Store every durable Markdown output generated by
the plugin under `_project-design/`, including a Markdown source used as a
durable companion to an external-format document.

Do not overwrite an existing artefact or document silently. When the user is
explicitly revising the same deliverable, update it and preserve traceability.
Otherwise use a clear project-, baseline-, or version-qualified filename.

If the target project root is unavailable or not writable, deliver the content
through the active interface, state that `_project-design/` could not be
created, and provide the intended relative path. Do not claim that a file was
saved when it was not.
