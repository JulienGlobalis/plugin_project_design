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

`project-design` implements the guided entry into the plugin: it presents the
skills, obtains explicit consent, initializes `_project-design/`, proposes
step 1 `project-framing` by default, captures document preferences, persists
each required transition, and hands work to an implemented specialized skill.
Complete cross-step orchestration remains future work.

The four specialized business skills produce format-neutral business
artefacts and own project knowledge. The four `document-` skills
consume their corresponding validated artefacts and apply document structure,
formatting, an optional template, and an output format without changing
business knowledge when their methodology is implemented.

The mandatory naming convention is:

```text
<discipline>          -> business artefact
document-<discipline> -> corresponding document
```

## Invocation and Project Workspace

Every skill starts with a concise launch brief naming the selected skill,
available and missing inputs, expected deliverables, and any required or
optional user-supplied model or template. Placeholder skills explicitly state
that they cannot generate their forecast output.

Durable Markdown outputs are grouped under `_project-design/` at the root of
the target project. Business artefacts use stable top-level names such as
`_project-design/project-canvas.md`; documentary Markdown outputs use
`_project-design/documents/`. This is a storage convention only and does not
change artefact ownership or merge business and document responsibilities.
`project-design` asks for explicit confirmation before its idempotent
initialization script creates this workspace and `documents/`; refusal creates
nothing. Its state machine stores the current phase and non-business choices in
`_project-design/project-design-state.json`, rejects skipped transitions, and
allows a new conversation to resume from the recorded next action.

## Current Status

The guided `project-design` entry, the `project-framing` business methodology,
and the `document-project-canvas` documentary methodology are implemented.
Manual validation of the combined chain remains pending. The other six skill
entries are explicit placeholders; complete orchestration is also pending.

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
