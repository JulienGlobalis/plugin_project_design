# French Canonical Terminology Review

- Date: 2026-07-23
- Reviewer: Codex
- Platform: Platform independent
- Invocation: Localized terminology review
- Source commit: WORKTREE, uncommitted
- Skills: All future skills and document-output
- Scenarios: Shared terminology validation
- Golden output: NONE

## Overall Status

PASS

## Objective Achieved

Added the initial
[French canonical terminology companion](../../shared/terminology/canonical-terms.fr.md)
without translating or modifying the normative Canonical Domain Model.

The companion gives future skills stable French labels, allowed variants,
usage distinctions, shared-model labels, and explicit fallback rules.

## Localized Terminology Summary

- Language: `fr`
- Canonical concept mappings: 22
- Shared Knowledge Model and Project Model labels: 14
- Normalization status labels: 3
- Lifecycle perspective labels: 3
- Knowledge Basis role labels: 3
- Regional variants introduced: NONE
- Canonical definitions translated or duplicated: NONE

Main decisions:

- keep English canonical names and definitions normative;
- localize presentation labels rather than canonical semantics;
- distinguish canonical concepts from shared-model constructions;
- preserve high-risk distinctions such as Stakeholder versus Actor, Need
  versus Requirement, Option versus Decision, and Risk versus Issue;
- keep project-specific Domain Terms under source and project-glossary
  authority;
- require explicit handling when requested-language terminology is missing.

## Architecture Compliance

| Check | Result |
| --- | --- |
| Canonical Domain Model file changed | PASS: NO |
| Canonical concepts changed | PASS: NONE |
| Knowledge Model file changed | PASS: NO |
| Knowledge Model responsibilities changed | PASS: NONE |
| Project Model file changed | PASS: NO |
| Project Model responsibilities changed | PASS: NONE |
| Information-processing pipeline changed | PASS: NO |

Frozen foundation SHA-256 values before and after this change:

- Canonical Domain Model:
  `8ba605e6b3b437d27181e04458069a2cdda57862252cb8d36a7373aff76b84f5`
- Minimal Knowledge Model:
  `45edcc2479191d6172ccd48f2b5c8f9990fd38b2cf6762c98af702832c475aee`
- Minimal Normalized Project Model:
  `a21e78e961a294b8b2406f308128ce69f7ea93ab4bd9a4016a0f142fbf553612`

Localized terminology remains a presentation resource outside the processing
pipeline.

## Vocabulary Validation

| Concern | Result |
| --- | --- |
| All 22 canonical names mapped exactly once | PASS |
| Every concept has one preferred French label | PASS |
| Canonical and non-canonical labels separated | PASS |
| Stakeholder and Actor distinction | PASS |
| Need and Requirement distinction | PASS |
| Option and Decision distinction | PASS |
| Risk and Issue distinction | PASS |
| Capability and Feature distinction | PASS |
| System Element granularity preserved | PASS |
| Project Domain Terms protected from automatic translation | PASS |

The mappings cover the canonical concerns exercised by all four permanent
fixtures. No fixture or generated output was changed.

## Resolution and Fallback Validation

- Exact regional language before base language: PASS
- Base `fr` resource usable for `fr-FR` and `fr-CA`: PASS
- Missing requested language remains explicit: PASS
- English remains the default when no language is requested: PASS
- Requested-language fallback to English requires an explicit rule or user
  acceptance: PASS
- Silent unrelated-language fallback prohibited: PASS

## Repository Impact

Created:

- `shared/terminology/canonical-terms.fr.md`
- `tests/quality-checklists/localized-terminology.md`
- `tests/executions/2026-07-23-french-terminology-review.md`

Modified:

- `README.md`
- `PLAN.md`
- `SPEC.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `shared/terminology/README.md`
- `shared/assets/README.md`
- `shared/quality-rules/README.md`
- `tests/quality-checklists/README.md`
- `tests/quality-checklists/document-output.md`

Removed:

- NONE

## CI and Quality Checks

| Check | Result |
| --- | --- |
| Documentation updated | PASS |
| All canonical concepts mapped | PASS |
| Preferred French labels present | PASS |
| Translation collisions documented | PASS |
| Language resolution documented | PASS |
| Canonical Domain Model unchanged | PASS |
| Knowledge Model unchanged | PASS |
| Project Model unchanged | PASS |
| Repository consistency | PASS |
| Markdown validation | PASS |
| Local Markdown links | PASS |
| Plugin manifests | PASS |
| Skill foundations | PASS |
| Golden Outputs unchanged | PASS |
| Functional localized output execution | NOT APPLICABLE |

Functional localized output execution is not applicable because
`project-framing` and `document-output` methodologies remain under
construction.

## Assumptions

- `fr` is the appropriate first resource for generic French terminology.
- English canonical names remain stable internal references.
- Preferred labels may be refined from real output review without changing
  canonical meaning.
- Regional terminology should be introduced only when a demonstrated
  difference justifies it.

## Open Questions

- Whether real project-framing outputs require `fr-FR` or `fr-CA` overrides.
- How project-specific Domain Terms and approved glossaries will be localized.
- Which future skill-specific concepts need their own terminology companions.
- Whether output formats require machine-readable terminology mappings after
  methodologies stabilize.

## Recommendation

Iteration 8 should use the French companion when French framing output is
requested and record any awkward or ambiguous label as terminology feedback.
Do not add regional files or machine-readable mappings until real usage
demonstrates the need.

## Git Status

Changes are local only. No commit or push was performed.

## Result

PASS
