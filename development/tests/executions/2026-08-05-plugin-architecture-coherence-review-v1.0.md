# Plugin Architecture and Coherence Review v1.0

Date: 2026-08-05

Repository: `/Users/julienoger/Documents/Dev/project_design`

Branch: `main`

Baseline: `dfba5f1` (`Finalize document skill architecture`)

Initial state: existing uncommitted Iteration 8.4 and 8.5 changes preserved

## Objective

Review the complete `project-design` architecture before implementing
`functional-design`. The review covers stable models, all nine skills,
business artefacts, documents, ownership, direct and indirect dependencies,
forbidden dependencies, cycles, manifests, documentation, and roadmap
readiness.

This is a read-and-document architecture review. It does not modify a shared
model, skill methodology, fixture, business artefact, or Golden Output.

## Overall Result

**PASS WITH RESERVATIONS**

The architecture is coherent and ready for the `functional-design`
methodology iteration. Each business artefact and document representation has
one owner. No model depends on a skill, no business skill generates a
document, no document skill produces knowledge, and the bundle-local Markdown
dependency graph contains no cycle.

No additional shared foundation is required. The reservations concern stale
or ambiguous documentation and future methodology choices, not a structural
architecture defect.

The official consolidated reference created by this review is:

- `development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md`

## Facts Established

### Repository and Packaging

- `main`, `origin/main`, and `origin/HEAD` resolve to `dfba5f1`.
- The working tree already contained the uncommitted
  `document-project-canvas` implementation and Shared Document Model work.
- The installable boundary is `plugins/project-design/`.
- The complete bundle remains byte-for-byte identical to the active
  `0.1.0+codex.20260805211133` cache installed before this review.
- Development tests, fixtures, reports, examples, and continuity context are
  outside the bundle.
- Both manifests identify the same plugin and expose the same shared skill
  implementation. The Codex version retains base version `0.1.0` with a local
  cachebuster suffix; the Claude manifest uses `0.1.0`.
- Exactly nine skill directories are installed.

### Stable Models

| Model | Established role | Runtime producer |
| --- | --- | --- |
| Canonical Domain Model | Shared semantic vocabulary | None; architectural contract |
| Knowledge Model | Evidence, provenance, epistemic state, and assertion relationships | No standalone producer implemented |
| Project Model | Normalized Project View, statuses, perspectives, and Knowledge Basis | No standalone producer implemented |
| Shared Document Model | Common artefact-to-document contract | None; architectural contract |

The Knowledge Model and Project Model are conceptual structures. When raw
sources are supplied, the implemented `project-framing` workflow prepares
working knowledge and project views according to those contracts without
creating a private competing model.

### Skill Status

| Skill | Status | Unique responsibility |
| --- | --- | --- |
| `project-design` | Placeholder | Future routing and cross-step consistency only |
| `project-framing` | Implemented v0.2; manual validation pending | Project Canvas business artefact |
| `functional-design` | Placeholder | Future Functional Design business artefact |
| `technical-design` | Placeholder | Future Technical Design business artefact |
| `product-backlog` | Placeholder | Future Product Backlog business artefact |
| `document-project-canvas` | Implemented v0.1; combined validation pending | Project Canvas document representation |
| `document-functional-design` | Placeholder | Future Functional Design document representation |
| `document-technical-design` | Placeholder | Future Technical Design document representation |
| `document-product-backlog` | Placeholder | Future Product Backlog document representation |

### Ownership and Boundaries

- `project-framing` solely owns Project Canvas business meaning.
- `functional-design`, `technical-design`, and `product-backlog` will each
  own only their corresponding business artefact.
- Each `document-<discipline>` skill owns only the documentary representation
  and document-level verification of its corresponding artefact.
- `project-design` owns routing and transmission only; it owns no artefact or
  document.
- Business skills contain no document-format ownership.
- Document skills cannot analyze raw sources, normalize project knowledge,
  resolve contradictions, or make Decisions.
- Accepted artefacts or documents re-enter a later evidence cycle as new
  sources; they do not mutate shared models directly.

### Dependencies

- Direct model flow: sources -> Knowledge Model -> Project Model -> business
  skills -> business artefacts.
- Documentary flow: validated business artefact -> corresponding document
  skill -> document.
- Canonical Domain Model defines vocabulary across models and skills but is
  not a processing stage.
- Shared Document Model is consumed by every document skill and depends on no
  discipline or skill.
- Optional platform integrations depend on the core; the core does not depend
  on them.
- Automated graph inspection found 28 bundle Markdown nodes and 73 direct
  local dependencies with no cycle.
- No bundle Markdown file references `development/`.

### Roadmap

- Canonical semantics, evidence preservation, normalization, and documentary
  restitution foundations are complete at their declared conceptual scope.
- Functional and technical design are complementary and may run in parallel;
  the architecture is not a mandatory linear waterfall.
- `functional-design` is the next logical methodology iteration.
- The combined manual validation of `project-framing` and
  `document-project-canvas` remains pending. It is a quality gate, not a
  missing architectural foundation.

## Inconsistencies and Ambiguities Detected

### Architecture Defects

None detected.

No duplicate artefact owner, duplicate document owner, forbidden dependency,
model redefinition, or circular dependency was found.

### Documentation Inconsistencies

1. `plugins/project-design/README.md` says that “the four skills without the
   `document-` prefix” produce business artefacts. Five installed skills lack
   that prefix because `project-design` is also non-documentary, but it
   explicitly produces no business artefact. The intended meaning is the four
   specialized business skills.
2. The `Next Iteration` sections in the Information Architecture ADR,
   Canonical Domain Model, Knowledge Model, and Project Model record the next
   step at the time each foundation was created. Read literally today, they
   conflict with the current roadmap.
3. `development/examples/README.md` states that no runtime example is
   approved, while `project-framing/references/project-canvas-example.md` is
   an installed, approved structural runtime example.
4. `development/tests/golden-outputs/README.md` says detailed skill
   methodologies remain entirely `TO BE DEFINED`, although
   `project-framing` and `document-project-canvas` are implemented. The
   statement that no Golden Output is approved remains correct.
5. `development/PROJECT_CONTEXT.md` contains the duplicated phrase “Le Le
   Google Sheet” in historical continuity text.
6. The execution-history template uses `PASS`, `FAIL`, or `BLOCKED`, while
   later review prompts and manual validation also use
   `PASS WITH RESERVATIONS` and `NOT APPLICABLE`.

These findings are documentary debt. They do not change runtime behavior or
architectural responsibility.

### Deliberately Unresolved Methodology Boundaries

1. There is no standalone executable producer for the Knowledge Model or
   Project Model. This is consistent with their current conceptual status,
   but future skills must state whether they require a supplied Project View
   or can prepare a working view from raw inputs.
2. The minimum combination of Project Canvas, Functional Design, and
   Technical Design required before `product-backlog` can proceed is not yet
   fixed.
3. The exact coordination points between functional and technical design are
   not yet defined beyond their complementary or parallel relationship.
4. Stable identifiers, serialization, schemas, change propagation, and
   invalidation remain deferred by the shared models.

These items belong to future methodology or representation work. None
requires a new shared foundation before `functional-design`.

## Recommendations

### Necessary Improvements

Before a public release or architecture v1.0 freeze:

- correct the ambiguous business-skill wording in the bundle README;
- mark the model and ADR `Next Iteration` sections as historical, or replace
  them with links to the current roadmap without changing model semantics;
- align the examples and Golden Output README status statements with the
  implemented skills;
- remove the duplicated continuity-text word;
- define one repository-wide result vocabulary for execution reports.

During the `functional-design` iteration:

- define its minimum accepted input modes;
- define its structured Functional Design artefact contract;
- preserve the Project Canvas and shared-model boundaries;
- define purpose-specific readiness, blocking questions, traceability, and
  founded upstream adjustment handling;
- validate the methodology against all four permanent fixtures.

### Optional Improvements

- add direct terminology references to `technical-design` and
  `product-backlog` for consistency, even though they already inherit
  canonical semantics through the Project Model and quality rules;
- add a small maintained ownership matrix beside the architecture overview;
- automate the existing link, bundle-boundary, and cycle checks under a
  lightweight development tool without automating methodological approval;
- add a README under `development/documentation/` if more official
  architecture documents are introduced.

### Future Evolution

- define stable model identities and versions only when multiple implemented
  consumers demonstrate the required behavior;
- define schemas and serialization without embedding skill methodology;
- define the Product Backlog minimum designed-input contract in its own
  iteration;
- implement global orchestration only after all specialized contracts are
  stable;
- keep external platform adapters dependent on the core rather than changing
  core contracts for a platform.

## Files Created

- `development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md`
- `development/tests/executions/2026-08-05-plugin-architecture-coherence-review-v1.0.md`

## Files Modified

- `README.md`
- `CHANGELOG.md`
- `development/README.md`
- `development/PLAN.md`
- `development/PROJECT_CONTEXT.md`
- `development/SPEC.md`

No file under `plugins/project-design/shared/`,
`plugins/project-design/skills/`, `development/tests/fixtures/`, or
`development/tests/golden-outputs/` was modified by this review.

## Validation Results

| Control | Result |
| --- | --- |
| Required files read completely | PASS |
| Model objectives, owners, producers, consumers, dependencies, and limits | PASS |
| Nine skill contracts and responsibility overlap | PASS |
| Unique business-artefact ownership | PASS |
| Unique document-representation ownership | PASS |
| Business/document boundary | PASS |
| Model-to-skill dependency direction | PASS |
| Bundle dependency graph | PASS — 28 nodes, 73 edges, no cycle |
| Global, model, and skill diagrams | PASS |
| Flow matrix and roadmap consistency | PASS WITH RESERVATIONS — pending manual replay and future methodology details |
| Codex official plugin validation | PASS |
| Claude strict plugin validation | PASS |
| Nine official skill validations | PASS |
| Local Markdown links | PASS |
| Markdown code fences | PASS |
| Bundle dependency on `development/` | PASS — none |
| Bundle comparison with the pre-review active cache | PASS — identical |
| Stable models | PASS — unchanged |
| Skill methodologies | PASS — unchanged |
| Fixtures and Golden Outputs | PASS — unchanged |
| `git diff --check` | PASS |

## Final Confirmation

The plugin architecture is coherent. No major ambiguity prevents the next
methodology iteration. `functional-design` can be started from the stable
foundations without revisiting or extending them, provided its detailed prompt
defines the discipline-specific contract listed above.

No commit was created. No push was performed.
