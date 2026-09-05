# Version 0.1.0 Unreleased Specification

## Iteration Objective

Implement the guided `project-design` entry, `functional-design`, and
`document-project-canvas` as the documentary counterpart of the validated
Project Canvas business artefact. Functional Design must remain a living,
traceable business artefact, independently callable while guided routing and
the five remaining placeholders stay unchanged.

## Current Capability Status

| Skill | Status in version 0.1.0 | Capability statement |
| --- | --- | --- |
| `project-design` | Stateful guided entry version 0.5 | Presents skills, obtains consent, initializes the workspace, persists and enforces phases including pending framing answers, proposes `project-framing`, and hands off; complete routing is not implemented |
| `project-framing` | Implemented methodology version 0.6 | Produces the ten-section Project Canvas business artefact, a separate three-stage readiness assessment, and complete necessary question batches; corrective manual re-test remains pending |
| `functional-design` | Implemented methodology version 0.2 | Creates, reviews, and evolves the living `_project-design/functional-design.md` artefact from a validated Canvas and project evidence |
| `technical-design` | Installed placeholder | Future complementary or parallel technical-design methodology |
| `product-backlog` | Installed placeholder | Future transformation of designed and validated Scope into traceable backlog items |
| `document-project-canvas` | Implemented methodology version 0.2 | Produces a verified Project Canvas document in native Markdown, Microsoft Word, or Google Docs with strict reverse mapping to the supplied Canvas |
| `document-functional-design` | Installed placeholder | Future functional specifications in Markdown, Word, or Google Docs |
| `document-technical-design` | Installed placeholder | Future technical specifications in Markdown, Word, or Google Docs |
| `document-product-backlog` | Installed placeholder | Future backlog document in Markdown, Google Sheets, Excel, Word, or Google Docs |

The guided entry, `project-framing`, `functional-design`, and
`document-project-canvas` are implemented. The first framing/document
real-project replay identified and corrected defects; a focused re-test
remains pending. Functional-design fixture and manual replay are pending. The
other five entries remain architecture-stabilizing placeholders and provide
no operational capability.

## In Scope

- Document global orchestration and the definitive business/document skill
  families.
- Define the discipline-neutral Shared Document Model as the common contract
  for every implemented and future document skill.
- Implement `project-design` consent, idempotent workspace initialization,
  persistent state, phase validation, stage selection, documentary-choice
  capture, framing and approval gates, and specialized-skill handoff while
  retaining complete orchestration as future work.
- Position `project-framing` as the first design step.
- Keep the Project Canvas as the primary `project-framing` business artefact.
- Define the ten required Canvas sections, filling rules, qualitative
  readiness, and traceable later-adjustment rules.
- Add a runtime Project Canvas reference and, when useful, a short fictional
  structural example unrelated to permanent fixtures.
- Implement `functional-design` as a living business artefact with stable
  identifiers, controlled change history, actors and roles, global Processes,
  a product-module-feature inventory, detailed feature specifications,
  interfaces and fields, Business Rules, acceptance criteria, and a global
  message catalog.
- Preserve nominal, alternative valid, error, and exception behavior as
  distinct concepts; define messages once and reference them by stable ID.
- Keep `technical-design` as a future complementary step.
- Remove the generic documentary placeholder and every active architectural
  dependency on it.
- Implement `document-project-canvas` with a default documentary structure,
  optional compatible-template handling, native Markdown, Microsoft Word, and
  Google Docs routing, content-preservation rules, and format verification.
- Keep `document-functional-design`, `document-technical-design`, and
  `document-product-backlog` as non-operational placeholders.
- Extend the four fixture scenarios and add manual replay coverage for
  Functional Design creation and controlled evolution, without changing
  Golden Outputs.
- Apply the mandatory `<discipline>` / `document-<discipline>` convention.
- Update repository documentation, skill descriptions, quality checklists,
  manifests, execution evidence, and continuity context.
- Preserve the isolated installable bundle and its independence from
  `development/`.
- Require a concise pre-execution brief naming the selected skill, available
  and missing inputs, expected deliverables, and required or optional models
  or templates.
- Store every durable generated Markdown output beneath `_project-design/` at
  the root of the target project, with documentary outputs below
  `_project-design/documents/`.
- Require explicit consent before workspace initialization and create no
  placeholder output during initialization.
- Persist only workflow-control metadata in
  `_project-design/project-design-state.json`, atomically update it through the
  bundled script, reject skipped transitions, and keep all project knowledge
  out of the state file.
- Make `project-framing` present the ten Canvas chapters, resolve optional
  Word or Google Docs delivery, accept a prompt description or sources, and
  co-construct the Canvas through explicit question batches containing every
  necessary non-duplicated decision question.
- Persist question-batch control counts without business text, resume pending
  questions from the Canvas across conversations, support partial answers and
  explicit deferrals, and reject premature or ambiguous closure.
- Support the project manager with grounded recommendations, decision
  consequences, progressive responses, reused explicit setup choices, and a
  reviewable Canvas approval and next-action handoff. Keep agent proposals
  separate from authorized project decisions.
- Distinguish active and explicitly deferred questions during resumption.
- Check basic OOXML Word package structure before recording delivery, without
  replacing native rendering or semantic verification.

## Out of Scope

- Implementing `technical-design`, `product-backlog`,
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
- General-purpose workflow engines, language packages, templating engines,
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
5. Functional Scope with validated MVP and authorized Outside MVP;
6. Technical Constraints;
7. Risks;
8. Decisions;
9. Questions;
10. Success Criteria.

Every section is present. Missing validated information is `To be defined`;
an indispensable undecided scope boundary or contradiction becomes a concise
question in section 9. Proposals, normalization labels, and conflict history
remain outside the standard Canvas. After its ten numbered sections, a
mandatory unnumbered block qualifies readiness for functional design, technical
design, and backlog preparation separately. Never invent content to appear
complete.

`project-framing` owns this business artefact and no document format.
`document-project-canvas` consumes the validated artefact and produces its
verified native Markdown, Microsoft Word, or Google Docs document.

## Functional Design Contract

`functional-design` consumes a validated Project Canvas or equivalent current
project position and produces `_project-design/functional-design.md`. The
artefact contains evolution controls, Actors and roles, general
specifications, a product-module-feature inventory, one detailed section per
feature, global Business Rules, a global message catalog, and separate
technical-design and backlog-preparation readiness.

Stable project-local identifiers and cross-references survive updates.
Changes are limited to affected sections and classified as additions,
clarifications, corrections, deprecations, or replacements. The skill does
not invent missing behavior, silently change the Canvas, create technical
architecture or backlog items, or own final-document formatting.

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

- Both manifests continue to identify `project-design` with base release
  version `0.1.0`; the Codex manifest retains its existing cachebuster suffix.
- All nine installed skills retain valid front matter and distinct triggering
  descriptions.
- `document-project-canvas` contains an implemented methodology and only the
  runtime references required for structure, formats, and quality.
- `document-project-canvas` explicitly references and conforms to the Shared
  Document Model without changing its methodology.
- The other three document skills remain placeholders containing only
  `SKILL.md`.
- `functional-design` contains an implemented methodology, runtime structure,
  quality checklist, and fictional example with no runtime dependency on
  `development/`.
- Every inventory feature maps to one detailed section or a justified
  deferral, and all rule, interface, field, message, and acceptance references
  resolve through stable identifiers.
- Functional Design updates preserve unaffected meaning and identifiers while
  recording the affected IDs and known reason.
- Alternative valid scenarios remain distinct from errors and exceptions.
- Messages are defined once in the global annex catalog and referenced from
  features and fields.
- Functional Design contains no architecture, API, database schema,
  implementation task, prioritization, estimate, sprint, release plan, or
  documentary formatting.
- Technical-design and backlog-preparation readiness are assessed separately.
- `project-design` owns the guided entry and remains the future complete global
  orchestrator; it does not duplicate specialized methodology.
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
- Established, Provisional, and Unresolved information remains distinguishable
  internally and is not displayed as normalization labels in the standard Canvas.
- Existing, Target, and Transition perspectives remain distinguishable.
- Contradictory or missing information remains traceable internally and appears
  as a concise necessary decision question or `To be defined` in the Canvas.
- Questions are project-specific and classified as blocking, required before
  functional design, required before technical design, required before
  backlog preparation, or deferrable.
- Every necessary question is written to the Canvas and presented in one
  explicit batch without a numeric cap; decorative or merely generic
  questions remain excluded.
- Pending batches survive conversation changes, partial answers preserve the
  remaining questions, and only explicit deferrals reduce the pending count.
- Question, answer, and project text never enters the workflow state.
- Qualitative 80-90% reliability is not represented as a calculated score.
- The Canvas states purpose-specific readiness for downstream steps and can
  remain usable despite explicit non-blocking unknowns.
- Later Canvas adjustments must be traceable, justified, limited, and must not
  silently rewrite validated information or Decisions.
- Detailed functional, technical, backlog, and document methodology remains
  outside `project-framing`; `functional-design` owns only functional design.
- `project-framing`, `functional-design`, `technical-design`, and
  `product-backlog` contain no document format, export, or template ownership.
- Project Canvas Markdown, Microsoft Word, and Google Docs are documented as
  current behavior; formats forecast for the remaining document skills remain
  explicitly non-operational.
- The combined framing/document manual test file remains one flat Markdown file, retains
  `PF-MAN-001` through `PF-MAN-005`, bilingual business and documentary
  criteria, allowed statuses, result areas, and the confidentiality rule.
- The functional-design manual test covers all four permanent fixtures plus a
  controlled real project and includes at least one stable-ID update check.
- No Golden Output changes without explicit human approval.
- No installable skill or shared resource depends on `development/`.
- Every installed skill applies the shared invocation brief; placeholders say
  that they generate no output.
- `project-framing` targets `_project-design/project-canvas.md` for durable
  Markdown delivery.
- `document-project-canvas` targets
  `_project-design/documents/project-canvas.md` for Markdown delivery.
- Existing files are not overwritten silently, and an unavailable project
  root is reported instead of claiming a successful save.
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
