# Definitive Document Skill Architecture Review

Date: 2026-08-05  
Branch: `main`  
Baseline: `ff72ce5` (`Clarify project document architecture`)  
Initial repository state: clean and aligned with `origin/main`

## Objective

Replace the provisional generic document architecture with a definitive
separation between business skills and discipline-specific document skills,
without implementing any new business or document-generation methodology.

## Result

The plugin now exposes the following official skill tree:

```text
skills/
├── project-design
├── project-framing
├── functional-design
├── technical-design
├── product-backlog
├── document-project-canvas
├── document-functional-design
├── document-technical-design
└── document-product-backlog
```

The former generic document placeholder and its development checklist were
deleted. No active contract or documentation page refers to it. Historical
execution reports retain their original evidence and are marked as superseded
by this decision.

## Responsibility Model

The definitive convention is:

```text
<discipline>          -> business artefact
document-<discipline> -> corresponding document
```

- `project-design` will coordinate the workflow without producing business
  content or documents.
- Business skills own project knowledge and produce format-neutral business
  artefacts only.
- Each document skill consumes one validated corresponding artefact, adds no
  knowledge, and will eventually apply document structure, presentation, and
  format rules.
- Markdown will be native for every future document skill.
- Project Canvas, functional-design, and technical-design documents may later
  target Markdown, Microsoft Word, or Google Docs.
- Product Backlog documents may later target Markdown, Google Sheets,
  Microsoft Excel, Microsoft Word, or Google Docs.

These format declarations describe future scope only. No generator,
conversion, export, template, script, example, or external integration has
been implemented.

## Files Created

- `AGENTS.md`
- `CLAUDE.md`
- `plugins/project-design/skills/document-project-canvas/SKILL.md`
- `plugins/project-design/skills/document-functional-design/SKILL.md`
- `plugins/project-design/skills/document-technical-design/SKILL.md`
- `plugins/project-design/skills/document-product-backlog/SKILL.md`
- `plugins/project-design/README.md`
- `development/tests/quality-checklists/document-project-canvas.md`
- `development/tests/quality-checklists/document-functional-design.md`
- `development/tests/quality-checklists/document-technical-design.md`
- `development/tests/quality-checklists/document-product-backlog.md`
- this execution report

## Files Removed

- `plugins/project-design/skills/document-output/SKILL.md`
- `development/tests/quality-checklists/document-output.md`

## Files Aligned

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `README.md`
- `development/PLAN.md`
- `development/PROJECT_CONTEXT.md`
- `development/SPEC.md`
- `development/tests/executions/2026-07-23-french-terminology-review.md`
- `development/tests/executions/2026-07-23-project-model-review.md`
- `development/tests/executions/2026-08-05-document-architecture-audit.md`
- `development/tests/executions/2026-08-05-project-canvas-review.md`
- `development/tests/quality-checklists/README.md`
- `development/tests/quality-checklists/project-design.md`
- `plugins/project-design/.claude-plugin/plugin.json`
- `plugins/project-design/.codex-plugin/plugin.json`
- `plugins/project-design/shared/project-model/README.md`
- `plugins/project-design/shared/project-model/information-architecture.md`
- `plugins/project-design/skills/project-design/SKILL.md`
- `plugins/project-design/skills/project-framing/SKILL.md`
- `plugins/project-design/skills/project-framing/references/framing-structure.md`
- `plugins/project-design/skills/project-framing/references/project-canvas.md`
- `plugins/project-design/skills/project-framing/references/quality-checklist.md`
- `plugins/project-design/skills/functional-design/SKILL.md`
- `plugins/project-design/skills/technical-design/SKILL.md`
- `plugins/project-design/skills/product-backlog/SKILL.md`

## Methodology Preservation

No business methodology was added or redesigned. The implemented
`project-framing` workflow still applies the same non-invention rules, ten
Project Canvas sections, traceability requirements, and readiness logic. Its
changes are limited to making the output contract format-neutral and routing
future documentary restitution to `document-project-canvas`.

The other business and document skills remain explicit placeholders. The four
new document skills contain only their role, expected input, future formats,
boundaries, and shared references.

## Roadmap

The official sequence is now:

| Iteration | Scope |
| --- | --- |
| Validation 8.2 | Manual Project Canvas replay |
| 9 | `functional-design` |
| 10 | `technical-design` |
| 11 | `product-backlog` |
| 12 | `document-project-canvas` |
| 13 | `document-functional-design` |
| 14 | `document-technical-design` |
| 15 | `document-product-backlog` |
| 16 | `project-design` orchestration |

## Validation Results

| Control | Result |
| --- | --- |
| Exact nine-skill tree | PASS |
| Active references to the former generic skill | PASS — none outside superseded execution history |
| Four document placeholders remain resource-free | PASS — only `SKILL.md` is present in each directory |
| Business skills remain format-neutral | PASS |
| Nine skill contracts | PASS — official `quick_validate.py` |
| Codex plugin manifest | PASS — official plugin validator |
| Claude plugin manifest | PASS — strict Claude validation |
| Installed Codex cache | PASS — version `0.1.0+codex.20260805192838`, exact nine-skill tree |
| Bundle independence from `development/` | PASS |
| Local Markdown links and code fences | PASS |
| Stable foundations, fixtures, and golden outputs | PASS — unchanged |
| `git diff --check` | PASS |

The manifests keep `skills: "./skills/"` discovery; no per-skill manifest is
required by the current plugin architecture.

## Local Installation Refresh

The repository marketplace already pointed to the edited local bundle, but
Codex was still using the previously installed `0.1.0` cache. The official
cachebuster flow updated the Codex manifest to
`0.1.0+codex.20260805192838`, then reinstalled
`project-design@project-design`.

The installed cache now contains exactly the nine official skill directories,
including the four document placeholders, and contains no occurrence of the
former generic skill name. A new Codex thread is required for the application
to reload the updated skill registry.

## Git State

The user explicitly authorized committing and pushing the complete iteration
on 2026-08-05. The delivery commit is created from this reviewed working tree;
the Git log is authoritative for its final identifier. The post-push working
tree and `main`/`origin/main` alignment are verified during delivery.
