# Packaging Boundary Review

- Date: 2026-07-24
- Reviewer: Codex
- Platform: Codex and Claude Code
- Invocation: Repository packaging-boundary review
- Source commit: WORKTREE, uncommitted
- Plugin path: `plugins/project-design/`
- Development path: `development/`
- Local path: `.local/`

## Overall Status

PASS

## Objective Achieved

Separated the installable plugin bundle from versioned development resources
and ignored local work.

The repository marketplace now points only to `plugins/project-design/`.
Tests, fixtures, execution evidence, continuity context, plans,
specifications, and examples remain versioned under `development/` without
being part of the installable source path.

## Packaging Summary

| Area | Responsibility | Git | Installed |
| --- | --- | --- | --- |
| `plugins/project-design/` | Manifests, skills, shared models, terminology, and runtime quality contracts | Tracked | Yes |
| `development/` | Tests, fixtures, reports, context, plans, specifications, and examples | Tracked | No |
| `.local/` | Temporary, confidential, and machine-specific work | Ignored | No |
| `integrations/` | Development notes and future optional adapters | Tracked | No |

## Runtime Independence

- The normative `project-framing` checklist is now bundled under the skill's
  `references/` directory.
- Shared quality rules are self-contained.
- Knowledge Model and Project Model examples no longer link to development
  fixtures.
- The normative Spec Kit independence boundary is bundled under `shared/`.
- No file under `plugins/project-design/` references `development/`.
- All bundle-local Markdown links remain inside the installable boundary.

No canonical concept, Knowledge Model construction, Project Model
construction, or skill responsibility was added, removed, renamed, merged, or
split. Changes to shared-model documents are limited to removing
development-corpus link dependencies from examples.

## Repository Impact

Created:

- `.agents/plugins/marketplace.json`
- `development/README.md`
- `development/PROJECT_CONTEXT.md`
- `development/tests/executions/2026-07-24-packaging-boundary-review.md`
- `plugins/project-design/skills/project-framing/references/quality-checklist.md`

Moved:

- plugin manifests, `skills/`, and `shared/` to
  `plugins/project-design/`;
- tests, examples, plan, specification, and continuity context to
  `development/`;
- the normative Spec Kit boundary to the installable `shared/` directory;
- the manual `project-framing` workbook to one flat Markdown file.

Modified:

- repository, contribution, integration, testing, roadmap, specification,
  changelog, quality-rule, model-example, and execution-report documentation;
- `.gitignore` to exclude `.local/`;
- `project-framing` and `project-design` runtime references.

Removed:

- runtime dependencies on development fixtures and quality checklists;
- the per-skill manual-test subdirectory.

## CI and Quality Checks

| Check | Result |
| --- | --- |
| Codex plugin validator | PASS |
| Claude strict plugin validator | PASS |
| Six skill validators | PASS |
| Repository marketplace JSON | PASS |
| Marketplace source path exists | PASS |
| `.local/` exists and is ignored | PASS |
| Bundle dependency on `development/` | PASS: NONE |
| Bundle links escaping installable boundary | PASS: NONE |
| Global Markdown links and fences | PASS |
| Manual test cases and tables | PASS |
| `git diff --check` | PASS |
| Local app installation from marketplace | NOT RUN |
| Golden Outputs changed | PASS: NO CONTENT CHANGE |

## Assumptions

- The repository marketplace root resolves `./plugins/project-design`
  relative to the repository root.
- Local app installation is a distribution smoke test, not required to prove
  the source boundary structurally.
- Development fixtures and reports remain available to contributors through
  Git.
- `.local/` may contain sensitive work and must never be relied on by tests or
  installed skills.

## Open Questions

- External GitLab marketplace distribution and authentication.
- Version pinning policy for marketplace releases.
- Whether a package-registry distribution is needed later.
- Automated installation smoke testing in CI.

## Recommendation

Run one local marketplace installation test before the first distributed
release. The next business iteration can then implement `functional-design`
against the isolated bundle.

## Git Status

Changes are local only. No commit or push was performed.

## Result

PASS
