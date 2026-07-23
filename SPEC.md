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
- An evidence-aware common information-architecture decision.
- A minimal Canonical Domain Model shared by future models and skills.
- A minimal conceptual Knowledge Model for assertions, provenance, epistemic
  state, and inter-assertion relationships.
- A minimal normalized Project Model for coherent project elements,
  relationships, normalization status, lifecycle perspective, and Knowledge
  Model traceability.

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
- Source documents, extracted knowledge, normalized project information, and
  generated artefacts have distinct responsibilities.
- The accepted architecture preserves end-to-end provenance without coupling
  shared models to a skill, platform, or Spec Kit.
- Canonical concepts are justified by the permanent corpus or cross-skill
  responsibility.
- The Canonical Domain Model defines vocabulary and relationships without
  implementing knowledge state, project instances, schemas, or methodology.
- The Knowledge Model preserves assertions, provenance, confidence,
  uncertainty, validation, contradictions, and coexistence without
  normalizing project truth.
- Knowledge Model constructions reuse the unchanged Canonical Domain Model
  and remain independent from storage, platform, methodology, and
  serialization.
- The Project Model consolidates knowledge into canonical project elements
  and relationships without copying every assertion.
- Established, Provisional, and Unresolved normalized information remains
  distinguishable from Knowledge Model validation and confidence.
- Existing, Target, and Transition perspectives can coexist in one current
  Project View.
- Every material normalized element and relationship remains traceable to
  supporting, qualifying, and opposing knowledge.
- The Project Model remains independent from skill methodology, storage,
  platform, and serialization.

## Unresolved Design

The skill methodologies, shared-model representation and versioning, detailed
schemas, artefact mappings, installation distribution, license, and
automation implementation are TO BE DEFINED.
