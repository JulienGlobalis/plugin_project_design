# Validation and Tests

The repository uses a lightweight, documentation-first testing strategy. Tests
evaluate methodological quality rather than exact wording.

Start with [TESTING.md](TESTING.md), which defines the mandatory workflow for
skill changes and releases.

## Test Areas

- [Fixtures](fixtures/README.md): the four permanent anonymized source sets.
- [Scenarios](scenarios/README.md): platform-independent test instructions.
- [Quality checklists](quality-checklists/README.md): repository-wide and
  skill-specific evaluation criteria.
- [Golden outputs](golden-outputs/README.md): human-approved reference
  artefacts.
- [Regression](regression/README.md): difference classification and review.
- [Execution history](executions/README.md): records of completed test runs.
- [Manual validation](manual/README.md): one lightweight real-project test
  file per implemented skill.

Structural validation of manifests and skill front matter remains required in
addition to the methodology tests described here.
