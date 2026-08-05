# Project Framing Checklist

## Input Use and Interaction

- [ ] Every supplied source artefact is considered.
- [ ] The skill uses an existing Project View when supplied and does not
      silently override it.
- [ ] Raw sources are organized according to the Knowledge Model and Project
      Model without introducing a private model or new layer.
- [ ] The skill does not ask for information already available.
- [ ] A useful first Project Canvas is produced without a preliminary
      questionnaire when the available information permits it.
- [ ] Any preliminary questions are limited, high-value, and explain why the
      answer matters.
- [ ] The user can continue with an explicitly incomplete Canvas.

## Required Project Canvas Structure

- [ ] The primary output is identified as a Project Canvas.
- [ ] Business Context is present or explicitly insufficiently informed.
- [ ] Objectives and Expected Value is present or explicitly insufficiently
      informed.
- [ ] Project Stakeholders is present or explicitly insufficiently informed.
- [ ] Users is present or explicitly insufficiently informed.
- [ ] Functional Scope is present and separates MVP, Outside MVP, and
      Unresolved Scope.
- [ ] Technical Constraints is present or explicitly insufficiently informed.
- [ ] Risks is present or explicitly insufficiently informed.
- [ ] Decisions is present or explicitly insufficiently informed.
- [ ] Questions is present and uses the required impact classifications.
- [ ] Success Criteria is present or explicitly insufficiently informed.

## Content and Semantic Quality

- [ ] The Canvas clarifies and structures the expression of need rather than
      merely summarizing source documents.
- [ ] The business context and relevant Existing situation are clear and
      source-supported.
- [ ] Objectives remain distinct from Needs, outcomes, value, Requirements,
      and measures.
- [ ] Expected value is not invented from a proposed solution.
- [ ] Stakeholders remain distinct from Actors and users.
- [ ] User populations, roles, Needs, rights, and responsibilities are not
      enriched beyond the evidence.
- [ ] MVP, explicit exclusions, deferred items, future Options, and unresolved
      boundaries remain distinct.
- [ ] No MVP or outside-MVP classification is invented.
- [ ] Business and technical Constraints remain distinct from preferences and
      proposed designs.
- [ ] Existing, Target, and Transition perspectives remain distinct.
- [ ] Decisions remain distinct from Options, Assumptions, and informal
      proposals.
- [ ] Risks remain distinct from confirmed Issues.
- [ ] Success criteria, measures, baselines, and targets are not invented.

## Information Quality and Traceability

- [ ] Established, Provisional, and Unresolved information is presented
      according to the Project Model.
- [ ] Facts, interpretations, Assumptions, proposals, Decisions, and Open
      Questions are not conflated.
- [ ] Contradictory information remains visible unless an authorized,
      traceable resolution exists.
- [ ] Material statements remain traceable through Project Model information
      and Knowledge Basis to source locations.
- [ ] Source absence is not presented as proof that information does not
      exist.
- [ ] No owner, date, volume, priority, Constraint, Business Rule,
      Requirement, Decision, value claim, or success criterion is invented.
- [ ] Required sections with material gaps state those gaps explicitly rather
      than receiving generic filler.

## Questions and Downstream Readiness

- [ ] Every unresolved question is concrete, project-specific, and
      actionable.
- [ ] Questions are classified as blocking, required before functional
      design, required before technical design, required before backlog
      preparation, or deferrable.
- [ ] A question may identify multiple affected stages when justified.
- [ ] Deferrable questions are not presented as immediate blockers.
- [ ] Question priority reflects decision impact, Risk, and dependency rather
      than missing detail alone.
- [ ] Owners or authorities are named only when known.
- [ ] The Canvas states whether functional design, technical design, and
      backlog preparation can proceed and which gaps qualify them.
- [ ] Readiness is qualitative and purpose-specific; no artificial 80-90%
      score or universal completeness claim is produced.
- [ ] The Canvas remains usable by the next applicable stage despite explicit
      non-blocking unknowns.

## Language and Artefact Usability

- [ ] The business artefact is format-neutral and contains no template,
      conversion, export, or final-document formatting logic.
- [ ] The Canvas uses the requested language.
- [ ] French output uses localized canonical terminology while keeping prose
      natural and professional.
- [ ] Project-specific Domain Terms remain faithful to source vocabulary.
- [ ] Missing requested-language terminology or fallback is explicit.
- [ ] Internal canonical identifiers and model mechanics do not burden normal
      stakeholder-facing prose.
- [ ] The default Canvas is autonomous, concise, structured, actionable, and
      suitable for stakeholder review.
- [ ] Any requested final document is handed to
      `document-project-canvas`; `project-framing` does not claim a document
      format capability.

## Boundaries, Adjustments, and Handoffs

- [ ] The output does not produce detailed products, modules, features,
      screens, exhaustive journeys, functional data models, exception
      catalogs, acceptance criteria, architecture, APIs, components,
      deployment design, or a complete backlog.
- [ ] Framing-relevant Requirements and Business Rules are included only at
      the level needed for context, boundaries, feasibility, governance,
      Risk, or handoff.
- [ ] Functional, technical, backlog, and document work is handed off without
      being executed.
- [ ] Any later Canvas adjustment is traceable, justified, limited, and does
      not silently rewrite validated information or Decisions.
- [ ] The skill remains independently callable, Spec Kit independent, and
      free of runtime dependency on development-only resources.
- [ ] The Canonical Domain Model, Knowledge Model, Project Model, and localized
      terminology remain unchanged.
