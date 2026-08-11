# Project Design Checklist

## Implemented Guided Workflow

- [ ] A framing iteration is opened before new analysis or Canvas mutation.
- [ ] The complete necessary, non-duplicated question batch is written to the
      Canvas and presented before its count is recorded.
- [ ] `awaiting_framing_answers` persists across conversations and `status`
      directs the agent to the existing Canvas questions without creating a
      batch or iteration.
- [ ] Question batches may contain any non-negative count; relevance and
      downstream decision impact, not a numeric ceiling, control inclusion.
- [ ] Partial answers reduce only the pending count and preserve unanswered
      Canvas questions.
- [ ] Deferrals require explicit user intent and remain separate from answers.
- [ ] A technical transition request or conversation change does not count as
      an answer or deferral.
- [ ] A batch cannot close until answers plus explicit deferrals cover every
      presented question.
- [ ] A completed batch and a completed iteration are separate transitions.
- [ ] The state contains only workflow-control metadata and no project
      description, source content, question text, answer text, or Canvas body.
- [ ] Migration from older state schemas is idempotent, preserves existing
      choices and history, and enters cautious recovery when framing state is
      ambiguous.

## Forecast Contract — Not Yet Implemented

- [ ] The request is classified as complete workflow, one specialized skill,
      or an explicit subset.
- [ ] Only relevant specialized skills are selected.
- [ ] The proposed order respects dependencies between selected skills.
- [ ] `project-framing` supplies the Project Canvas before downstream design
      when framing is required.
- [ ] `functional-design` and `technical-design` may be ordered or parallelized
      only when their inputs and unresolved questions permit it.
- [ ] Design skills remain distinct from future document-restitution skills.
- [ ] Each document skill receives only its corresponding validated business
      artefact and remains directly callable.
- [ ] `project-design` owns global step selection, artefact transmission, and
      cross-step consistency but produces neither business content nor
      documents.
- [ ] Reliable new information may trigger a traceable return to an earlier
      stage without silently rewriting validated artefacts.
- [ ] Shared facts, assumptions, decisions, and questions remain consistent
      across artefacts.
- [ ] Specialized methodology is not duplicated in orchestration.
- [ ] A single specialized concern is routed to its dedicated skill.
- [ ] No unsupported project information is introduced.
- [ ] Core orchestration remains independent from Spec Kit and platform
      runtimes.

## Future Methodology

`TO BE DEFINED`: detailed routing rules, dependency resolution, parallel-step
governance, cross-artefact reconciliation, documentary routing, output
structure, and completion criteria.
