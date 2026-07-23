# Project Design

`project-design` is a methodology-first, Markdown-first plugin foundation for application and software project design. It is intended to make project framing, functional design, technical design, Product Backlog preparation, and document assembly modular, reusable, and traceable.

## Problem Addressed

Project-design knowledge is often spread across briefs, workshops, requirements, architecture notes, and delivery tools. This plugin will provide a shared information architecture and focused skills without coupling the methodology to one AI agent, document format, or orchestration framework.

## Architecture

The plugin contains one future orchestration skill and five specialized skills:

- `project-design` will select and coordinate specialized skills.
- `project-framing` will structure project context and boundaries.
- `functional-design` will structure expected system behavior.
- `technical-design` will structure architecture and technical decisions.
- `product-backlog` will structure and harmonize backlog items.
- `document-output` will assemble consistent project documents.

Each specialized skill is independently callable. Users will be able to request a complete workflow, one skill, or an explicit subset of skills.

All skills will rely on the accepted
[common information architecture](shared/project-model/information-architecture.md):

```text
Source documents -> Knowledge Model -> Project Model -> Skills -> Generated artefacts
```

The Knowledge Model preserves extracted evidence, provenance, uncertainty,
and conflicts. The Project Model provides normalized project information.
Neither model belongs to an individual skill.

Version 0.1 of the
[Minimal Knowledge Model](shared/knowledge-model/README.md) defines how
assertions and their epistemic state are preserved before normalization.

Version 0.1 of the
[Minimal Normalized Project Model](shared/project-model/README.md) defines the
shared current project view consumed by future skills.

The
[Canonical Domain Model](shared/terminology/canonical-domain-model.md)
defines the vocabulary shared by both models and all skills. It governs
semantics but is not an additional processing layer.

## Platforms

Version 0.1.0 targets Codex and Claude Code. Both platforms discover the same root `skills/` implementation. Platform-specific manifests and notes are isolated under `.codex-plugin/`, `.claude-plugin/`, and `integrations/`.

## Standalone and Spec Kit Use

The plugin is standalone by design and does not require GitHub Spec Kit. Spec Kit is an optional future companion or integration target; it does not own the methodology. See [the Spec Kit integration boundary](integrations/spec-kit/README.md).

## Repository Structure

```text
.codex-plugin/       Codex manifest
.claude-plugin/      Claude Code manifest
skills/              Shared, platform-independent skill foundations
shared/              Shared models, assets, schemas, rules, and terms
integrations/        Platform notes and optional integration boundaries
examples/            Future examples
tests/               Shared fixtures, scenarios, checklists, and regression evidence
```

## Localization and Assets

All plugin source content is English. Only user-facing assets may be localized. Localized assets follow `<asset-name>.<language-code>.<extension>`, with optional regional tags such as `fr-FR`. Resolution must never silently fall back to an unrelated language.

## Current Status

UNDER CONSTRUCTION

Version 0.1.0 provides manifests, valid skill skeletons, shared-resource
placeholders, integration boundaries, repository documentation, a
documentation-first testing strategy, a permanent multi-artefact reference
corpus, the common information-architecture decision, version 0.1 of the
Canonical Domain Model, version 0.1 of the conceptual Knowledge Model, and
version 0.1 of the Minimal Normalized Project Model. It does not provide the
detailed skill methodologies, executable workflows, schemas, exporters,
persistence, API integrations, MCP servers, hooks, agents, commands, or Spec
Kit automation.

## Development Approach

Develop one responsibility per skill, reuse shared concepts, preserve evidence and traceability, and validate methodology before adding automation. Every change follows [the shared testing strategy](tests/TESTING.md). Planned capability remains `TO BE DEFINED` until its behavior and contracts are explicitly designed.

## Roadmap

The next iteration implements and validates the first complete methodology,
`project-framing`, using the Canonical Domain Model, Knowledge Model, and
Project Model as its architectural foundations.

## Installation

Installation and distribution are TO BE DEFINED. The repository has valid local plugin manifests but no marketplace entry, package release, or automated installer in version 0.1.0.
