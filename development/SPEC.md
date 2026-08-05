# Version 0.1.0 Unreleased Specification

## Iteration Objective

Specify the current and forecast skill architecture after the Project Canvas
evolution, distinguish implemented behavior from placeholders and future
skills, and define the boundary between design artefacts and their eventual
document restitution without changing the implemented `project-framing`
methodology.

## Current Capability Status

| Skill | Status in version 0.1.0 | Capability statement |
| --- | --- | --- |
| `project-design` | Installed placeholder | Forecast global orchestration only; complete routing is not implemented |
| `project-framing` | Implemented methodology version 0.2 | Produces the ten-section Markdown Project Canvas; manual user validation remains pending |
| `functional-design` | Installed placeholder | Future structured functional-design methodology |
| `technical-design` | Installed placeholder | Future complementary or parallel technical-design methodology |
| `product-backlog` | Installed placeholder | Future transformation of designed and validated Scope into traceable backlog items |
| `document-output` | Installed provisional placeholder | Possible future documentary orchestration; long-term necessity is undecided |

`document-functional-design`, `document-technical-design`, and
`document-product-backlog` are documented future skills. They are not
installed, scaffolded, or operational.

## In Scope

- Document the three responsibility levels: global orchestration, design
  skills, and document-restitution skills.
- Retain `project-design` as the future global orchestrator.
- Position `project-framing` as the first design step.
- Make Markdown Project Canvas the primary `project-framing` artefact.
- Define the ten required Canvas sections, filling rules, qualitative
  readiness, and traceable later-adjustment rules.
- Add a runtime Project Canvas reference and, when useful, a short fictional
  structural example unrelated to permanent fixtures.
- Document `functional-design` and `technical-design` as future complementary
  steps without implementing their methodologies.
- Document future `document-functional-design`,
  `document-technical-design`, and `document-product-backlog` responsibilities
  without creating empty skill scaffolding.
- Evaluate and document the provisional future role of `document-output`.
- Document the current direct Markdown restitution of the Project Canvas and
  the undecided future `document-project-canvas` option without creating it.
- Update repository documentation, skill descriptions, scenarios, quality
  checklists, manual tests, execution evidence, and continuity context.
- Re-run `project-framing` against exactly four permanent fixtures.
- Preserve the isolated installable bundle and its independence from
  `development/`.

## Out of Scope

- Implementing `functional-design`, `technical-design`, `product-backlog`, or
  any document-specific skill.
- Implementing complete `project-design` or `document-output` orchestration.
- Creating Google Docs, Google Sheets, or DOCX integrations or generators.
- Claiming Google Docs, Google Sheets, or Microsoft Word as currently
  supported output formats.
- Creating empty future-skill directories.
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

`project-framing` currently produces this business artefact directly in
Markdown. It owns framing content, not general document conversion. A future
`document-project-canvas` may be evaluated for Google Docs or Microsoft Word
restitution, but is neither decided nor implemented.

## Design and Restitution Boundary

- Design skills produce traceable structured business or technical
  artefacts.
- Document skills present those validated artefacts for people or external
  tools without changing their meaning, status, Decisions, or unresolved
  questions.
- Markdown is the native default format.
- Future Google Docs or Microsoft Word restitution for functional and
  technical design requires a supplied compatible template.
- Future Google Sheets restitution for the Product Backlog requires a
  supplied compatible template. Google Docs or Microsoft Word are considered
  only for an explicitly requested documentary form with a compatible
  template.
- No external document format is an implemented version 0.1.0 capability.

## Acceptance Criteria

- Both manifests continue to identify `project-design` at version `0.1.0`.
- All six existing skills retain valid front matter and distinct triggering
  descriptions.
- Future document-specific skills are documented but have no empty
  scaffolding.
- `project-design` remains a future global orchestrator and does not duplicate
  specialized methodology.
- `document-output` is retained without irreversible transformation and its
  documentary-orchestration status is explicitly provisional.
- `document-output` does not become a second global project orchestrator and
  never owns or modifies design content.
- `project-framing` accepts an existing Project View or available project
  sources and remains independently callable.
- `project-framing` explicitly reworks and clarifies the expression of need
  rather than only summarizing sources.
- The primary output is an autonomous, Markdown-native Project Canvas.
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
- Future Google Docs and Microsoft Word targets remain documented as
  template-dependent capabilities, not current behavior.
- Future Google Sheets backlog restitution remains template-dependent and is
  not current behavior.
- All four permanent fixture scenarios are re-run and documented.
- The manual test file remains one flat Markdown file, retains
  `PF-MAN-001` through `PF-MAN-005`, bilingual criteria, allowed statuses,
  result areas, and the confidentiality rule.
- No Golden Output changes without explicit human approval.
- No installable skill or shared resource depends on `development/`.
- The Canonical Domain Model, Knowledge Model, Project Model, Information
  Architecture ADR, and French canonical terminology remain unchanged.
- No commit or push is performed.

## Open Decisions

- Whether `document-output` remains the long-term documentary orchestrator
  after document-specific skill behavior is implemented and observed.
- Whether a future `document-project-canvas` is justified for Google Docs or
  Microsoft Word restitution.
- The exact division of routing and consistency responsibilities between
  `project-design` and `document-output`.
- Whether the Unreleased changes remain in version `0.1.0` or require a new
  version.
- Which compatible template contracts will eventually support Google Docs,
  Google Sheets, and Microsoft Word outputs.
- Which Project Canvas changes discovered downstream require a future stable
  identity or version representation.

## Validation Status

Technical implementation and fixture validation may complete in this
iteration. Full methodology validation remains pending until the user returns
the requested manual test results.
