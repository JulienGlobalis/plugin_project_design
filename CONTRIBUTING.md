# Contributing

Keep normative source content, identifiers, comments, manifests,
documentation, workflows, schemas, and tests in English. Localized
user-facing assets and terminology companions are the exceptions and must
follow `<asset-name>.<language-code>.<extension>`, optionally using a regional
language code.

English canonical names and definitions remain authoritative. A localized
terminology companion may define preferred labels, variants, and usage notes
but must not add, remove, merge, split, or redefine canonical concepts.

Keep one responsibility per skill and reuse shared resources instead of
duplicating concepts. Preserve the platform independence of
`plugins/project-design/skills/`; place platform-specific configuration in
the plugin manifest or an integration directory.

Apply the definitive skill naming and ownership convention to every new
discipline:

```text
<discipline>           produces the business artefact
document-<discipline>  produces its document
```

Business skills own knowledge and contain no document format, template,
formatting, conversion, or export behavior. Document skills consume one
validated business artefact and never add knowledge or make Decisions.

Keep the installable bundle independent from `development/`. Tests may
validate runtime contracts but installable skills and shared resources must
not link to development-only files.

Keep draft or unapproved examples under `development/examples/`. Place an
approved example needed at runtime under the relevant
`plugins/project-design/skills/<skill-name>/references/` directory and link
to it directly from that skill's `SKILL.md`. Do not use expected fixture
conclusions as runtime examples because that would bias regression
validation. Golden Outputs remain development-only test evidence.

Reuse the
[Canonical Domain Model](plugins/project-design/shared/terminology/canonical-domain-model.md) for
shared business concepts. Do not redefine canonical meaning inside a skill,
schema, integration, or generated artefact.

Reuse the
[Minimal Knowledge Model](plugins/project-design/shared/knowledge-model/README.md) for assertions,
provenance, confidence, uncertainty, validation, and relationships between
extracted statements. Do not resolve contradictions or normalize project
truth inside extraction or an individual skill.

Reuse the
[Minimal Normalized Project Model](plugins/project-design/shared/project-model/README.md) for the
shared current project view, normalized canonical elements, relationships,
normalization status, lifecycle perspective, and Knowledge Model derivation.
Skills may consume relevant project information but must not maintain a
private competing normalized view.

Do not add automation before the related methodology and contracts are validated. Distinguish implemented behavior from `UNDER CONSTRUCTION` and `TO BE DEFINED` plans.

Update `CHANGELOG.md` for every release or material repository change.
Validate the plugin bundle at `plugins/project-design/`, both manifests, and
every modified skill before submitting a contribution.

Before changing a skill or shared contract, read
[`development/tests/TESTING.md`](development/tests/TESTING.md), identify affected scenarios and
checklists, and update them in the same change. Run the relevant scenarios,
classify meaningful differences, and record the validation result. Never add
or replace a golden output without explicit human approval.
