# Examples

## Purpose

This directory, `development/examples/`, is a versioned workspace for draft,
experimental, or not-yet-approved examples. It is outside the installable
plugin boundary.

Examples required by an installed skill to guide reasoning or reduce
unsupported invention belong under:

```text
plugins/project-design/skills/<skill-name>/references/
```

The relevant `SKILL.md` must link directly to each runtime example and explain
when it should be read. Do not create a plugin-level `examples/` directory
that no skill explicitly references.

## Promotion Rules

Promote a development example to a skill reference only when:

- it supports a repeated, validated reasoning or output pattern;
- it is concise enough to load only when needed;
- it contains no confidential or project-specific information;
- it does not reveal expected conclusions from the permanent fixtures;
- the skill instructions identify when the example is relevant.

Prefer focused examples and counterexamples over complete generated
deliverables. Golden Outputs remain test evidence under
`development/tests/golden-outputs/` and must not become runtime instructions.

Localized example assets must follow the conventions in the
[shared asset guidance](../../plugins/project-design/shared/assets/README.md).

No development or runtime examples are currently approved.
