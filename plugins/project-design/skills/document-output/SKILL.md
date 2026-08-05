---
name: document-output
description: Provisionally coordinate future document-specific project-design restitution from validated domain artefacts, including document routing, output language, asset selection, branding, formatting, and cross-document consistency. Use only for composed project-document concerns rather than the underlying framing, functional, technical, or backlog analysis.
---

# Document Output

## Status

UNDER CONSTRUCTION - provisional responsibility

The need for a generic documentary orchestrator, its routing, template
contracts, localization resolution, and exporter behavior are TO BE DEFINED.

## Purpose

Potentially coordinate future document-specific restitution while preserving
source meaning, status, traceability, language, assets, and cross-document
consistency.

The current recommendation is provisional. Reassess this skill after
`document-functional-design`, `document-technical-design`, and
`document-product-backlog` provide concrete usage evidence. Direct invocation
of those future skills must remain possible.

## Expected Inputs

- One or more validated Project Canvas, functional-design, technical-design,
  or Product Backlog artefacts.
- Requested document type, output language, branding, assets, and formatting constraints.

## Expected Outputs

- Future routing to the applicable document-specific skill and a consistent
  cross-document presentation plan.
- Explicit handling of unavailable localized assets.

Output formats are TO BE DEFINED.

## Boundaries

- Remain independently callable without the `project-design` orchestrator.
- Remain fully usable without GitHub Spec Kit.
- Do not perform exports, implement localization resolution, or alter source methodology in this iteration.
- Never silently fall back to an unrelated language.
- Do not invent, reinterpret, or modify business or technical content owned by
  design skills.

## Shared References

- [Asset conventions](../../shared/assets/README.md)
- [Quality rules](../../shared/quality-rules/README.md)
- [Terminology](../../shared/terminology/README.md)
