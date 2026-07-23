# Shared Assets

UNDER CONSTRUCTION

This directory will contain reusable user-facing assets for project-design outputs. Assets may be global or localized.

Use these naming forms:

```text
<asset-name>.<extension>
<asset-name>.<language-code>.<extension>
<asset-name>.<regional-language-code>.<extension>
```

Examples:

```text
project-framing.md
project-framing.fr.md
project-framing.en.md
project-framing.fr-FR.md
project-framing.fr-CA.md
project-framing.en-GB.md
```

The future resolution order is:

1. Exact regional-language asset.
2. Base-language asset.
3. Global asset.
4. Controlled missing-asset handling.

Never silently fall back to an unrelated language. Asset storage, resolution, validation, and branding rules are TO BE DEFINED.

Localized canonical terminology is maintained separately under
[`shared/terminology/`](../terminology/README.md). Terminology companions use
the same language suffix convention but are not document templates or
presentation assets.
