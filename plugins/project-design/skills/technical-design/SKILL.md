---
name: technical-design
description: Structure the future technical design of an application or software system, including architecture, technologies, components, integrations, APIs, flows, constraints, security, performance, deployment, decisions, risks, and non-functional requirements. Use when translating a Project Canvas and known project or functional needs into technology-oriented design considerations.
---

# Technical Design

## Status

UNDER CONSTRUCTION

The detailed technical-design methodology and output templates are TO BE DEFINED.

## Purpose

Eventually describe a coherent technical direction that is traceable to the
Project Canvas and validated project or functional needs. Operate as a
complementary or parallel step to functional design when inputs permit.

## Expected Inputs

- Project Canvas, functional Requirements when available, existing system
  context, and technical Constraints.
- Known standards, integrations, non-functional needs, risks, and prior decisions.

## Expected Outputs

- A structured technical-design artefact.
- Traceable architecture, technologies, components, Integrations, APIs,
  flows, Constraints, security, performance, deployment, Decisions, Risks,
  and non-functional Requirements.

Output structures are TO BE DEFINED.

## Boundaries

- Remain independently callable without the `project-design` orchestrator.
- Remain fully usable without GitHub Spec Kit.
- Do not implement runtime code, select technologies without evidence, or define detailed methodology in this iteration.
- Keep proposals distinct from decisions.
- Do not repeat complete project framing or silently rewrite validated Canvas
  information; identify any founded adjustment for traceable upstream review.

## Shared References

- [Schemas](../../shared/schemas/README.md)
- [Project model](../../shared/project-model/README.md)
- [Quality rules](../../shared/quality-rules/README.md)
