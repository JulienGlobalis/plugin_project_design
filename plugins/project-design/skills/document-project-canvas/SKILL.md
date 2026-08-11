---
name: document-project-canvas
description: Create, format, and validate a human-facing Project Canvas document from the validated Project Canvas business artefact produced by project-framing. Use for native Markdown, Microsoft Word, or Google Docs delivery, including requests to apply a compatible supplied template or to run documentary restitution immediately after project framing. Preserve all business meaning, status, Decisions, contradictions, questions, readiness, and traceability without adding or resolving project knowledge.
---

# Document Project Canvas

## Status

IMPLEMENTED METHODOLOGY VERSION 0.1 — MANUAL USER VALIDATION PENDING

## Purpose

Transform one validated Project Canvas business artefact into a readable,
reviewable, and reusable document without changing its knowledge.

Own document structure, presentation, template application, format creation,
and document-level quality only. Keep `project-framing` as the sole owner of
the Canvas business content.

## Invocation Brief and Delivery

Before inspecting the artefact, apply the shared
[Invocation Brief and Project Workspace Delivery contract](../../shared/quality-rules/README.md).
State briefly that `document-project-canvas` is being used, identify the
validated Canvas and requested format, name the document that will be
generated, and tell the user whether a template is required, optional, or
replaced by the default professional structure. A compatible template is
optional unless the user explicitly requires one.

Save a generated Markdown document to
`_project-design/documents/project-canvas.md` at the target project root. When
an external format is requested, also save any durable Markdown source that is
actually generated for that delivery under this directory; do not create an
artificial Markdown duplicate solely to satisfy the storage convention.
Save a local Word delivery by default as
`_project-design/documents/project-canvas.docx`. Deliver a native Google Doc
through its verified Google Drive link.

## Guided Workflow State

Remain independently callable, but when
`_project-design/project-design-state.json` exists or the user invoked the
guided plugin flow, read it through
`../project-design/scripts/workflow.py status` before document work. Proceed
only when the phase is `awaiting_document`. Reuse the recorded format,
template mode, and template reference without asking again.

After native verification and delivery, run `complete-document` with the
verified `.docx` path or native Google Docs URL. Do not report the guided flow
as complete unless that transition succeeds. Never place business content or
document body text in the state file.

## Required Input

Require:

- the validated Project Canvas artefact produced by `project-framing` or an
  equivalent artefact that satisfies the same contract;
- the requested output format when the user does not want native Markdown.

Accept when supplied:

- intended audience and review purpose;
- output language;
- document title and approved metadata;
- a compatible template, visual identity, or presentation constraints;
- confidentiality, accessibility, or delivery constraints.

Do not require optional presentation information before producing a useful
default document. Never infer missing business content from presentation
instructions.

## Workflow

### 1. Verify the Artefact Boundary

Confirm that the input is a Project Canvas rather than raw project sources or
an unstructured request. It must represent or explicitly qualify all ten
business sections:

1. Business Context;
2. Objectives and Expected Value;
3. Project Stakeholders;
4. Users;
5. Functional Scope;
6. Technical Constraints;
7. Risks;
8. Decisions;
9. Questions;
10. Success Criteria.

Also preserve any downstream-readiness statement and Knowledge Basis supplied
with the artefact.

If material content is absent, contradictory, or unresolved but correctly
labelled, keep it that way. If the input is not a valid Canvas, do not repair
it through documentary editing. Request a corrected artefact or route the
business work to `project-framing`.

### 2. Resolve the Documentary Request

Use native Markdown when no output format is requested. Otherwise support:

- native Markdown;
- Microsoft Word (`.docx`);
- native Google Docs.

Use the requested language. When none is requested, preserve the Canvas
language. Do not silently translate project-specific Domain Terms.

Use a supplied template only after confirming that it can represent every
required section, explicit gap, status, contradiction, Decision, question,
readiness statement, and traceability element. Treat blank template fields as
presentation slots, not permission to invent content.

When no template is supplied, apply the default structure in
[document structure](references/document-structure.md).

A template choice may already have been captured by `project-design` or
`project-framing`. Reuse it without asking again. Otherwise, for Word or Google
Docs, ask whether the user wants to supply a local template, a Google Drive
template link, or use the default professional structure.

### 3. Build a Content-Preservation Map

Before formatting, map every material Canvas element to one document
location. Preserve:

- section membership and logical relationships;
- Established, Provisional, and Unresolved status where material;
- Existing, Target, and Transition perspective where material;
- opposing positions and unresolved contradictions;
- authoritative Decisions separately from Assumptions, Options, preferences,
  and proposals;
- Risks separately from confirmed Issues;
- MVP, Outside MVP, explicit exclusions, future Options, and Unresolved Scope;
- question classifications, known authority, and next clarification action;
- source basis or traceability references;
- downstream-readiness qualifications.

Reorder content only to improve documentary readability. Do not summarize,
merge, deduplicate, shorten, or rewrite when doing so could change meaning,
authority, status, qualification, or traceability.

### 4. Compose the Document

Apply the rules in [document structure](references/document-structure.md).

Use headings for the ten required sections. Use prose for context and
rationale, and tables for comparison, status, authority, Scope, Decisions,
Risks, questions, success criteria, or traceability when tables improve
review.

Keep the document concise and stakeholder-facing, but preserve every material
Canvas statement. Include only metadata supplied by the artefact or user.
Never invent an author, sponsor, owner, version, approval status, date,
classification, or review decision.

### 5. Produce the Requested Format

Follow [format guidance](references/format-guidance.md).

For external formats, use the platform's available native document tooling.
Do not simulate a Word or Google Docs delivery with renamed Markdown, HTML, a
plain-text approximation, or an unverified upload.

If the requested external format cannot be created in the active environment,
state the limitation and offer the validated Markdown document. Do not claim
that the requested format was produced.

### 6. Verify Content and Presentation

Use the runtime [quality checklist](references/quality-checklist.md).

Compare the finished document with the input artefact and confirm that every
material element appears exactly once or through an explicit cross-reference.
For Word, render and inspect every page. For Google Docs, read back the native
document structure and inspect the visible result when the platform permits.

Correct documentary defects only. Return business-content defects to
`project-framing`; never fix them silently in the document.

### 7. Deliver

Deliver the Markdown content, Word file, or Google Docs link requested by the
user. State:

- the produced format;
- whether the default structure or a supplied template was used;
- the document-validation result;
- any unresolved documentary limitation.

For Markdown delivery, report the `_project-design/` relative path when the
file was saved. For external delivery, report any durable companion Markdown
path only when such a file was actually generated.

Do not present the document as business-approved merely because its
formatting passed validation.

For a guided workflow, record the verified delivery with the state-machine
command before reporting completion. If the command rejects the file or URL,
keep the phase `awaiting_document` and correct the delivery or report the
blocker.

## Boundaries

- Do not analyze raw project sources or perform project framing.
- Do not add, remove, reinterpret, approve, reject, prioritize, or resolve
  business or technical knowledge.
- Do not change a Decision, Assumption, Option, Risk, Issue, Requirement,
  Scope position, success criterion, question, status, or traceability basis.
- Do not create missing content to fill a document or template.
- Do not hide uncertainty, contradiction, non-readiness, or absent authority
  for visual simplicity.
- Do not modify the Canonical Domain Model, Knowledge Model, Project Model, or
  Project Canvas business contract.
- Do not depend on development-only resources.
- Remain independently callable without the `project-design` orchestrator.

## References

- [Shared Document Model](../../shared/document-model/README.md)
- [Document structure](references/document-structure.md)
- [Format guidance](references/format-guidance.md)
- [Runtime quality checklist](references/quality-checklist.md)
- [Project Canvas business contract](../project-framing/references/project-canvas.md)
- [Asset conventions](../../shared/assets/README.md)
- [Shared quality rules](../../shared/quality-rules/README.md)
- [Terminology](../../shared/terminology/README.md)
