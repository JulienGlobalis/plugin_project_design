# Incomplete Information Scenario

## Fixture

Use every source artefact listed in the
[incomplete-project fixture README](../fixtures/incomplete-project/README.md)
as project input. Do not provide the README itself.

## Request

```text
Use <selected-skill> to analyze and structure the supplied project material.
Produce the artefact supported by the current skill methodology and make
uncertainty visible.
```

## Applicable Skills

Run this scenario for `project-framing`, `functional-design`,
`document-project-canvas`, and `project-design`, and for any skill whose
handling of missing information or unsupported invention changes.

## Expected Observations

- Supplied facts remain intact and attributable to the source.
- Missing information becomes explicit.
- Open questions are actionable and do not masquerade as requirements.
- Assumptions remain distinct from facts.
- Ambiguous user populations are not silently merged.
- No requirement, priority, volume, owner, or constraint is invented.
- The output stays within the selected skill's responsibility.

## Project Framing-Specific Observations

- The primary output is a Project Canvas with all ten required sections.
- A useful first Canvas is produced before requesting non-blocking details.
- Existing handling remains distinct from the proposed workspace.
- Business Context covers the mailbox, messages, spreadsheet, lost requests,
  workload concern, and incomplete timing without inventing a deadline.
- Objectives and Expected Value do not invent measures or benefits beyond the
  stated reduction of lost requests and workload visibility.
- Project Stakeholders remain distinct from users, and missing requester,
  security, support, legal, and data-governance representation stays visible.
- Users are not silently normalized across ambiguous requester, volunteer,
  coordinator, service-team, and site terms.
- Validated MVP and authorized Outside MVP remain explicit; preliminary or
  undecided Capabilities are omitted and no complete split is invented.
- Technical Constraints include only known environment or preferences and do
  not become a technical architecture.
- Indispensable missing scope, ownership, terminology, success criteria,
  service targets, integrations, and governance use `To be defined` or a
  concise Decision question.
- Confirmed current handling problems remain distinct from future Risks.
- The Decisions section does not promote service-manager preferences to
  authoritative Decisions.
- Ambiguous terms such as request, ticket, case, requester, and site are not
  normalized silently.
- Questions are limited to Decisions conditioning functional design, technical
  design, or backlog preparation; classification labels remain internal.
- Recommended next steps prioritize scope authority, participant coverage,
  terminology, and critical information requirements without inventing a
  delivery plan.
- Success Criteria states missing measures explicitly without inventing
  thresholds.
- The Canvas identifies responsible downstream work without performing
  detailed functional or technical design.

## Document Project Canvas-Specific Observations

- The final document preserves all explicit gaps and does not fill empty
  sections through presentation content.
- Ambiguous terms and undecided positions are not presented as defining the
  Project; indispensable items become concise Questions.
- The documentary hierarchy makes the ten sections reviewable without adding
  metadata, owners, dates, or approval status.
- The requested format is native and verified.

## Functional Design-Specific Observations

- A validated Canvas or equivalent baseline is required before detailed work;
  blocking framing gaps are returned upstream.
- The feature inventory and detailed sections contain only supportable
  behavior; absent prerequisites, rules, fields, and acceptance conditions
  remain `To be defined` or focused questions.
- Ambiguous requester, volunteer, coordinator, service-team, and site roles
  are not silently merged or assigned invented permissions.
- Message and interface entries use stable IDs without inventing exact wording
  or a complete data model.
- Backlog preparation may remain not ready even when some functional analysis
  can proceed.

## Project Manager Interaction

For guided decision support and progressive answers, also run the
[interaction replay](project-manager-interaction.md) using this same fixture.
