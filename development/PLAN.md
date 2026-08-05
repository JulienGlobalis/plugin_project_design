# Project Design Plan

## Vision

Provide a reusable, evidence-aware methodology for designing application and
software projects across AI coding agents, orchestration frameworks,
documentation systems, and project-management platforms.

## Architectural Principles

- Keep methodology independent from platforms and output formats.
- Keep one clear responsibility per specialized skill.
- Separate design knowledge from document restitution.
- Share project concepts, terminology, assets, and quality rules.
- Support complete and partial workflows.
- Preserve traceability between facts, interpretations, assumptions,
  proposals, decisions, and open questions.
- Separate source documents, extracted knowledge, normalized project
  information, and generated artefacts.
- Use one canonical vocabulary across shared models and skills.
- Keep English canonical names stable while allowing governed localized
  presentation labels.
- Keep the installable plugin bundle physically isolated from versioned
  development resources and ignored local work.
- Prefer Markdown, YAML, and JSON until executable behavior is justified.
- Isolate optional integrations so dependencies point toward external
  platforms, never into the core.

## Responsibility Levels

### Global Orchestration

- `project-design`: future orchestration, routing, artefact transmission, and
  cross-step consistency without duplicating specialized methodology.

### Design Skills

- `project-framing`: implemented step 1; clarifies the expression of need and
  produces the Project Canvas.
- `functional-design`: future step 2; products or applications, modules,
  features, users, Processes, journeys, Business Rules, functional data,
  exceptions, dependencies, and remaining functional questions.
- `technical-design`: future step 2 bis; architecture, technologies,
  components, Integrations, APIs, flows, Constraints, security, performance,
  deployment, technical Decisions, and technical Risks. It may complement or
  run in parallel with functional design when inputs permit.
- `product-backlog`: future transformation of designed and validated Scope
  into a traceable backlog without inventing requirements, priority, value,
  effort, or Decisions.

### Document Restitution Skills

- `document-functional-design`: future Markdown output by default, with
  template-based Google Docs or Microsoft Word as optional future targets.
- `document-technical-design`: future Markdown output by default, with
  template-based Google Docs or Microsoft Word as optional future targets.
- `document-product-backlog`: future Markdown or Google Sheets-oriented
  restitution, with other template-based document formats only when justified.
- `document-output`: existing placeholder provisionally retained as a future
  documentary orchestrator. Its necessity must be confirmed after the first
  document-specific skills provide usage evidence.

Only existing skills are implemented or scaffolded. Do not add empty skill
directories merely to mirror this forecast architecture.

## Design Sequence

```text
project-framing -> Project Canvas
                       |
                       +-> functional-design --------+
                       |                             |
                       +-> technical-design ---------+-> product-backlog
                                                     |
                                                     v
                                          document restitution
```

Functional and technical design are complementary. Their exact execution
order depends on the available information and must preserve traceable Canvas
adjustments rather than silently rewriting validated framing.

## Usage Modes

The plugin will support standalone use, optional preparation alongside GitHub
Spec Kit, and a future isolated Spec Kit adapter. It will also support one
skill, several selected skills, or a complete orchestrated workflow.

## Extension Points

Future extension points include runtime helpers, persistence, exporters,
APIs, MCP integrations, agent adapters, Spec Kit, Jira, GitHub, GitLab,
Google Docs, Google Sheets, Word, PDF, PowerPoint, Notion, and Confluence.

These extension points are not implemented in version 0.1.0 and must not
force a reorganization of the shared skills.

## Testing Strategy

All skill development uses the shared fixtures, scenarios, quality
checklists, Golden Output policy, and regression workflow defined in
[`tests/TESTING.md`](tests/TESTING.md). A methodology change is incomplete
until its affected tests have been updated and reviewed.

## Roadmap

1. Establish the repository testing strategy.
2. Build the permanent anonymized reference corpus.
3. Decide the shared information architecture.
4. Define and validate the Canonical Domain Model.
5. Define and test the minimal Knowledge Model.
6. Define and test the minimal normalized Project Model.
7. Define and test the initial `project-framing` methodology.
8. Isolate the installable bundle from tests and development context.
9. Revise `project-framing` around the Project Canvas and complete manual user
   validation.
10. Define and test `functional-design`.
11. Define and test `technical-design` as a complementary or parallel step.
12. Define and test `product-backlog`.
13. Define the three document-specific restitution skills and decide whether
   `document-output` remains their orchestrator.
14. Define global orchestration and cross-artefact consistency.
15. Design optional platform and Spec Kit adapters.
16. Consider automation only after stable contracts exist.
