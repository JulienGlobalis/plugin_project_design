# Project Canvas Evolution Review

> **Superseded architecture notice:** the documentary-orchestration
> recommendation in this historical report was replaced later on 2026-08-05
> by the definitive discipline-specific document-skill architecture. The
> Project Canvas methodology evidence remains valid.

- Date: 2026-08-05
- Reviewer: Codex
- Platform: Platform independent, with Codex and Claude manifest validation
- Invocation: Architecture evolution and four independent
  `project-framing` fixture executions
- Source commit: `19f8abf` (`Document prompt history and runtime example policy`)
- Source branch: `main`, initially clean and aligned with `origin/main`
- Skill: `project-framing` methodology version 0.2
- Scenarios: all four permanent fixtures
- Golden Output: NONE APPROVED; no Golden Output changed

## Overall Status

**IMPLEMENTATION COMPLETE — MANUAL USER VALIDATION PENDING**

Technical and repository validation: **PASS**.

Full methodology validation remains pending until the user returns the manual
test results from `development/tests/manual/project-framing.md`.

## 1. Modifications Realized

### Target Architecture

The documented forecast architecture now distinguishes:

1. global orchestration through future `project-design` behavior;
2. design knowledge through `project-framing`, future
   `functional-design`, future `technical-design`, and future
   `product-backlog` behavior;
3. document restitution through future `document-functional-design`,
   `document-technical-design`, and `document-product-backlog` skills.

`functional-design` and `technical-design` are documented as complementary
steps that may run in parallel when inputs and unresolved questions permit.
No future skill scaffold or methodology was created.

### `project-framing`

`project-framing` is now explicitly the first project-design step. It reworks
and clarifies the expression of need and produces a Markdown-native Project
Canvas rather than a flexible framing summary.

The Canvas contract requires:

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

A materially missing section remains visible as unresolved. The skill must not
invent content to complete the structure.

### Runtime References

Created:

- `plugins/project-design/skills/project-framing/references/project-canvas.md`;
- `plugins/project-design/skills/project-framing/references/project-canvas-example.md`.

The example is short, fictional, unrelated to the permanent fixtures, and
contains unresolved information and an explicit Scope limit. It is not a
Golden Output.

The previous framing-structure reference now concentrates on Project Canvas
presentation and registers. The runtime quality checklist now verifies all
ten sections, semantic distinctions, readiness, non-invention, and later
adjustment rules.

### Reliability and Later Adjustments

The intended 80-90% reliability is represented only as a qualitative business
expectation. No calculated score, probability, or completeness percentage is
generated.

Functional or technical design may reveal reliable information requiring a
later Canvas update. An update must be traceable, justified by a new or
corrected source, limited to a founded enrichment, clarification, or
correction, and must not silently rewrite validated information or Decisions.

### Documentation and Tests

Updated:

- repository architecture, roadmap, specification, changelog, and manifests;
- forecast contracts for existing skill placeholders;
- four fixture scenarios;
- project-framing and adjacent forecast quality checklists;
- testing and manual-validation documentation;
- the flat manual test file with `PF-MAN-001` through `PF-MAN-005`.

The manual file provides each case's objective, exact data list, invocation
prompt, expected controls, bilingual criteria, result area, and reservations.

## 2. Controls Executed

| Control | Command or method | Result | Status |
| --- | --- | --- | --- |
| Initial Git state | `git status --short --branch` | `main...origin/main`, clean | PASS |
| Repository history | `git log -15 --oneline` | 12 commits inspected; HEAD `19f8abf` | PASS |
| Required document review | Full read of context, plan, specification, testing strategy, five stable foundations, skill, runtime references, tests, fixtures, and previous report | Required sources reviewed before modification | PASS |
| Project Canvas structure | Standard-library structural validator | 10 ordered sections in each of four raw fixture outputs | PASS |
| Permanent fixture count | Standard-library structural validator | Exactly four | PASS |
| Manual case identifiers | Standard-library structural validator | `PF-MAN-001` to `PF-MAN-005` | PASS |
| Manual bilingual/status fields | Standard-library structural validator and review | Present with result and reservation areas | PASS |
| JSON syntax | Standard-library JSON parser | Codex, Claude, and marketplace JSON valid | PASS |
| Codex plugin validation | Plugin Creator `validate_plugin.py` | Plugin validation passed | PASS |
| Claude plugin validation | `claude plugin validate plugins/project-design --strict` | Validation passed | PASS |
| Six skill validations | Skill Creator `quick_validate.py` through isolated `uv` environment | 6/6 valid | PASS |
| Markdown fences and local links | Standard-library repository validator | Valid | PASS |
| Bundle-local links | Standard-library repository validator | All remain in installable boundary | PASS |
| Bundle dependency on development resources | Text and link validation | None | PASS |
| Patch whitespace | `git diff --check` | No error | PASS |
| Local raw-output isolation | `git check-ignore -v` | `.local/` rule applies | PASS |
| Information Architecture ADR hash | SHA-256 before and after | `44bbeb8f48009c4bb9b53e05400671c028d0bd4198bf31ce340a2173b009d264` unchanged | PASS |
| Canonical Domain Model hash | SHA-256 before and after | `8ba605e6b3b437d27181e04458069a2cdda57862252cb8d36a7373aff76b84f5` unchanged | PASS |
| Knowledge Model hash | SHA-256 before and after | `f594341281352dc996654a8fd7228bf93c24ceae4786e17926f78da0145e97cb` unchanged | PASS |
| Project Model hash | SHA-256 before and after | `13ec01e1965d39ca08abfb1938cbcd394b1c54ad434c27391e7604b46befcae8` unchanged | PASS |
| French terminology hash | SHA-256 before and after | `c84ce988a30f269bc5aa8919e5bc23ecf6e6ee58eb6f20cf8dc58db7e23bed16` unchanged | PASS |
| Golden Output README hash | SHA-256 before and after | `9436dfaff67ea29da21f0090fbf912ef63c23f01850369cf73156af5bf7993b1` unchanged | PASS |
| Google Docs, Sheets, DOCX, runtime, API, MCP, agent, hook, persistence implementation | Scope review | Not implemented | NOT APPLICABLE |
| Manual user validation | Updated manual workbook | Awaiting user execution | PASS WITH RESERVATIONS |

The first direct `quick_validate.py` attempts failed because the system Python
did not contain PyYAML. The same official validator then passed for all six
skills through an isolated `uv --with pyyaml` environment; no dependency was
installed in the repository.

## 3. Four-Fixture Validation

Raw outputs are preserved outside Git under
`.local/test-runs/2026-08-05-project-canvas/`.

### `incomplete-project`

**Result: PASS**

- Produced all ten sections.
- Preserved Existing mailbox, message, and spreadsheet handling.
- Kept the target Capability list outside an approved MVP.
- Preserved ambiguous users and Domain Terms.
- Left ownership, Scope, approval rules, data rules, technical Constraints,
  measures, and success criteria unresolved.
- Classified questions by functional, technical, backlog, blocking, or
  deferrable impact.
- Did not invent a delivery plan or architecture.

### `contradictory-project`

**Result: PASS**

- Produced all ten sections.
- Preserved two-, three-, five-, and seven-year retention positions.
- Preserved conflicts in eligibility, approval, response time, reporting,
  rollout, cutover, launch dates, mailbox transition, and priorities.
- Kept preferences, estimates, workshop proposals, and assumptions outside
  the Decision list.
- Avoided invented success targets and unsupported Scope normalization.
- Presented the Canvas as a decision frame rather than a false resolved view.

### `application-modernization`

**Result: PASS**

- Produced all ten sections.
- Preserved Existing, Target, and Transition perspectives.
- Kept current application defects as confirmed Issues and migration
  uncertainty as Risks.
- Preserved reopening and Central Intake contradictions.
- Preserved unknown applicability of historical Decisions.
- Avoided target module decomposition, architecture, technology selection,
  and invented MVP sequencing.
- Preserved supplied continuity and history Constraints without inventing
  additional success measures.

### `new-application`

**Result: PASS**

- Produced all ten sections in natural French.
- Kept proposed MVP Scope provisional pending required authority.
- Kept explicit exclusions separate from future Options.
- Distinguished Project Stakeholders, direct users, indirect users, and
  personas.
- Preserved identity, language, accessibility, security, privacy, service
  quality, and interface concerns at framing level.
- Used supplied availability, performance, and restoration targets without
  inventing business baselines or target values.
- Avoided inventing a legacy application, migration history, architecture, or
  technology.

## 4. Regression Assessment

| Area | Observed difference | Classification | Disposition |
| --- | --- | --- | --- |
| Output structure | Flexible selected sections become ten required sections or explicit gaps | IMPROVEMENT | Accepted by the intervention brief |
| Output identity | Framing document becomes Project Canvas | IMPROVEMENT | Runtime and repository contracts updated |
| Missing sections | Previously omitted; now explicitly unresolved when material | IMPROVEMENT | Prevents hidden gaps for downstream skills |
| Question priority | Three prior groups become five downstream-impact classifications | IMPROVEMENT | Tests and references updated |
| MVP representation | Generic Scope becomes explicit MVP, Outside MVP, and Unresolved Scope | IMPROVEMENT | Non-invention safeguards added |
| Document handling | Generic future document output becomes separated document-specific forecast architecture | IMPROVEMENT | No future skill implemented |
| Golden Outputs | No approved references exist and no files changed | NO REGRESSION | Human approval remains required for any future Golden Output |
| Manual validation | Previous manual results do not validate the revised Canvas contract | UNRESOLVED ISSUE | User must replay the updated cases |

No automatic Golden Output replacement is proposed. Any future approved
reference must be reviewed against the ten-section Canvas contract by a human.

## 5. Documentary Architecture Recommendation

### Observed Facts

- `document-output` already exists as one of six current skill directories.
- Three future deliverable types need different mappings and destination
  conventions.
- Language, branding, assets, template compatibility, and cross-document
  consistency are shared documentary concerns.
- No document-specific methodology has yet been implemented or tested.

### Interpretation

Direct document-specific skills improve responsibility clarity, while a small
orchestrator could prevent duplication of shared documentary routing and
consistency rules. Current evidence is insufficient to prove that an
additional orchestration layer is necessary.

### Recommendation

Provisionally retain `document-output` as a future documentary orchestrator
that routes validated domain artefacts to independently callable
document-specific skills. It must not own or modify business or technical
content.

### Decision Still Required

Reassess Option A versus Option B after at least the first two
document-specific skills have concrete, tested workflows. Do not remove
`document-output` before that evidence exists.

## 6. Manual Tests to Perform

Use `development/tests/manual/project-framing.md`.

Replay:

- `PF-MAN-001`: incomplete fixture;
- `PF-MAN-002`: contradictory fixture;
- `PF-MAN-003`: modernization fixture;
- `PF-MAN-004`: new application in French;
- `PF-MAN-005`: controlled real project when suitable material is available.

Return:

- selected case identifier;
- generated Project Canvas;
- completed bilingual verification grid;
- case result and reservations;
- feedback summary;
- readiness decisions for functional design, technical design, and backlog
  preparation.

Human validation must specifically confirm practical usefulness, natural
language, level of detail, ten-section coverage, absence of invention, and
whether the Canvas avoids repeating the complete framing effort downstream.

## 7. Repository Impact

Created:

- `plugins/project-design/skills/project-framing/references/project-canvas.md`;
- `plugins/project-design/skills/project-framing/references/project-canvas-example.md`;
- `development/tests/executions/2026-08-05-project-canvas-review.md`.

Modified:

- `README.md`;
- `CHANGELOG.md`;
- `development/PLAN.md`;
- `development/SPEC.md`;
- `development/PROJECT_CONTEXT.md`;
- testing, scenario, manual, and quality-checklist documentation;
- both plugin manifests;
- all six existing skill contracts or descriptions where architecture or
  handoff wording required alignment;
- `project-framing` runtime references and quality contract.

Removed:

- NONE.

The four raw fixture outputs are local ignored evidence and are not listed as
versioned repository files.

## 8. Final Git and Delivery Status

The worktree contains only local, uncommitted intervention changes plus the
two intended new runtime references and this report. `.local/` raw outputs are
ignored.

No commit and no push were performed.

## Result

**IMPLEMENTATION COMPLETE — MANUAL USER VALIDATION PENDING**
