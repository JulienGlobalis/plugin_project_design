# Project Design

`project-design` is a methodology-first, Markdown-first plugin foundation for
application and software project design. It separates the production of
project knowledge from its documentary restitution so framing, functional
design, technical design, Product Backlog preparation, and document delivery
remain modular, reusable, and traceable.

## Problem Addressed

Project-design knowledge is often spread across briefs, workshops, requirements, architecture notes, and delivery tools. This plugin will provide a shared information architecture and focused skills without coupling the methodology to one AI agent, document format, or orchestration framework.

## Architecture

The official architecture distinguishes global orchestration, business skills,
and document skills.

See the
[Plugin Architecture Overview v1.0](development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md)
for the consolidated layer, model, skill, ownership, flow, and dependency
reference.

- `project-design` now provides the guided entry: skill presentation, explicit
  consent, safe workspace initialization, persisted phase enforcement,
  resumable framing-question batches, stage selection with `project-framing`
  by default, and handoff. Complete cross-stage orchestration remains future
  work.
- `project-framing` is the implemented first design step. It clarifies the
  expression of need and produces the Project Canvas.
- `functional-design` will structure products, modules, features, users,
  processes, journeys, rules, functional data, exceptions, and dependencies.
- `technical-design` will structure architecture, technologies, components,
  integrations, APIs, flows, security, performance, deployment, decisions,
  and technical risks. It may run in parallel with or complement functional
  design when the available inputs permit it.
- `product-backlog` will transform designed and validated Scope into traceable
  backlog items without inventing requirements, priority, value, or effort.
- `document-project-canvas` is the implemented documentary counterpart of
  `project-framing`. It produces a verified Markdown, Microsoft Word, or
  Google Docs document from a validated Project Canvas without changing its
  business knowledge.
- `document-functional-design`, `document-technical-design`, and
  `document-product-backlog` remain installed placeholders for future
  document restitution from their corresponding business artefacts.

Exactly nine skill directories are installed. The `project-design` guided
entry, `project-framing`, and `document-project-canvas` are implemented; the
other six entries are explicit placeholders. Every specialized skill remains independently
callable, and future orchestration must preserve direct use.

Before work begins, the selected skill gives a short operational brief:
skill and purpose, available or missing inputs, deliverables to be generated,
and models or templates the user must provide. Durable Markdown outputs are
stored together under `_project-design/` at the root of the target project;
documentary Markdown uses `_project-design/documents/`.

### Current Availability

| Skill | Installed entry | Current status | Current or forecast responsibility |
| --- | --- | --- | --- |
| `project-design` | Yes | Stateful guided entry implemented | Consent, persistent phase enforcement, workspace initialization, stage selection, and handoff; full routing is not implemented |
| `project-framing` | Yes | Implemented; manual user validation pending | Step 1; produces the Project Canvas business artefact |
| `functional-design` | Yes | Placeholder | Future structured functional-design methodology |
| `technical-design` | Yes | Placeholder | Future complementary or parallel technical-design methodology |
| `product-backlog` | Yes | Placeholder | Future traceable transformation of designed and validated Scope |
| `document-project-canvas` | Yes | Implemented; combined manual validation pending | Project Canvas document in Markdown, Microsoft Word, or Google Docs |
| `document-functional-design` | Yes | Placeholder | Future functional specifications document |
| `document-technical-design` | Yes | Placeholder | Future technical specifications document |
| `document-product-backlog` | Yes | Placeholder | Future Product Backlog document |

An installed placeholder is discoverable but does not provide the future
methodology. The manifests expose all nine installed entries through their
shared `skills/` directory.

```text
project-design
├── project-framing
├── functional-design
├── technical-design
├── product-backlog
├── document-project-canvas          # implemented
├── document-functional-design       # placeholder
├── document-technical-design        # placeholder
└── document-product-backlog         # placeholder
```

## Skill Usage Guide

Skills can be invoked by naming them explicitly in a natural-language prompt
in Codex or Claude Code. Use `project-design` for the guided workflow, or call
an implemented specialized skill directly when its required input already
exists. A direct call remains subject to the same consent, workspace, input,
validation, and delivery rules as the guided workflow.

Examples below are platform-neutral and ready to adapt. Replace paths,
languages, formats, and source names with project-specific values. Only
`project-design`, `project-framing`, and `document-project-canvas` execute a
methodology today. Placeholder examples are explicitly marked and must not
create an artefact.

### `project-design` — Guided Workflow

[Full skill instructions](plugins/project-design/skills/project-design/SKILL.md)

- **Status:** implemented stateful guided entry; complete multi-stage
  orchestration remains future work.
- **Use it when:** starting, resuming, or checking a project specification
  workflow and when the plugin should guide consent, setup, source intake,
  framing, approval, and optional document delivery.
- **Inputs:** the target project root, then the project description or source
  documents requested by the workflow. Documentary preferences and the source
  storage strategy are collected in order.
- **Outputs:** `_project-design/project-design-state.json`, the initialized
  workspace, and artefacts produced by implemented specialized skills. The
  state file contains workflow control data, never project knowledge.
- **Important:** on an existing workflow, the skill runs `status` first and
  follows only its recorded `next_action`. It never resets or skips a phase
  based on conversation history.

Example — start a new guided workflow:

```text
Use the project-design skill to guide the specification of the application in
/path/to/my-project. Present the available skills and workspace rules, then ask
for my explicit consent before creating or reusing _project-design/.
```

Example — resume after a conversation change:

```text
Resume the project-design workflow in /path/to/my-project. Check the persisted
status first and perform only the recorded next action. If framing answers are
pending, present exactly the unanswered questions already stored in the
Project Canvas.
```

### `project-framing` — Project Canvas

[Full skill instructions](plugins/project-design/skills/project-framing/SKILL.md)

- **Status:** implemented methodology version 0.4; manual user validation is
  still required.
- **Use it when:** clarifying a project brief, discovery material, an existing
  application, or an early expression of need before functional design,
  technical design, or backlog preparation.
- **Inputs:** a project description, source documents, an existing Project
  View, or any useful combination of them. No document template is required.
- **Output:** the current validated project position in the ten-section
  `_project-design/project-canvas.md` business artefact.
- **Important:** the standard Canvas is concise and decision-oriented. It does
  not expose audit mechanics or invent missing information. Any indispensable
  unresolved point becomes a focused question; other missing content remains
  `To be defined` in the requested output language.

Example — direct framing from mixed sources:

```text
Use the project-framing skill for /path/to/my-project. Build a French Project
Canvas from the brief in docs/brief.md and the workshop notes in
docs/workshop-notes.md. Preserve unresolved decisions, ask every materially
necessary decision question without an arbitrary limit, and save the durable
business artefact to _project-design/project-canvas.md.
```

### `functional-design` — Functional Design

[Full skill instructions](plugins/project-design/skills/functional-design/SKILL.md)

- **Status:** placeholder; the methodology and artefact structure are not
  implemented.
- **Forecast use:** describe modules, features, actors, journeys, business
  rules, functional data, exceptions, dependencies, requirements, and
  acceptance criteria from a validated Project Canvas and project evidence.
- **Forecast inputs:** Project Canvas, stakeholder needs, requirements,
  observed workflows, terminology, constraints, rules, and desired outcomes.
- **Forecast output:** `_project-design/functional-design.md` once the
  methodology is implemented.
- **Current behavior:** announce that the skill is unavailable and create no
  file. It must not perform document formatting or silently redo framing.

Example — current availability check, not design execution:

```text
Check the functional-design skill for /path/to/my-project. If it is still a
placeholder, summarize its forecast inputs and outputs, identify what is
missing for future use, and do not create _project-design/functional-design.md.
```

### `technical-design` — Technical Design

[Full skill instructions](plugins/project-design/skills/technical-design/SKILL.md)

- **Status:** placeholder; the methodology and artefact structure are not
  implemented.
- **Forecast use:** define a technical direction covering architecture,
  components, integrations, APIs, flows, security, performance, hosting,
  operations, deployment, decisions, risks, and non-functional requirements.
- **Forecast inputs:** Project Canvas, functional requirements when available,
  system context, standards, integrations, constraints, risks, and prior
  decisions.
- **Forecast output:** `_project-design/technical-design.md` once the
  methodology is implemented.
- **Current behavior:** announce that the skill is unavailable and create no
  file. Proposals must remain distinct from approved technical decisions.

Example — current availability check, not design execution:

```text
Check the technical-design skill for /path/to/my-project using the validated
Project Canvas and the existing architecture notes. If the methodology is
still a placeholder, explain the forecast coverage and do not generate a
Technical Design artefact.
```

### `product-backlog` — Product Backlog Artefact

[Full skill instructions](plugins/project-design/skills/product-backlog/SKILL.md)

- **Status:** placeholder; backlog creation, harmonization, prioritization,
  and estimation are not implemented.
- **Forecast use:** transform validated designed Scope into a traceable Product
  Backlog without inventing requirements, priority, value, or effort.
- **Forecast inputs:** Project Canvas, validated functional or technical
  design, existing backlog material, and known prioritization, estimation,
  ownership, and traceability constraints.
- **Forecast output:** `_project-design/product-backlog.md` once the
  methodology is implemented.
- **Current behavior:** announce that the skill is unavailable and create no
  backlog artefact or backlog items.

Example — current availability check, not backlog generation:

```text
Check whether the product-backlog skill can process the validated design in
/path/to/my-project. If it is still a placeholder, list the forecast inputs
and boundaries and do not create or prioritize backlog items.
```

### `document-project-canvas` — Project Canvas Document

[Full skill instructions](plugins/project-design/skills/document-project-canvas/SKILL.md)

- **Status:** implemented methodology; combined manual validation with
  `project-framing` remains pending.
- **Use it when:** a validated Project Canvas must be delivered as a polished
  native Markdown, Microsoft Word, or Google Docs document.
- **Input:** a validated Project Canvas business artefact. Language, audience,
  output format, and a compatible optional template may also be supplied.
- **Output:** Markdown under `_project-design/documents/`, a verified `.docx`
  there, or a verified native Google Docs link.
- **Important:** this skill formats and verifies the Canvas without adding,
  resolving, removing, or changing project knowledge. A business defect is
  returned to `project-framing` rather than corrected silently.

Example — create a Word document without a supplied template:

```text
Use the document-project-canvas skill to turn the validated
_project-design/project-canvas.md into a professional French Microsoft Word
document. Use the default structure, preserve all business meaning and
unresolved questions, save it to
_project-design/documents/project-canvas.docx, and verify the native result
before delivery.
```

### `document-functional-design` — Functional Specifications Document

[Full skill instructions](plugins/project-design/skills/document-functional-design/SKILL.md)

- **Status:** placeholder; document methodology, template contracts, and
  format integrations are not implemented.
- **Forecast use:** restitute a validated Functional Design as human-facing
  functional specifications without changing its business knowledge.
- **Forecast inputs:** validated Functional Design plus language, presentation,
  optional compatible template, and output-format constraints.
- **Forecast outputs:** Markdown, Microsoft Word, or Google Docs in a future
  implementation.
- **Current behavior:** announce that the skill is unavailable and create no
  file or external document.

Example — current availability check, not document generation:

```text
Check the document-functional-design skill for the validated Functional Design
in /path/to/my-project. If it is still a placeholder, report the future format
options and do not create a functional specifications document.
```

### `document-technical-design` — Technical Specifications Document

[Full skill instructions](plugins/project-design/skills/document-technical-design/SKILL.md)

- **Status:** placeholder; document methodology, template contracts, and
  format integrations are not implemented.
- **Forecast use:** restitute a validated Technical Design as human-facing
  technical specifications without changing its technical decisions.
- **Forecast inputs:** validated Technical Design plus language, presentation,
  optional compatible template, and output-format constraints.
- **Forecast outputs:** Markdown, Microsoft Word, or Google Docs in a future
  implementation.
- **Current behavior:** announce that the skill is unavailable and create no
  file or external document.

Example — current availability check, not document generation:

```text
Check the document-technical-design skill for the validated Technical Design
in /path/to/my-project. If it is still a placeholder, report the forecast
formats and boundaries and do not create a technical specifications document.
```

### `document-product-backlog` — Product Backlog Document

[Full skill instructions](plugins/project-design/skills/document-product-backlog/SKILL.md)

- **Status:** placeholder; document methodology, template contracts, and
  format integrations are not implemented.
- **Forecast use:** restitute a validated Product Backlog without creating,
  reprioritizing, estimating, or changing backlog content.
- **Forecast inputs:** validated Product Backlog plus language, presentation,
  optional compatible template, and output-format constraints.
- **Forecast outputs:** Markdown, Google Sheets, Microsoft Excel, Microsoft
  Word, or Google Docs in a future implementation.
- **Current behavior:** announce that the skill is unavailable and create no
  file, spreadsheet, or external document.

Example — current availability check, not document generation:

```text
Check the document-product-backlog skill for the validated backlog in
/path/to/my-project. If it is still a placeholder, report its forecast native
formats and do not create or modify any backlog document.
```

All skills will rely on the accepted
[common information architecture](plugins/project-design/shared/project-model/information-architecture.md):

```text
Source documents -> Knowledge Model -> Project Model -> Skills -> Generated artefacts
```

The Knowledge Model preserves extracted evidence, provenance, uncertainty,
and conflicts. The Project Model provides normalized project information.
Neither model belongs to an individual skill.

### Design Artefacts and Document Restitution

Business skills own the structured project knowledge they produce. They do
not generate final documents, select output formats, apply templates, export,
or contain document-format logic. Document skills consume one corresponding
validated business artefact and may present it for people or external tools,
but must not invent content, resolve a business question, change a Decision,
or become owners of business methodology.

Version 0.1 of the
[Shared Document Model](plugins/project-design/shared/document-model/README.md)
defines this discipline-neutral artefact-to-document contract for every
implemented and future document skill.

Markdown is the native default. `document-project-canvas` currently supports
native Markdown, Microsoft Word, and Google Docs through available native
document tooling, with a default professional structure or a compatible
supplied template. The rules are:

- `document-project-canvas`: Markdown by default; verified native Google Docs
  or Microsoft Word on explicit request;
- `document-functional-design`: Markdown by default; Google Docs or Microsoft
  Word only in a future implementation when a compatible template is
  supplied;
- `document-technical-design`: the same future format rule for the technical
  artefact;
- `document-product-backlog`: Markdown by default; Google Sheets, Microsoft
  Excel, Google Docs, or Microsoft Word in a future implementation.

The formats for the remaining three document skills are forecast only. Those
placeholders contain no methodology, template, example, generator,
conversion, export, or integration.

Version 0.1 of the
[Minimal Knowledge Model](plugins/project-design/shared/knowledge-model/README.md) defines how
assertions and their epistemic state are preserved before normalization.

Version 0.1 of the
[Minimal Normalized Project Model](plugins/project-design/shared/project-model/README.md) defines the
shared current project view consumed by future skills.

The
[Canonical Domain Model](plugins/project-design/shared/terminology/canonical-domain-model.md)
defines the vocabulary shared by both models and all skills. It governs
semantics but is not an additional processing layer.

Localized terminology companions, starting with
[French canonical terminology](plugins/project-design/shared/terminology/canonical-terms.fr.md),
provide output labels without changing that semantic contract.

## Platforms

Version 0.1.0 targets Codex and Claude Code. Both platforms discover the same
`plugins/project-design/skills/` implementation. Installable manifests live
inside the plugin bundle, while platform notes and optional adapters remain
outside it under `integrations/`.

## Standalone and Spec Kit Use

The plugin is standalone by design and does not require GitHub Spec Kit. Spec Kit is an optional future companion or integration target; it does not own the methodology. See [the Spec Kit integration boundary](integrations/spec-kit/README.md).

## Repository Structure

```text
plugins/project-design/   Installable plugin bundle
  .codex-plugin/          Codex manifest
  .claude-plugin/         Claude Code manifest
  skills/                 Platform-independent skill foundations
  shared/                 Models, assets, schemas, rules, and terminology
development/              Versioned resources excluded from installation
  PROJECT_CONTEXT.md      Cross-conversation continuity
  tests/                  Fixtures, scenarios, checklists, and evidence
  examples/               Draft examples excluded from installation
  PLAN.md                 Project roadmap
  SPEC.md                 Current specification
.local/                   Ignored local and confidential working files
.agents/plugins/          Codex marketplace metadata
.claude-plugin/           Claude Code marketplace metadata
integrations/             Platform notes and optional integration boundaries
```

`_project-design/` and its `documents/` subdirectory are initialized in a
target project only after the user explicitly confirms use of the plugin for
their specifications. The guided flow stores non-business control state in
`_project-design/project-design-state.json`; it contains control counters for
active question batches but no question text, answer text, source, or Canvas
content. Initialization creates no placeholder artefact. The workspace is not
a repository-development or plugin-cache directory.

The Codex and Claude Code marketplace entries both point only to
`plugins/project-design/`. Development resources remain versioned in Git but
are not part of the installed plugin copy.

## Localization and Assets

Normative plugin source content and canonical names are English. User-facing
assets and terminology companions may be localized. Localized resources
follow `<asset-name>.<language-code>.<extension>`, with optional regional tags
such as `fr-FR`.

Resolution prefers an exact regional language and then its base language.
Missing requested-language content must be explicit. English is the default
when no output language is requested and is a fallback for a requested
language only through an explicit rule or user acceptance. Resolution must
never silently fall back to an unrelated localized language.

## Current Status

UNDER CONSTRUCTION

Version 0.1.0 provides manifests, valid skill foundations, shared-resource
placeholders, integration boundaries, repository documentation, a
documentation-first testing strategy, a permanent multi-artefact reference
corpus, the common information-architecture decision, version 0.1 of the
Canonical Domain Model, version 0.1 of the conceptual Knowledge Model, and
version 0.1 of the Minimal Normalized Project Model. It also provides the
initial French canonical terminology companion and the first complete
business methodology, `project-framing`, plus the first document methodology,
`document-project-canvas`. Its current unreleased evolution defines the
Project Canvas as the primary framing artefact and supports its verified
Markdown, Microsoft Word, or Google Docs restitution. Combined manual user
validation remains pending. It does not provide the remaining detailed skill
methodologies, complete cross-stage orchestration, general exporters, API
integrations, MCP servers, hooks, agents, commands, or Spec Kit automation.

## Development Approach

Develop one responsibility per skill, reuse shared concepts, preserve
evidence and traceability, and validate methodology before adding automation.
Every change follows [the shared testing strategy](development/tests/TESTING.md).
Combined real-project validation of `project-framing` and
`document-project-canvas` uses the
[manual test file](development/tests/manual/project-framing.md).
Development continuity between conversations is maintained in
[PROJECT_CONTEXT.md](development/PROJECT_CONTEXT.md).
Planned capability remains `TO BE DEFINED` until its behavior and contracts
are explicitly designed.

## Roadmap

1. Iteration 8 and advanced Iteration 12: `project-framing` -> Project Canvas
   -> `document-project-canvas`; combined manual validation remains pending.
2. Iteration 9: `functional-design` -> Functional Design.
3. Iteration 10: `technical-design` -> Technical Design.
4. Iteration 11: `product-backlog` -> Product Backlog.
5. Iteration 12: `document-project-canvas` implementation advanced into the
   combined Iteration 8 validation; complete that validation.
6. Iteration 13: implement `document-functional-design`.
7. Iteration 14: implement `document-technical-design`.
8. Iteration 15: implement `document-product-backlog`.
9. Iteration 16: implement complete `project-design` orchestration.

## Installation

The public GitHub repository is:

```text
JulienGlobalis/plugin_project_design
```

### Claude Code

Add the GitHub repository as a marketplace, then install the plugin:

```bash
claude plugin marketplace add JulienGlobalis/plugin_project_design
claude plugin install project-design@project-design
```

Restart Claude Code after installation. To retrieve a later release:

```bash
claude plugin marketplace update project-design
claude plugin update project-design@project-design
```

The Claude marketplace catalog is
`.claude-plugin/marketplace.json`. It points to the isolated
`plugins/project-design/` bundle, so development tests and context files are
not installed with the plugin.

### Codex

The Codex marketplace catalog is `.agents/plugins/marketplace.json`. Add the
GitHub repository as a marketplace and install the plugin with:

```bash
codex plugin marketplace add JulienGlobalis/plugin_project_design --ref main
codex plugin add project-design@project-design
```

Submission to an official vendor-managed public directory remains separate
from this independently distributed GitHub marketplace.
