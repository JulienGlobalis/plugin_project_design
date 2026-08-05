# Project Design

`project-design` is a methodology-first, Markdown-first plugin foundation for
application and software project design. It separates the production of
project knowledge from its documentary restitution so framing, functional
design, technical design, Product Backlog preparation, and document delivery
remain modular, reusable, and traceable.

## Problem Addressed

Project-design knowledge is often spread across briefs, workshops, requirements, architecture notes, and delivery tools. This plugin will provide a shared information architecture and focused skills without coupling the methodology to one AI agent, document format, or orchestration framework.

## Architecture

The target architecture distinguishes global orchestration, design skills,
and document-restitution skills.

- `project-design` will select and coordinate the necessary design and
  restitution steps without duplicating their methodologies.
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
- `document-functional-design`, `document-technical-design`, and
  `document-product-backlog` are future document-specific restitution skills.
- `document-output` is provisionally retained as their possible documentary
  orchestrator; this responsibility remains to be confirmed through usage.

Only the six existing skill directories are currently present. Future skills
are documented without empty scaffolding. Every specialized skill remains
independently callable, and future orchestration must preserve direct use.

### Current Availability

| Skill | Installed entry | Current status | Current or forecast responsibility |
| --- | --- | --- | --- |
| `project-design` | Yes | Placeholder | Future global orchestration; full routing is not implemented |
| `project-framing` | Yes | Implemented; manual user validation pending | Step 1; produces the Markdown Project Canvas |
| `functional-design` | Yes | Placeholder | Future structured functional-design methodology |
| `technical-design` | Yes | Placeholder | Future complementary or parallel technical-design methodology |
| `product-backlog` | Yes | Placeholder | Future traceable transformation of designed and validated Scope |
| `document-output` | Yes | Provisional placeholder | Possible future documentary orchestrator; necessity remains undecided |
| `document-functional-design` | No | Future | Document restitution from the functional-design artefact |
| `document-technical-design` | No | Future | Document restitution from the technical-design artefact |
| `document-product-backlog` | No | Future | Document restitution from the Product Backlog artefact |

An installed placeholder is discoverable but does not provide the future
methodology. The manifests expose only the six installed entries; they do not
make the three future document-specific skills available.

```text
project-design
├── project-framing
├── functional-design
├── technical-design
├── product-backlog
├── document-output                  # provisional future orchestrator
├── document-functional-design       # future
├── document-technical-design        # future
└── document-product-backlog         # future
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

Design skills own the structured project knowledge they produce. Document
skills may present a validated artefact for people or external tools, but
must not invent content, resolve a business question, change a Decision, or
become owners of design methodology.

Markdown is the native default. Google Docs, Google Sheets, and Microsoft
Word are not currently implemented output capabilities. The forecast rules
are:

- `document-functional-design`: Markdown by default; Google Docs or Microsoft
  Word only in a future implementation when a compatible template is
  supplied;
- `document-technical-design`: the same future format rule for the technical
  artefact;
- `document-product-backlog`: Markdown by default; Google Sheets only in a
  future implementation when a compatible template is supplied; Google Docs
  or Microsoft Word only for an explicitly requested documentary form with a
  compatible template.

The current minimal Project Canvas option is direct Markdown production by
`project-framing`. A future `document-project-canvas` could isolate Google
Docs or Microsoft Word restitution, but no such skill exists and the decision
is deliberately deferred until concrete format workflows provide evidence.

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
business methodology, `project-framing`. Its current unreleased evolution
defines the Project Canvas as the primary framing artefact and awaits manual
user validation. It does not provide the remaining detailed skill
methodologies, documentary skills, executable orchestration, schemas,
exporters, persistence, API integrations, MCP servers, hooks, agents,
commands, or Spec Kit automation.

## Development Approach

Develop one responsibility per skill, reuse shared concepts, preserve
evidence and traceability, and validate methodology before adding automation.
Every change follows [the shared testing strategy](development/tests/TESTING.md).
Real-project validation of `project-framing` uses the
[manual test file](development/tests/manual/project-framing.md).
Development continuity between conversations is maintained in
[PROJECT_CONTEXT.md](development/PROJECT_CONTEXT.md).
Planned capability remains `TO BE DEFINED` until its behavior and contracts
are explicitly designed.

## Roadmap

1. Complete manual user validation of revised Iteration 8
   `project-framing` and its Project Canvas.
2. Iteration 9: implement `functional-design`.
3. Iteration 10: implement `technical-design` as step 2 bis, complementary,
   parallel, or iterative with functional design according to available
   inputs.
4. Iteration 11: implement `product-backlog` from designed and validated
   Scope.
5. Run separate document iterations for `document-functional-design`,
   `document-technical-design`, and `document-product-backlog`; do not assume
   that their format and template complexity is identical.
6. Experiment with and decide the exact role of `document-output`, the
   possible need for `document-project-canvas`, and the boundary between
   documentary and global orchestration.
7. Implement complete `project-design` orchestration only after specialized
   skill contracts are sufficiently stable.
8. Design optional adapters and structural automation after the methodologies
   and document contracts are stable.

## Installation

The repository includes a local marketplace entry at
`.agents/plugins/marketplace.json`. It points to the isolated
`plugins/project-design/` bundle so development tests and context files are
not installed with the plugin.

External publication, package releases, and automated installation remain TO
BE DEFINED.
