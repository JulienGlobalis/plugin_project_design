---
name: document-output
description: Plan and assemble consistent project-design documents from artefacts produced by other skills, including output language, asset selection, branding, formatting, and cross-document consistency. Use when the requested deliverable is a composed project document rather than the underlying design analysis itself.
---

# Document Output

## Status

UNDER CONSTRUCTION

The assembly process, localization resolution, templates, and exporter behavior are TO BE DEFINED.

## Purpose

Eventually assemble coherent user-facing documents while preserving source traceability and respecting language and asset conventions.

## Expected Inputs

- One or more validated project-design artefacts.
- Requested document type, output language, branding, assets, and formatting constraints.

## Expected Outputs

- A planned or assembled project document with consistent structure and terminology.
- Explicit handling of unavailable localized assets.

Output formats are TO BE DEFINED.

## Boundaries

- Remain independently callable without the `project-design` orchestrator.
- Remain fully usable without GitHub Spec Kit.
- Do not perform exports, implement localization resolution, or alter source methodology in this iteration.
- Never silently fall back to an unrelated language.

## Shared References

- [Asset conventions](../../shared/assets/README.md)
- [Quality rules](../../shared/quality-rules/README.md)
- [Terminology](../../shared/terminology/README.md)
