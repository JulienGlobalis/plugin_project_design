# Project Design Plan

## Vision

Provide a reusable, evidence-aware methodology for designing application and
software projects across AI coding agents, orchestration frameworks,
documentation systems, and project-management platforms.

The consolidated current architecture is documented in the
[Plugin Architecture Overview v1.0](documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md).

## Architectural Principles

- Keep methodology independent from platforms and output formats.
- Keep one clear responsibility per specialized skill.
- Separate design knowledge from document restitution.
- Use the Shared Document Model as the discipline-neutral contract for every
  documentary restitution skill.
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

## Responsibility Families

### Global Orchestration

- `project-design`: installed placeholder for future orchestration, routing,
  artefact transmission, cross-step consistency, and traceable returns to an
  earlier stage when reliable new information appears. Full orchestration is
  not implemented. It produces neither business content nor documents and
  must not duplicate specialized methodology.

### Business Skills

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
  into a traceable Product Backlog artefact containing supported Epics,
  Features, User Stories, technical tasks, dependencies, increments, and
  methodological organization without inventing requirements, priority,
  value, effort, or Decisions.

Business skills own project knowledge. They produce business artefacts only.
They do not generate final documents, know output formats, apply templates,
perform exports, or contain presentation logic.

### Document Skills

- `document-project-canvas`: implemented Project Canvas documentary
  restitution in native Markdown, Microsoft Word, or Google Docs from the
  validated business artefact.
- `document-functional-design`: future functional specifications in Markdown,
  Microsoft Word, or Google Docs.
- `document-technical-design`: future technical specifications in Markdown,
  Microsoft Word, or Google Docs.
- `document-product-backlog`: future backlog document in Markdown, Google
  Sheets, Microsoft Excel, Microsoft Word, or Google Docs.

`project-framing` has an implemented business methodology and
`document-project-canvas` has an implemented documentary methodology. Their
combined manual validation remains pending. The other seven installed entries
are placeholders or under-construction contracts. Document skills consume
their corresponding business artefacts and apply only document structure,
formatting, an optional template, and an output format. They add no knowledge
and make no Decisions.

All implemented and future document skills must conform to the bundle-owned
[Shared Document Model](../plugins/project-design/shared/document-model/README.md).

The naming convention is mandatory:

```text
<discipline>           -> business artefact
document-<discipline>  -> corresponding document
```

## Design Sequence

```text
project-framing -> Project Canvas artefact -> document-project-canvas
                       |
                       +-> functional-design -> Functional Design artefact
                       |                          -> document-functional-design
                       |
                       +-> technical-design -> Technical Design artefact
                       |                         -> document-technical-design
                       |
                       +-> product-backlog -> Product Backlog artefact
                                             -> document-product-backlog
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
9. Iteration 8: implement `project-framing` and the Project Canvas artefact;
   combine its manual user validation with the advanced
   `document-project-canvas` implementation.
10. Iteration 9: define and test `functional-design` and its Functional Design
    artefact.
11. Iteration 10: define and test `technical-design` and its Technical Design
    artefact as a complementary or parallel step.
12. Iteration 11: define and test `product-backlog` and its Product Backlog
    artefact.
13. Iteration 12: implementation advanced into the combined Iteration 8
    validation; complete validation of `document-project-canvas`.
14. Iteration 13: define and test `document-functional-design`.
15. Iteration 14: define and test `document-technical-design`.
16. Iteration 15: define and test `document-product-backlog`.
17. Iteration 16: define global `project-design` orchestration and
    cross-artefact consistency after specialized contracts are stable.
