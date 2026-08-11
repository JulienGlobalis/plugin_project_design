# Repository-Wide Quality Checklist

## Source Fidelity

- [ ] Every stated fact is supported by supplied source material.
- [ ] Source meaning, qualifications, and conflicts are preserved.
- [ ] No requirement, constraint, actor, priority, estimate, or decision is
      invented.

## Traceability

- [ ] Material claims can be traced to their source.
- [ ] Facts, interpretations, assumptions, proposals, decisions, and open
      questions remain distinguishable.
- [ ] Derived content identifies its supporting evidence and reasoning.

## Consistency

- [ ] Terms and concepts are used consistently.
- [ ] Contradictory sources remain visible until a justified decision resolves
      them.
- [ ] Related artefacts do not silently disagree.

## Completeness

- [ ] All information relevant to the selected skill is represented or
      explicitly excluded with a reason.
- [ ] Missing information and incomplete evidence are visible.
- [ ] Required sections are present according to the current methodology.

## Assumptions and Questions

- [ ] Assumptions are explicit, testable, and not represented as facts.
- [ ] Open questions identify a concrete information or decision need.
- [ ] Uncertainty is not hidden by confident wording.

## Skill Boundaries

- [ ] The output addresses the selected skill's responsibility.
- [ ] Out-of-scope concerns are handed off or noted without implementing
      another skill's methodology.
- [ ] The output does not require Spec Kit or a platform-specific runtime.

## Invocation and Delivery

- [ ] `project-design` obtains explicit user consent before creating the
      `_project-design/` workspace, and a refusal creates nothing.
- [ ] Workspace initialization is idempotent and creates no placeholder
      artefact or document.
- [ ] The guided workflow creates and resumes
      `_project-design/project-design-state.json` without resetting it.
- [ ] Every attempted transition outside its required phase fails without
      advancing or corrupting the state.
- [ ] The state contains control metadata only and no source content, project
      description, question, answer, or business artefact content.
- [ ] Stage selection explicitly proposes step 1 `project-framing` by default
      and does not present placeholder stages as implemented.
- [ ] Before substantive work, the response briefly names the selected skill,
      available and missing inputs, expected deliverables, and required or
      optional models or templates.
- [ ] A placeholder clearly states that it generates no artefact or document.
- [ ] Every durable generated Markdown file is stored beneath
      `_project-design/` at the target project root.
- [ ] Business artefacts and documentary representations use their distinct
      default paths.
- [ ] No existing file is silently overwritten and no unavailable save is
      reported as successful.
- [ ] The workflow reaches `complete` only after explicit Canvas approval and,
      when requested, a verified native document reference.

## Methodological Quality

- [ ] Structure supports review and future reuse.
- [ ] Reasoning is proportionate to available evidence.
- [ ] Meaningful risks, dependencies, and unresolved issues remain visible.
- [ ] Stylistic polish does not conceal methodological gaps.
