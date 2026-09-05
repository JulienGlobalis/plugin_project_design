# Functional Design Checklist

Use this checklist with the repository-wide checklist for every
`functional-design` run.

## Inputs and Evolution

- [ ] A validated Project Canvas or equivalent baseline is identified.
- [ ] Existing functional content and every supplied change input are used.
- [ ] Stable identifiers are preserved; new identifiers are unique and are
      never reused for another meaning.
- [ ] The current body states the applicable behavior and the concise change
      history identifies affected IDs, change type, and known reason.
- [ ] No version, date, owner, approval, status, or Decision is invented.
- [ ] Unaffected sections survive an update unchanged in meaning.

## General Specifications

- [ ] Actors and functional roles remain distinct from project Stakeholders.
- [ ] Global Processes connect triggers, Actors, stages, outcomes, features,
      and applicable rules at a useful depth.
- [ ] The product-module-feature inventory uses only meaningful hierarchy
      levels and remains a coverage index rather than a backlog.
- [ ] Global Business Rules are defined once and referenced from features.

## Detailed Features

- [ ] Every inventory feature has one detailed specification or a justified
      deferral, and every detailed feature occurs in the inventory.
- [ ] Each feature covers supported general information, nominal behavior,
      alternative valid scenarios, errors and exceptions, acceptance
      criteria, questions and Decisions, interfaces and fields, rules, and
      messages.
- [ ] Alternative valid scenarios are not mislabeled as errors.
- [ ] Errors and exceptions preserve supported trigger, handling, resulting
      state, visible feedback, and message references.
- [ ] Acceptance criteria are observable, testable, traceable, and contain no
      invented threshold or test data.
- [ ] Interfaces and fields describe functional behavior without prescribing
      visual design, widgets, database types, APIs, or implementation.
- [ ] Feature-specific rules do not duplicate global rules.

## Messages, Semantics, and Traceability

- [ ] Every message is defined once in the global catalog and referenced by a
      stable ID from affected features, fields, or error cases.
- [ ] Exact message wording is used only when supplied or approved.
- [ ] Needs, Capabilities, Processes, Requirements, Business Rules, features,
      and acceptance criteria are not conflated.
- [ ] Established, Provisional, and Unresolved content remains distinct.
- [ ] Existing, Target, and Transition behavior remains distinct.
- [ ] Material behavior traces to the Canvas, Project View, Decision, or
      supporting evidence.
- [ ] Contradictions remain unresolved until authoritative resolution.

## Boundaries and Delivery

- [ ] No unsupported Actor, permission, requirement, behavior, value,
      priority, estimate, date, owner, or Decision is invented.
- [ ] Framing defects are returned to `project-framing` rather than silently
      changing the Canvas.
- [ ] The artefact contains no architecture, API design, database schema,
      technology, component, infrastructure, deployment choice, epic, user
      story, task, sprint, estimate, priority, or release plan.
- [ ] Documentary format and layout remain outside this skill.
- [ ] Technical-design and backlog-preparation readiness are assessed
      separately without a completeness score.
- [ ] The output is `_project-design/functional-design.md`, created only after
      workspace consent and never silently overwritten.
- [ ] The skill remains independently callable and Spec Kit independent.

## Project Manager Support

- [ ] Apply the interaction criteria in the skill runtime quality checklist.
- [ ] Run the [interaction replay](../scenarios/project-manager-interaction.md)
      and distinguish executed phases from pending manual validation.
