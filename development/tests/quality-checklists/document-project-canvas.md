# Document Project Canvas Checklist

## Input and Responsibility

- [ ] Input is a validated Project Canvas artefact rather than raw project
      sources.
- [ ] The document adds, removes, resolves, approves, or reinterprets no
      project knowledge.
- [ ] Business-content defects are returned to `project-framing` instead of
      being silently repaired.
- [ ] The skill remains independently callable and does not perform global
      orchestration.
- [ ] The response first identifies `document-project-canvas`, the validated
      Canvas input, requested output, and whether a supplied template is
      required, optional, or replaced by the default structure.

## Content Preservation

- [ ] All ten required Canvas sections are visible or explicitly qualified.
- [ ] Every material artefact statement appears once or through an explicit
      cross-reference.
- [ ] Established, Provisional, and Unresolved status is preserved.
- [ ] Existing, Target, and Transition perspective is preserved.
- [ ] Stakeholders remain distinct from users.
- [ ] MVP, Outside MVP, exclusions, future Options, and Unresolved Scope remain
      distinct when present.
- [ ] Decisions remain distinct from Assumptions, Options, preferences, and
      proposals.
- [ ] Risks remain distinct from confirmed Issues.
- [ ] Contradictions, question classifications, readiness qualifications, and
      traceability remain visible.
- [ ] No metadata, owner, date, status, threshold, content, or approval is
      invented to fill the document or a template.

## Documentary Structure and Presentation

- [ ] The document has one clear title and a consistent sequential heading
      hierarchy.
- [ ] Prose and registers are selected for readability without changing
      meaning or relationships.
- [ ] Tables remain readable and preserve their logical rows, statuses, and
      qualifications.
- [ ] Missing information remains visible without decorative filler.
- [ ] Language and project-specific terminology match the validated artefact
      or explicit user instruction.
- [ ] A supplied template is compatible, introduces no stale facts, and does
      not suppress any required role.
- [ ] A format or template choice captured upstream is reused without asking
      the user again.
- [ ] In a guided flow, document generation starts only in
      `awaiting_document` and uses the state-recorded format and template.

## Format Verification

- [ ] The selected format is native Markdown, Microsoft Word, or Google Docs.
- [ ] Markdown headings, tables, links, and fences are valid when applicable.
- [ ] Word output is a real `.docx` and every rendered page is visually
      inspected when applicable.
- [ ] A local Word file uses `_project-design/documents/project-canvas.docx`
      or a justified qualified filename.
- [ ] Google Docs output is native and its structure and material text are
      read back after writing when applicable.
- [ ] The delivered file or link is the verified output; no external format
      is simulated or claimed without verification.
- [ ] The state becomes `complete` only after the verified `.docx` path or
      native Google Docs URL is accepted by `complete-document`.

## Validation Status

- [ ] Markdown delivery uses
      `_project-design/documents/project-canvas.md` or a justified qualified
      filename without silent overwrite.

Classify the result as `PASS`, `PASS WITH RESERVATIONS`, or `FAIL`. Documentary
validation does not constitute business approval of the Project Canvas.
