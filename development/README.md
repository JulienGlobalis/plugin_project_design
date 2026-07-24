# Development Resources

This directory contains versioned resources used to design, validate, and
maintain `project-design`. It is outside the installable plugin boundary.

Contents:

- `PROJECT_CONTEXT.md`: cross-conversation continuity and current state;
- `PLAN.md`: project direction and roadmap;
- `SPEC.md`: current specification and acceptance criteria;
- `tests/`: fixtures, scenarios, quality checklists, manual tests, and
  execution evidence;
- `examples/`: draft or unapproved examples that are not installed with the
  plugin.

Do not place files required by an installed skill in this directory.
Installable methodology, models, terminology, and quality contracts belong
under `plugins/project-design/`.

Use the ignored root `.local/` directory for temporary, confidential, or
machine-specific work that must not be committed.
