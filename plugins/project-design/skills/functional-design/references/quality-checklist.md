# Functional Design Quality Checklist

## Inputs and Baseline

- [ ] Review order is recommended from dependencies and uncertainty without
      inventing backlog priority or requiring approval for every feature.
- [ ] Material decisions expose grounded alternatives and consequences;
      recommendations never silently replace validated behavior.
- [ ] Answers update affected identifiers only; review-only mode writes nothing.

- [ ] A validated Project Canvas or equivalent project position is identified.
- [ ] Every supplied relevant source and existing Functional Design is used.
- [ ] Canvas Scope, Decisions, Constraints, Risks, and unresolved Questions are
      not silently changed.
- [ ] A blocking framing defect is returned to `project-framing`.

## Living Artefact

- [ ] Existing stable identifiers are preserved across updates.
- [ ] New identifiers are unique, resolvable, and never reused for another
      meaning.
- [ ] Updates affect only justified sections and preserve unaffected content.
- [ ] Each change is classified and recorded with known affected identifiers
      and reason or source.
- [ ] No date, version, owner, approval, or decision status is invented.
- [ ] Replaced or deprecated behavior is not silently deleted from history.

## General Specifications

- [ ] Actors and roles describe functional participation and remain distinct
      from Stakeholders.
- [ ] Global Processes connect triggers, actors, stages, outcomes, features,
      and rules at appropriate depth.
- [ ] The inventory distinguishes products, modules, and features only when
      those hierarchy levels have project meaning.
- [ ] The inventory remains a coverage index rather than a backlog.
- [ ] Global Business Rules are defined once and referenced consistently.

## Feature Specifications

- [ ] Every inventory feature has one detailed section or a justified
      deferral, and every detail maps to the inventory.
- [ ] General information preserves supported objectives, actors,
      prerequisites, postconditions, dependencies, maturity, and traceability.
- [ ] Nominal behavior is observable and independent from implementation.
- [ ] Alternative valid scenarios remain distinct from errors and exceptions.
- [ ] Errors and exceptions state supported triggers, handling, resulting
      states, and feedback without inventing recovery behavior.
- [ ] Acceptance criteria are observable, testable, traceable, and contain no
      invented threshold or test data.
- [ ] Open Questions are material, actionable, and not disguised proposals.

## Interfaces, Fields, Rules, and Messages

- [ ] Interfaces describe functional purpose, actors, actions, outcomes, and
      states without prescribing visual or technical design.
- [ ] Field definitions distinguish expected information, requirement,
      editability, visibility, source or default, validation, and behavior.
- [ ] Field-level rules reference stable Rule and Message IDs where relevant.
- [ ] Feature-specific rules do not duplicate or contradict global rules.
- [ ] Every message is defined once in the global catalog and referenced by
      affected features.
- [ ] Exact message wording is used only when supplied or approved.

## Semantics and Traceability

- [ ] Needs, Capabilities, Processes, Requirements, Business Rules, features,
      and acceptance criteria are not conflated.
- [ ] Established, Provisional, and Unresolved information remains
      distinguishable.
- [ ] Existing, Target, and Transition behavior remains distinguishable.
- [ ] Material statements trace to the Canvas, Project View, Decision, or
      supporting evidence.
- [ ] Conflicting behavior remains unresolved until authoritative resolution.
- [ ] No unsupported actor, permission, requirement, rule, behavior, value,
      owner, priority, date, or Decision is invented.

## Boundaries and Delivery

- [ ] The artefact contains no architecture, API design, database schema,
      framework, component, infrastructure, or deployment choice.
- [ ] The artefact contains no epic, user story, task, priority, estimate,
      sprint, or release plan.
- [ ] The skill owns no document template, layout, export, or external format.
- [ ] Founded Canvas adjustments are reported for upstream review rather than
      silently applied.
- [ ] Technical-design and backlog-preparation readiness are assessed
      separately without a completeness score.
- [ ] The artefact is saved under `_project-design/functional-design.md` only
      after workspace consent and without silent overwrite.
- [ ] The skill remains independently callable and Spec Kit independent.
