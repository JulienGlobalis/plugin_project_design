# Version 0.1.0 Unreleased Specification

## Iteration Objective

Implement `document-project-canvas` as the documentary counterpart of the
validated Project Canvas business artefact so `project-framing` and final
document restitution can be tested sequentially, without changing the
business methodology or the three remaining document placeholders.

## Current Capability Status

| Skill | Status in version 0.1.0 | Capability statement |
| --- | --- | --- |
| `project-design` | Installed placeholder | Forecast global orchestration only; complete routing is not implemented |
| `project-framing` | Implemented methodology version 0.2 | Produces the ten-section Project Canvas business artefact; manual user validation remains pending |
| `functional-design` | Installed placeholder | Future structured functional-design methodology |
| `technical-design` | Installed placeholder | Future complementary or parallel technical-design methodology |
| `product-backlog` | Installed placeholder | Future transformation of designed and validated Scope into traceable backlog items |
| `document-project-canvas` | Implemented methodology version 0.1 | Produces a verified Project Canvas document in native Markdown, Microsoft Word, or Google Docs |
| `document-functional-design` | Installed placeholder | Future functional specifications in Markdown, Word, or Google Docs |
| `document-technical-design` | Installed placeholder | Future technical specifications in Markdown, Word, or Google Docs |
| `document-product-backlog` | Installed placeholder | Future backlog document in Markdown, Google Sheets, Excel, Word, or Google Docs |

`project-framing` and `document-project-canvas` are implemented. Their combined
manual user validation remains pending. The other seven entries remain
architecture-stabilizing placeholders and provide no operational capability.

## In Scope

- Document global orchestration and the definitive business/document skill
  families.
- Define the discipline-neutral Shared Document Model as the common contract
  for every implemented and future document skill.
- Retain `project-design` as the future global orchestrator.
- Position `project-framing` as the first design step.
- Keep the Project Canvas as the primary `project-framing` business artefact.
- Define the ten required Canvas sections, filling rules, qualitative
  readiness, and traceable later-adjustment rules.
- Add a runtime Project Canvas reference and, when useful, a short fictional
  structural example unrelated to permanent fixtures.
- Document `functional-design` and `technical-design` as future complementary
  steps without implementing their methodologies.
- Remove the generic documentary placeholder and every active architectural
  dependency on it.
- Implement `document-project-canvas` with a default documentary structure,
  optional compatible-template handling, native Markdown, Microsoft Word, and
  Google Docs routing, content-preservation rules, and format verification.
- Keep `document-functional-design`, `document-technical-design`, and
  `document-product-backlog` as non-operational placeholders.
- Extend the four fixture scenarios and the manual replay to validate
  `project-framing` followed by `document-project-canvas`.
- Apply the mandatory `<discipline>` / `document-<discipline>` convention.
- Update repository documentation, skill descriptions, quality checklists,
  manifests, execution evidence, and continuity context.
- Preserve the isolated installable bundle and its independence from
  `development/`.

## Out of Scope

- Implementing `functional-design`, `technical-design`, `product-backlog`,
  `document-functional-design`, `document-technical-design`, or
  `document-product-backlog` methodology.
- Implementing complete `project-design` orchestration.
- Creating custom Google Docs or DOCX runtime packages, APIs, exporters, or
  bundled generators instead of using available native document tooling.
- Claiming Google Sheets or Microsoft Excel as Project Canvas output formats.
- Adding a bundled template, runtime example, script, or platform-specific
  integration to `document-project-canvas` without a demonstrated need.
- Adding methodology, templates, examples, scripts, or integrations to the
  three remaining document placeholders.
- Executable workflows, runtime code, language packages, templating engines,
  exporters, persistence, APIs, MCP servers, hooks, agents, commands, or Spec
  Kit automation.
- Changing the Information Architecture ADR, Canonical Domain Model,
  Knowledge Model, Project Model, or French canonical terminology.
- Creating, replacing, or approving Golden Outputs.
- Changing plugin version, tags, or release policy before the separate version
  governance decision.

## Project Canvas Contract

The required sections are:

1. Business Context;
2. Objectives and Expected Value;
3. Project Stakeholders;
4. Users;
5. Functional Scope with MVP, Outside MVP, and Unresolved Scope;
6. Technical Constraints;
7. Risks;
8. Decisions;
9. Questions;
10. Success Criteria.

Every section is present or explicitly states that information is missing,
contradictory, unsupported, or awaiting a Decision. The Canvas must never
invent content to appear complete.

`project-framing` owns this business artefact and no document format.
`document-project-canvas` consumes the validated artefact and produces its
verified native Markdown, Microsoft Word, or Google Docs document.

## Design and Restitution Boundary

- The
  [Shared Document Model](../plugins/project-design/shared/document-model/README.md)
  governs the common artefact-to-document contract without defining any
  discipline-specific methodology.
- Business skills produce traceable structured business or technical
  artefacts and know no document format, template, export, or presentation
  logic.
- Document skills present those validated artefacts for people or external
  tools without changing their meaning, status, Decisions, or unresolved
  questions.
- Document skills apply only a document structure, formatting, an optional
  template, and an output format.
- Markdown is the native default of every document skill.
- Project Canvas documents currently target native Markdown, Microsoft Word,
  or Google Docs through the active platform's native document tooling.
- Functional and technical specifications may later target Microsoft Word or
  Google Docs.
- Product Backlog documents may later target Google Sheets, Microsoft Excel,
  Microsoft Word, or Google Docs.
- No external document format is implemented for the three remaining document
  placeholders.

## Acceptance Criteria

- Both manifests continue to identify `project-design` at version `0.1.0`.
- All nine installed skills retain valid front matter and distinct triggering
  descriptions.
- `document-project-canvas` contains an implemented methodology and only the
  runtime references required for structure, formats, and quality.
- `document-project-canvas` explicitly references and conforms to the Shared
  Document Model without changing its methodology.
- The other three document skills remain placeholders containing only
  `SKILL.md`.
- `project-design` remains a future global orchestrator and does not duplicate
  specialized methodology.
- The former generic documentary skill directory is removed because its
  absence does not break plugin discovery or manifests.
- `project-framing` accepts an existing Project View or available project
  sources and remains independently callable.
- `project-framing` explicitly reworks and clarifies the expression of need
  rather than only summarizing sources.
- The primary output is an autonomous Project Canvas business artefact.
- The ten required sections are represented or explicitly insufficiently
  informed.
- Project Stakeholders and users remain distinct.
- MVP, Outside MVP, explicit exclusions, future Options, and unresolved Scope
  remain distinct.
- Known technical Constraints are represented without producing detailed
  technical design.
- No Objective, value claim, success criterion, threshold, MVP split,
  Requirement, Business Rule, priority, owner, date, or Decision is invented.
- Risks remain distinct from confirmed Issues.
- Decisions remain distinct from Assumptions, preferences, proposals, and
  Options.
- Established, Provisional, and Unresolved information remains distinguishable.
- Existing, Target, and Transition perspectives remain distinguishable.
- Contradictory or missing information remains visible and traceable.
- Questions are project-specific and classified as blocking, required before
  functional design, required before technical design, required before
  backlog preparation, or deferrable.
- Qualitative 80-90% reliability is not represented as a calculated score.
- The Canvas states purpose-specific readiness for downstream steps and can
  remain usable despite explicit non-blocking unknowns.
- Later Canvas adjustments must be traceable, justified, limited, and must not
  silently rewrite validated information or Decisions.
- Detailed functional, technical, backlog, and document methodology remains
  outside `project-framing`.
- `project-framing`, `functional-design`, `technical-design`, and
  `product-backlog` contain no document format, export, or template ownership.
- Project Canvas Markdown, Microsoft Word, and Google Docs are documented as
  current behavior; formats forecast for the remaining document skills remain
  explicitly non-operational.
- The combined manual test file remains one flat Markdown file, retains
  `PF-MAN-001` through `PF-MAN-005`, bilingual business and documentary
  criteria, allowed statuses, result areas, and the confidentiality rule.
- No Golden Output changes without explicit human approval.
- No installable skill or shared resource depends on `development/`.
- The Canonical Domain Model, Knowledge Model, Project Model, Information
  Architecture ADR, and French canonical terminology remain unchanged.
- No commit or push is performed.

## Open Decisions

- Whether the Unreleased changes remain in version `0.1.0` or require a new
  version.
- Which compatible template contracts will support the three remaining
  document skills and whether a branded Project Canvas template is later
  supplied.
- Which Project Canvas changes discovered downstream require a future stable
  identity or version representation.

## Validation Status

Technical implementation and fixture validation may complete in this
iteration. Full combined validation of `project-framing` and
`document-project-canvas` remains pending until the user returns the requested
manual test results.

The independent
[Plugin Architecture and Coherence Review v1.0](documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md)
confirms that no additional shared foundation is required before the
`functional-design` methodology iteration. The pending combined manual replay
remains a quality gate, not an architectural dependency.
