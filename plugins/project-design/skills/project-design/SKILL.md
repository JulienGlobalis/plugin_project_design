---
name: project-design
description: Coordinate a complete or partial application and software project-design effort across the plugin's specialized skills. Use when a request spans multiple design concerns, requires an execution order, or needs consistent framing, functional, technical, backlog, and document outputs. Do not use for a single specialized concern when one dedicated skill is sufficient.
---

# Project Design

## Status

UNDER CONSTRUCTION

Only the forecast orchestration contract is defined in version 0.1.0.
Detailed routing and methodology are TO BE DEFINED.

## Purpose

Eventually analyze a project-design request, select the required specialized
skills, transmit their artefacts, order or parallelize their use, and preserve
global consistency without duplicating their methodology.

Support three invocation patterns:

- A complete `project-design` workflow.
- One independently invoked specialized skill.
- Several specialized skills explicitly selected by the user.

## Expected Inputs

- A project request, source material, or existing project artefacts.
- The desired scope, selected skills, constraints, and output expectations when known.
- Explicit facts, assumptions, decisions, and open questions when available.

## Expected Outputs

- A proposed set and order of specialized skills.
- A consistent collection of project artefacts produced by those skills.
- Traceability between shared facts, assumptions, decisions, and open questions.

Output structures are TO BE DEFINED.

## Boundaries

- Keep specialized methodology inside the corresponding specialized skill.
- Do not require GitHub Spec Kit or any agent-specific runtime.
- Do not execute workflows, convert artefacts, persist project state, or invoke external systems in this iteration.
- Do not invent unsupported project information.

## Forecast Routing

The intended design sequence is:

1. `project-framing` produces the Project Canvas.
2. `functional-design` and `technical-design` consume it as complementary
   steps and may run in parallel when inputs permit.
3. `product-backlog` transforms designed and validated Scope.
4. Future document-specific skills restitute the validated domain artefacts.

`document-output` is provisionally retained as a possible documentary
orchestrator. Future `document-functional-design`,
`document-technical-design`, and `document-product-backlog` skills may also be
invoked directly. Do not implement this routing in the current version.

## Shared References

- [Project model](../../shared/project-model/README.md)
- [Quality rules](../../shared/quality-rules/README.md)
- [Terminology](../../shared/terminology/README.md)
- [Spec Kit boundary](../../shared/spec-kit-boundary.md)
