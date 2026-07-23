# Project Design

`project-design` is a methodology-first, Markdown-first plugin foundation for application and software project design. It is intended to make project framing, functional design, technical design, Product Backlog preparation, and document assembly modular, reusable, and traceable.

## Problem Addressed

Project-design knowledge is often spread across briefs, workshops, requirements, architecture notes, and delivery tools. This plugin will provide a shared project-information model and focused skills without coupling the methodology to one AI agent, document format, or orchestration framework.

## Architecture

The plugin contains one future orchestration skill and five specialized skills:

- `project-design` will select and coordinate specialized skills.
- `project-framing` will structure project context and boundaries.
- `functional-design` will structure expected system behavior.
- `technical-design` will structure architecture and technical decisions.
- `product-backlog` will structure and harmonize backlog items.
- `document-output` will assemble consistent project documents.

Each specialized skill is independently callable. Users will be able to request a complete workflow, one skill, or an explicit subset of skills.

## Platforms

Version 0.1.0 targets Codex and Claude Code. Both platforms discover the same root `skills/` implementation. Platform-specific manifests and notes are isolated under `.codex-plugin/`, `.claude-plugin/`, and `integrations/`.

## Standalone and Spec Kit Use

The plugin is standalone by design and does not require GitHub Spec Kit. Spec Kit is an optional future companion or integration target; it does not own the methodology. See [the Spec Kit integration boundary](integrations/spec-kit/README.md).

## Repository Structure

```text
.codex-plugin/       Codex manifest
.claude-plugin/      Claude Code manifest
skills/              Shared, platform-independent skill foundations
shared/              Shared assets, schemas, project model, rules, and terms
integrations/        Platform notes and optional integration boundaries
examples/            Future examples
tests/               Validation scope and future tests
```

## Localization and Assets

All plugin source content is English. Only user-facing assets may be localized. Localized assets follow `<asset-name>.<language-code>.<extension>`, with optional regional tags such as `fr-FR`. Resolution must never silently fall back to an unrelated language.

## Current Status

UNDER CONSTRUCTION

Version 0.1.0 provides manifests, valid skill skeletons, shared-resource placeholders, integration boundaries, and repository documentation. It does not provide the detailed methodology, executable workflows, exporters, persistence, API integrations, MCP servers, hooks, agents, commands, or Spec Kit automation.

## Development Approach

Develop one responsibility per skill, reuse shared concepts, preserve evidence and traceability, and validate methodology before adding automation. Planned capability remains `TO BE DEFINED` until its behavior and contracts are explicitly designed.

## Roadmap

The next iteration is limited to defining and testing `project-framing`. Later iterations may define the remaining specialized skills, the shared project model, orchestration, document outputs, and optional adapters.

## Installation

Installation and distribution are TO BE DEFINED. The repository has valid local plugin manifests but no marketplace entry, package release, or automated installer in version 0.1.0.
