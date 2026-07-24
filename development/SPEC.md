# Version 0.1.0 Specification

## Iteration Objective

Isolate the installable `project-design` bundle from versioned development
resources and ignored local work without changing the accepted methodology or
shared information architecture.

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
- An initial French terminology companion for canonical concepts and shared
  model labels.
- A complete `project-framing` methodology for concise, traceable,
  uncertainty-aware project framing.
- Four fixture scenarios, a detailed quality checklist, and a lightweight
  real-project manual test workbook for `project-framing`.
- An installable bundle under `plugins/project-design/`.
- Versioned tests, context, plans, specifications, and examples under
  `development/`.
- An ignored `.local/` directory for temporary or confidential local work.
- A repository marketplace entry pointing only to the installable bundle.

## Out of Scope

- Detailed `functional-design`, `technical-design`, `product-backlog`,
  `document-output`, and orchestration methodologies.
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
- No executable runtime or platform dependency is introduced.
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
- Localized terminology maps all canonical concepts without modifying their
  English names or definitions.
- Missing requested-language terminology is explicit and never falls back
  silently to an unrelated localized language.
- `project-framing` accepts an existing Project View or available project
  sources and remains independently callable.
- The framing output covers only justified context, objectives, Scope,
  participants, lifecycle perspectives, uncertainty, decisions, Risks,
  Issues, questions, and next steps.
- The framing distinguishes Established, Provisional, and Unresolved
  information and Existing, Target, and Transition perspectives.
- Contradictory or missing information remains visible and no unsupported
  project information is invented.
- Preliminary questions are limited to useful blockers and the user can
  continue with an incomplete framing.
- Detailed functional, technical, backlog, and document methodology remains
  outside `project-framing`.
- A concise manual workbook supports real-project validation without
  introducing a second automated suite.
- The installable bundle contains manifests, skills, shared models,
  terminology, and runtime quality contracts only.
- No installable skill or shared resource depends on `development/`.
- Tests and continuity context remain versioned without being included in the
  marketplace source path.
- The repository marketplace resolves `project-design` from
  `./plugins/project-design`.
- `.local/` is excluded from Git.

## Unresolved Design

The remaining skill methodologies, orchestration, shared-model representation
and versioning, detailed schemas, artefact mappings, external distribution,
license, and automation implementation are TO BE DEFINED.
