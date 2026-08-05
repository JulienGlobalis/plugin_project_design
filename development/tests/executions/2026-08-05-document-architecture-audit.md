# Document Architecture Audit

> **Superseded architecture notice:** this historical audit documented a
> provisional generic documentary-orchestration option. The later definitive
> architecture replaces it with four installed discipline-specific document
> placeholders. The observations and validation evidence remain historical.

- Date: 2026-08-05
- Reviewer: Codex
- Source branch: `main`
- Source commit: `0332597` (`Evolve project framing around Project Canvas`)
- Initial worktree: clean and aligned with `origin/main`
- Scope: repository documentation, manifests, installed skill descriptions,
  forecast roadmap, and documentary responsibility boundaries
- Excluded: methodology implementation, shared architectural foundations,
  fixtures, Golden Outputs, runtime, external integrations, commit, and push

## Overall Status

**DOCUMENTATION CORRECTED — TECHNICAL VALIDATION PASS**

The Project Canvas implementation remains technically complete. Manual user
validation of `project-framing` remains pending and is not replaced by this
documentation audit.

## 1. Facts Observed Before Correction

- Exactly six skill directories were installed:
  `project-design`, `project-framing`, `functional-design`,
  `technical-design`, `product-backlog`, and `document-output`.
- Only `project-framing` contained an implemented business methodology.
- The other five installed entries were marked `UNDER CONSTRUCTION`, but
  their front-matter descriptions sometimes used operational verbs that could
  make discoverability look like implemented capability.
- The repository already distinguished global orchestration, design skills,
  and future document-restitution skills in several files.
- `project-framing` already defined the Project Canvas as its primary
  Markdown output and explicitly rejected simulated Google Docs or Microsoft
  Word conversion.
- The three future document-specific skills had no directory and were not
  listed as installed by either manifest.
- `document-output` was already described as provisional, but its boundary
  with global `project-design` orchestration was not stated consistently.
- The roadmap grouped all three future document-specific skills into one
  iteration and contained no explicit `document-project-canvas` evaluation.
- The previous Project Canvas report recorded fixture and structural
  validation correctly; it did not provide a repository-wide matrix locating
  every documentary architecture decision.
- No non-canonical spelling variant of the functional-design or
  document-output skill names was present.

## 2. Inconsistencies Identified

1. Installed directory, implemented methodology, placeholder, provisional
   responsibility, and future non-installed skill were not compared in one
   authoritative status matrix.
2. Manifest descriptions were structurally valid but did not make the
   placeholder status of five installed entries sufficiently explicit.
3. The root README described the target tree but its roadmap was too short to
   show separate documentary iterations and delayed global orchestration.
4. `development/PLAN.md` grouped the future document skills and did not state
   the exact template conditions for each external format.
5. `development/SPEC.md` had no consolidated current-capability table, no
   explicit Google Sheets backlog condition, and no
   `document-project-canvas` decision point.
6. `development/PROJECT_CONTEXT.md` contained the forecast tree but not the
   complete format contract, and its Project Canvas Git section still
   described the former uncommitted state even though commit `0332597` had
   been pushed.
7. The `project-design` and `document-output` contracts did not state their
   mutual routing boundary precisely enough to prevent a second global
   orchestrator.
8. Placeholder skill descriptions could be interpreted as current
   executable capability despite their body status.

## 3. Documentary Architecture Matrix

| Architectural subject | Reference document | Section | Status before | Correction | Status after |
| --- | --- | --- | --- | --- | --- |
| Role of `project-design` | `development/PLAN.md` | Global Orchestration | Present but brief | Added installed-placeholder status, traceable return behavior, and non-duplication boundary | PASS |
| Role of `project-design` | `plugins/project-design/skills/project-design/SKILL.md` | Status, Purpose, Forecast Routing | Operational wording despite under-construction status | Marked as placeholder, kept global routing forecast, and separated documentary routing | PASS |
| Output of `project-framing` | `plugins/project-design/skills/project-framing/SKILL.md` | Output Contract | Already coherent | No change: Markdown Project Canvas remains current capability | PASS |
| Project Canvas structure | `plugins/project-design/skills/project-framing/references/project-canvas.md` | Purpose and Role, Later Adjustments | Already coherent | No change | PASS |
| Project Canvas restitution | `README.md`, `development/PLAN.md`, `development/SPEC.md` | Design Artefacts and Document Restitution / Project Canvas Restitution | Current Markdown behavior present only in skill; future decoupling absent | Documented current direct Markdown option and undecided future `document-project-canvas` | PASS |
| Role of `functional-design` | `plugins/project-design/skills/functional-design/SKILL.md` | Front matter, Status, Expected Outputs | Future scope present; placeholder status insufficiently visible to discovery | Marked installed entry as non-implemented placeholder and future business artefact | PASS |
| Role of `technical-design` | `plugins/project-design/skills/technical-design/SKILL.md` | Front matter, Status, Expected Outputs | Future scope present; hosting and operations not explicit | Marked placeholder and completed forecast responsibility list | PASS |
| Role of `product-backlog` | `plugins/project-design/skills/product-backlog/SKILL.md` | Front matter, Status, Purpose, Boundaries | Front matter implied current creation and estimation | Marked placeholder and reinforced non-invention from validated inputs | PASS |
| Future document skills | `README.md` | Current Availability | Named but not compared with installed skills | Added installed/status/capability matrix showing all three as non-installed future skills | PASS |
| Future document formats | `README.md`, `development/PLAN.md`, `development/SPEC.md` | Design and Restitution sections | Template dependency incomplete, especially for backlog | Added Markdown defaults and exact future compatible-template conditions | PASS |
| Status of `document-output` | `plugins/project-design/skills/document-output/SKILL.md` | Status, Purpose, Outputs, Boundaries | Provisional but operational verb could imply availability | Marked provisional non-implemented placeholder; excluded global step selection and content ownership | PASS |
| `project-design` / `document-output` boundary | Both installed contracts and quality checklists | Forecast Routing / Boundaries | Implicit | Assigned global routing to `project-design` and documentary routing only to `document-output` | PASS |
| Manifest capability truthfulness | Codex and Claude manifests | Description fields | Valid but future foundations not visibly placeholders | Descriptions now identify the implemented Canvas and non-implemented installed foundations | PASS |
| Roadmap | `development/PLAN.md`, `development/PROJECT_CONTEXT.md`, `README.md` | Roadmap | Documentary skills grouped and `document-project-canvas` absent | Split three document iterations, added documentary experiment, then delayed global orchestration and adapters | PASS |
| Iteration 8 status | `development/PROJECT_CONTEXT.md`, `README.md` | History / Current Status | Correct manual-validation reservation | Preserved explicitly | PASS |
| Historical Git state | `development/PROJECT_CONTEXT.md` | Project Canvas Git State | Obsolete after commit and push | Recorded delivered commit `0332597` and current audit baseline | PASS |

## 4. Architecture Now Documented

### Global Orchestration

`project-design` is the future global orchestrator. It will select useful
steps, transmit artefacts, maintain cross-step consistency, and support
traceable returns to earlier stages when reliable information changes. It is
an installed placeholder and does not yet execute this workflow.

### Design Skills

| Skill | Step | Status | Business artefact |
| --- | --- | --- | --- |
| `project-framing` | 1 | Implemented; manual validation pending | Project Canvas |
| `functional-design` | 2 | Installed placeholder | Future structured functional-design artefact |
| `technical-design` | 2 bis | Installed placeholder | Future structured technical-design artefact |
| `product-backlog` | After designed and validated Scope | Installed placeholder | Future traceable Product Backlog |

Functional and technical design may be parallel, sequential, or iterative
according to their inputs. Neither may silently rewrite the Canvas.

### Document Restitution

Document skills consume validated design artefacts and present them without
changing meaning, status, Decisions, or unresolved questions.

| Future skill | Input | Native default | Conditional future formats | Installed |
| --- | --- | --- | --- | --- |
| `document-functional-design` | Functional-design artefact | Markdown | Google Docs or Microsoft Word with supplied compatible template | No |
| `document-technical-design` | Technical-design artefact | Markdown | Google Docs or Microsoft Word with supplied compatible template | No |
| `document-product-backlog` | Product Backlog artefact | Markdown | Google Sheets with supplied compatible template; Google Docs or Microsoft Word only for an explicit documentary request with compatible template | No |

`document-output` remains an installed provisional placeholder. It may later
route documentary generation and coordinate presentation constraints, but it
must not select global design steps, own design content, or replace
`project-design`.

## 5. Project Canvas Restitution Recommendation

### Current Minimal Option

Keep the implemented behavior: `project-framing` produces the Project Canvas
directly in Markdown. Google Docs and Microsoft Word are not current
capabilities.

### Future Decoupled Option

Evaluate a future `document-project-canvas` only when at least one concrete
Google Docs or Microsoft Word workflow demonstrates a dedicated template,
format, and quality contract. Do not create it merely for architectural
symmetry.

### Recommendation

Retain the minimal option now. Keep `document-project-canvas` as an explicit
open decision and compare direct invocation with routing through
`document-output` when documentary workflows exist.

## 6. Corrected Roadmap

1. Validate revised Iteration 8 `project-framing` manually.
2. Iteration 9: implement `functional-design`.
3. Iteration 10: implement complementary or parallel `technical-design`.
4. Iteration 11: implement `product-backlog` from designed and validated
   inputs.
5. Implement `document-functional-design` in a dedicated iteration.
6. Implement `document-technical-design` in a dedicated iteration.
7. Implement `document-product-backlog` in a dedicated iteration.
8. Experiment with documentary orchestration and decide `document-output`,
   `document-project-canvas`, and the documentary/global routing boundary.
9. Implement full `project-design` orchestration after specialized contracts
   are sufficiently stable.
10. Design optional adapters and structural automation only afterward.

## 7. Files and Sections Corrected

| File | Sections changed |
| --- | --- |
| `README.md` | Architecture; Current Availability; Design Artefacts and Document Restitution; Roadmap |
| `CHANGELOG.md` | Unreleased |
| `development/PLAN.md` | Responsibility Levels; Project Canvas Restitution; Roadmap |
| `development/SPEC.md` | Iteration Objective; Current Capability Status; In Scope; Out of Scope; Project Canvas Contract; Design and Restitution Boundary; Acceptance Criteria; Open Decisions |
| `development/PROJECT_CONTEXT.md` | Project; Categories of Responsibilities; commit/report history; Project Canvas Git state; Roadmap; deferred decisions |
| Codex manifest | Plugin and interface descriptions |
| Claude manifest | Plugin description |
| `project-design/SKILL.md` | Description; Status; Purpose; Forecast Routing |
| `functional-design/SKILL.md` | Description; Status; Expected Outputs |
| `technical-design/SKILL.md` | Description; Status; Expected Outputs |
| `product-backlog/SKILL.md` | Description; Status; Purpose; Boundaries |
| `document-output/SKILL.md` | Description; Status; Purpose; Expected Outputs; Boundaries |
| `project-design` quality checklist | Forecast-contract status and orchestration boundaries |
| `document-output` quality checklist | Provisional status, template condition, and global-orchestration exclusion |

`project-framing/SKILL.md` and its Project Canvas reference were audited but
not modified because their documentary boundary was already coherent.

## 8. Decisions Still Open

- Whether `document-output` remains the long-term documentary orchestrator.
- Whether a future `document-project-canvas` is justified.
- The exact responsibility split between global `project-design` routing and
  future `document-output` routing after real workflows are observed.
- The compatible template contracts and external formats actually supported
  by each future document skill.
- Whether the Unreleased changes remain version `0.1.0` or require a new
  version.

## 9. Controls

| Control | Command or method | Result | Status |
| --- | --- | --- | --- |
| Initial Git state | `git status`, `git diff --stat`, `git diff --name-only` | Clean `main`, aligned with `origin/main` at `0332597` | PASS |
| Repository history | `git log --oneline -15` | 13 commits inspected | PASS |
| Required document audit | Full reads and repository-wide term searches | Completed before correction | PASS |
| Markdown links | Standard-library repository validator over 101 Markdown files | All local targets resolve | PASS |
| Markdown code fences | Standard-library repository validator over 101 Markdown files | All fences balanced | PASS |
| Canonical naming and typo search | `rg` search for known non-canonical variants | No occurrence | PASS |
| Obsolete architecture search | `rg` searches for grouped-document-roadmap wording and obsolete installed-skill status | No occurrence in current contracts | PASS |
| Codex plugin validation | Plugin Creator `validate_plugin.py plugins/project-design` | Plugin validation passed | PASS |
| Claude strict validation | `claude plugin validate plugins/project-design --strict` | Validation passed | PASS |
| Six installed skill validations | Skill Creator `quick_validate.py` through isolated `uv --with pyyaml` | 6/6 valid | PASS |
| Bundle dependency on `development/` | Repository validator and `rg -F 'development/' plugins/project-design` | None | PASS |
| Protected foundations unchanged | `git diff --quiet HEAD --` on Information Architecture, Canonical Domain Model, Knowledge Model, Project Model, and French terminology | No difference | PASS |
| Fixtures unchanged | `git diff --quiet HEAD -- development/tests/fixtures` | No difference | PASS |
| Golden Outputs unchanged | `git diff --quiet HEAD -- development/tests/golden-outputs` | No difference | PASS |
| Manifests expose no future skill | JSON parsing, exact six-directory comparison, and future-name scan | Six installed entries only; no future directory or manifest announcement | PASS |
| Patch whitespace | `git diff --check` | No error | PASS |
| Local cachebuster and plugin reinstall | Plugin Creator update workflow review | Outside this documentation-only scope; no installation state changed | NOT APPLICABLE |
| Manual user validation | Existing manual test file | Still awaiting user replay | PASS WITH RESERVATIONS |

## 10. Commit and Push

No commit and no push are authorized or performed by this audit.

## Result

**DOCUMENTATION CORRECTED — TECHNICAL VALIDATION PASS**
