# Contributing

Keep all source content, identifiers, comments, manifests, documentation, workflows, schemas, and tests in English. Localized user-facing assets are the only exception and must follow `<asset-name>.<language-code>.<extension>`, optionally using a regional language code.

Keep one responsibility per skill and reuse shared resources instead of duplicating concepts. Preserve the platform independence of `skills/`; place platform-specific configuration in its manifest or integration directory.

Reuse the
[Canonical Domain Model](shared/terminology/canonical-domain-model.md) for
shared business concepts. Do not redefine canonical meaning inside a skill,
schema, integration, or generated artefact.

Reuse the
[Minimal Knowledge Model](shared/knowledge-model/README.md) for assertions,
provenance, confidence, uncertainty, validation, and relationships between
extracted statements. Do not resolve contradictions or normalize project
truth inside extraction or an individual skill.

Reuse the
[Minimal Normalized Project Model](shared/project-model/README.md) for the
shared current project view, normalized canonical elements, relationships,
normalization status, lifecycle perspective, and Knowledge Model derivation.
Skills may consume relevant project information but must not maintain a
private competing normalized view.

Do not add automation before the related methodology and contracts are validated. Distinguish implemented behavior from `UNDER CONSTRUCTION` and `TO BE DEFINED` plans.

Update `CHANGELOG.md` for every release or material repository change. Validate both plugin manifests and every modified skill before submitting a contribution.

Before changing a skill or shared contract, read
[`tests/TESTING.md`](tests/TESTING.md), identify affected scenarios and
checklists, and update them in the same change. Run the relevant scenarios,
classify meaningful differences, and record the validation result. Never add
or replace a golden output without explicit human approval.
