# Project Design

`project-design` is a methodology-first, Markdown-first plugin foundation for application and software project design. It is intended to make project framing, functional design, technical design, Product Backlog preparation, and document assembly modular, reusable, and traceable.

## Problem Addressed

Project-design knowledge is often spread across briefs, workshops, requirements, architecture notes, and delivery tools. This plugin will provide a shared information architecture and focused skills without coupling the methodology to one AI agent, document format, or orchestration framework.

## Architecture

The plugin contains one future orchestration skill and five specialized
skills:

- `project-design` will select and coordinate specialized skills.
- `project-framing` structures project context, objectives, boundaries,
  participants, uncertainty, and next clarification activities.
- `functional-design` will structure expected system behavior.
- `technical-design` will structure architecture and technical decisions.
- `product-backlog` will structure and harmonize backlog items.
- `document-output` will assemble consistent project documents.

Each specialized skill is independently callable. Users will be able to request a complete workflow, one skill, or an explicit subset of skills.

All skills will rely on the accepted
[common information architecture](plugins/project-design/shared/project-model/information-architecture.md):

```text
Source documents -> Knowledge Model -> Project Model -> Skills -> Generated artefacts
```

The Knowledge Model preserves extracted evidence, provenance, uncertainty,
and conflicts. The Project Model provides normalized project information.
Neither model belongs to an individual skill.

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
  examples/               Future development examples
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

Version 0.1.0 provides manifests, valid skill skeletons, shared-resource
placeholders, integration boundaries, repository documentation, a
documentation-first testing strategy, a permanent multi-artefact reference
corpus, the common information-architecture decision, version 0.1 of the
Canonical Domain Model, version 0.1 of the conceptual Knowledge Model, and
version 0.1 of the Minimal Normalized Project Model. It also provides the
initial French canonical terminology companion and the first complete
business methodology, `project-framing` version 0.1. It does not provide the
remaining detailed skill methodologies, executable orchestration, schemas,
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

The next business iteration should implement `functional-design`, consuming
validated project framing and the shared Project Model without duplicating
the framing methodology.

## Installation

The repository includes a local marketplace entry at
`.agents/plugins/marketplace.json`. It points to the isolated
`plugins/project-design/` bundle so development tests and context files are
not installed with the plugin.

External publication, package releases, and automated installation remain TO
BE DEFINED.
