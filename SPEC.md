# Version 0.1.0 Specification

## Iteration Objective

Initialize the plugin structure, manifests, skills, and shared-resource placeholders. Do not implement the detailed project-design methodology.

## In Scope

- Codex and Claude Code plugin manifests.
- One orchestration skill skeleton and five specialized skill skeletons.
- Shared-resource directories and conventions.
- Codex, Claude Code, and GitHub Spec Kit integration documentation.
- Repository documentation, contribution rules, and validation scope.
- A shared documentation-first testing strategy and anonymized regression
  corpus.

## Out of Scope

- Detailed project-design methodology.
- Executable workflows or generic workflow engines.
- Runtime code or language packages.
- Hooks, custom agents, slash commands, MCP servers, and API integrations.
- Exporters, persistence, and automatic document conversion.
- Spec Kit installation, commands, template changes, synchronization, or artefact conversion.

## Acceptance Criteria

- Both manifests identify `project-design` at version `0.1.0`.
- All six skills have valid front matter and distinct triggering descriptions.
- All specialized skills state that they are independently callable and do not require Spec Kit.
- Shared and platform-specific content are separated.
- Spec Kit standalone, companion, and integration modes are documented.
- No runtime dependency or detailed methodology is introduced.
- Planned behavior is marked `UNDER CONSTRUCTION` or `TO BE DEFINED`.
- Exactly four permanent anonymized, multi-artefact fixtures support shared
  Codex and Claude Code scenarios.
- Repository-wide and skill-specific quality criteria evaluate methodology
  without requiring identical wording.
- Golden outputs require explicit human approval.

## Unresolved Design

The methodology, project-information model, detailed schemas, artefact mappings, installation distribution, license, and automation implementation are TO BE DEFINED.
