# Project Design Plugin Bundle

This directory is the isolated installable bundle for the `project-design`
plugin.

## Official Skill Architecture

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

`project-design` is the future global orchestrator. It will route work,
transmit artefacts, and maintain cross-step consistency without producing
business content or documents.

The four skills without the `document-` prefix produce format-neutral
business artefacts and own project knowledge. The four `document-` skills
consume their corresponding validated artefacts and apply document structure,
formatting, an optional template, and an output format without changing
business knowledge when their methodology is implemented.

The mandatory naming convention is:

```text
<discipline>          -> business artefact
document-<discipline> -> corresponding document
```

## Current Status

`project-framing` has an implemented business methodology and
`document-project-canvas` has its implemented documentary methodology. Manual
validation of the combined chain remains pending. The other seven skill
entries are explicit placeholders.

Current Project Canvas document formats are native Markdown, Microsoft Word,
and Google Docs. The methodology uses a default professional structure or a
compatible supplied template and verifies the native result without changing
Canvas knowledge.

Future formats for the remaining document placeholders are:

- Functional design and technical design: native Markdown, Microsoft Word,
  or Google Docs.
- Product Backlog: native Markdown, Google Sheets, Microsoft Excel, Microsoft
  Word, or Google Docs.

These remaining formats are forecast scope, not currently available
capabilities.

## Shared Foundations

All skills use the bundle-owned [Project Model](shared/project-model/README.md),
[Knowledge Model](shared/knowledge-model/README.md),
[Shared Document Model](shared/document-model/README.md),
[quality rules](shared/quality-rules/README.md), and
[terminology](shared/terminology/README.md). The bundle has no runtime
dependency on repository development material.
