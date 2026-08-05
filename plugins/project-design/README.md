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
consume their corresponding validated artefacts and will eventually apply
document structure, formatting, an optional template, and an output format
without changing business knowledge.

The mandatory naming convention is:

```text
<discipline>          -> business artefact
document-<discipline> -> corresponding document
```

## Current Status

Only `project-framing` has an implemented business methodology. The other
eight skill entries are explicit placeholders. In particular, the four
document skills do not yet contain document methodology, templates, examples,
generators, conversions, exports, or external integrations.

Future document formats are:

- Project Canvas, functional design, and technical design: native Markdown,
  Microsoft Word, or Google Docs.
- Product Backlog: native Markdown, Google Sheets, Microsoft Excel, Microsoft
  Word, or Google Docs.

These formats are forecast scope, not currently available capabilities.

## Shared Foundations

All skills use the bundle-owned [Project Model](shared/project-model/README.md),
[Knowledge Model](shared/knowledge-model/README.md),
[quality rules](shared/quality-rules/README.md), and
[terminology](shared/terminology/README.md). The bundle has no runtime
dependency on repository development material.
