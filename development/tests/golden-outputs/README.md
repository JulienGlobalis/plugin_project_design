# Golden Outputs

This directory is reserved for manually approved reference artefacts.

No golden output is approved yet. Detailed skill methodologies and their
reference artefacts are `TO BE DEFINED`.

## Approval Requirements

A new or updated golden output requires explicit human approval. Store it
under:

```text
<skill>/<scenario>/reference.md
```

Accompany each reference with `approval.md` containing:

- scenario and fixture;
- skill;
- source commit;
- approving reviewer;
- approval date;
- supported methodology version;
- reason for approval;
- known limitations.

Reference comparison evaluates structure, captured information, reasoning,
traceability, completeness, and boundaries. Identical wording is never
required.

Never generate, approve, or replace a golden output automatically. A candidate
remains temporary test output until the approval record exists.
