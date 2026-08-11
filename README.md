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
  consent, safe workspace initialization, persisted phase enforcement, stage
  selection with `project-framing` by default, and handoff. Complete
  cross-stage orchestration remains future work.
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
.agents/plugins/          Repository marketplace metadata
integrations/             Platform notes and optional integration boundaries
```

`_project-design/` and its `documents/` subdirectory are initialized in a
target project only after the user explicitly confirms use of the plugin for
their specifications. The guided flow stores non-business control state in
`_project-design/project-design-state.json`; it contains no source or Canvas
content. Initialization creates no placeholder artefact. The workspace is not
a repository-development or plugin-cache directory.

The repository marketplace points only to `plugins/project-design/`.
Development resources remain versioned in Git but are not part of the
installed plugin copy.

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
methodologies, executable orchestration, general exporters, persistence, API
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

The repository includes a local marketplace entry at
`.agents/plugins/marketplace.json`. It points to the isolated
`plugins/project-design/` bundle so development tests and context files are
not installed with the plugin.

External publication, package releases, and automated installation remain TO
BE DEFINED.
