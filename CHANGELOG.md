# Changelog

## Unreleased

- Added the documentation-first testing strategy.
- Added four fictional, fully anonymized, multi-artefact permanent regression
  fixtures representing realistic consulting inputs.
- Added shared scenarios for Codex and Claude Code.
- Added repository-wide and skill-specific quality checklists.
- Added golden-output governance, regression classification, release
  validation, and execution-history conventions.
- Accepted the layered Source Documents, Knowledge Model, Project Model, and
  Generated Artefacts information architecture.
- Defined version 0.1 of the corpus-driven Canonical Domain Model with 22
  shared concepts and explicit exclusions.
- Defined version 0.1 of the Minimal Knowledge Model for assertions,
  provenance, epistemic state, contradiction, coexistence, and traceability.
- Defined version 0.1 of the Minimal Normalized Project Model with shared
  elements, relationships, normalization status, lifecycle perspective, and
  Knowledge Model traceability.
- Added the initial French terminology companion for all canonical concepts,
  shared-model labels, and localization fallback rules.
- Implemented `project-framing` methodology version 0.1 with proportionate
  questioning, uncertainty-aware framing, lifecycle separation, traceable
  outputs, four fixture validations, and a real-project manual test workbook.
- Isolated the installable plugin under `plugins/project-design/`, moved
  versioned development resources under `development/`, added an ignored
  `.local/` workspace, and added a repository marketplace entry.
- Made runtime quality contracts self-contained so the installed plugin no
  longer depends on fixtures or development checklists.
- Added a cross-conversation project context and simplified manual tests to
  one Markdown file per skill.
- Defined the boundary between development examples and approved skill
  references used at runtime.
- Expanded the cross-conversation context with the prompt history, future
  roadmap, deferred decisions, and runtime-example policy.

## Version 0.1.0 - 2026-07-23

- Added the initial plugin structure.
- Added the Codex manifest.
- Added the Claude Code manifest.
- Added the initial orchestration and specialized skill scaffolding.
- Added shared-resource placeholders and conventions.
- Added Spec Kit integration placeholders and architectural boundaries.
