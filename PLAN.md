# Project Design Plan

## Vision

Provide a reusable, evidence-aware methodology for designing application and software projects across AI coding agents, orchestration frameworks, documentation systems, and project-management platforms.

## Architectural Principles

- Keep methodology independent from platforms and output formats.
- Keep one clear responsibility per specialized skill.
- Share project concepts, terminology, assets, and quality rules.
- Support complete and partial workflows.
- Preserve traceability between facts, interpretations, assumptions, proposals, decisions, and open questions.
- Separate source documents, extracted knowledge, normalized project
  information, and generated artefacts.
- Use one canonical vocabulary across shared models and skills.
- Prefer Markdown, YAML, and JSON until executable behavior is justified.
- Isolate optional integrations so dependencies point toward external platforms, never into the core.

## Skill Set

- `project-design`: orchestration and consistency.
- `project-framing`: context, objectives, scope, stakeholders, constraints, risks, assumptions, and questions.
- `functional-design`: actors, modules, features, journeys, rules, requirements, and acceptance criteria.
- `technical-design`: architecture, components, flows, integrations, decisions, risks, and non-functional requirements.
- `product-backlog`: backlog structure, harmonization, prioritization, estimation, and traceability.
- `document-output`: document assembly, language, assets, branding, formatting, and consistency.

Detailed methodology for every skill is TO BE DEFINED.

## Usage Modes

The plugin will support standalone use, optional preparation alongside GitHub Spec Kit, and a future isolated Spec Kit adapter. It will also support one skill, several selected skills, or a complete orchestrated workflow.

## Extension Points

Future extension points include runtime helpers, persistence, exporters, APIs, MCP integrations, agent adapters, Spec Kit, Jira, GitHub, GitLab, Google Docs, Google Sheets, Word, PDF, PowerPoint, Notion, and Confluence.

These extension points are not implemented in version 0.1.0 and must not force a reorganization of the shared skills.

## Testing Strategy

All skill development uses the shared fixtures, scenarios, quality checklists,
golden-output policy, and regression workflow defined in
[`tests/TESTING.md`](tests/TESTING.md). A methodology change is incomplete
until its affected tests have been updated and reviewed.

## Roadmap

1. Establish the repository testing strategy.
2. Build the permanent anonymized reference corpus.
3. Decide the shared information architecture.
4. Define and validate the Canonical Domain Model.
5. Implement and test the minimal Knowledge Model.
6. Implement and test the normalized Project Model and quality-rule contracts.
7. Define and test `project-framing`.
8. Define and test the remaining specialized skills individually.
9. Define orchestration and cross-artefact consistency.
10. Validate document-output conventions and localized assets.
11. Design optional platform and Spec Kit adapters.
12. Consider automation only after stable contracts exist.
