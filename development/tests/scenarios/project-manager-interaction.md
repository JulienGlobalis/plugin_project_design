# Project Manager Interaction Replay

Apply this supplemental scenario to all four permanent fixtures. Read every
source named in the fixture README; do not supply expected observations or
checklists to the executing agent. Keep test roots and raw outputs outside the
permanent corpus. This scenario adds no fifth fixture.

## Request

Use `project-design` to frame the supplied project. I explicitly consent to
using the plugin and creating its workspace in the test root. I select
`project-framing`, Markdown-only delivery, and keeping sources in place. Help
me decide and present the first Canvas and the necessary questions.

## First Interaction

Save the raw conversational response and Canvas before evaluation. Inspect
the real workflow phase and pending count. Evaluate with the repository,
project-design, and project-framing checklists. Verify grounded recommendations,
preserved unresolved decisions, complete necessary questions, absence of
duplicate intake, the saved readiness block, and pending-answer state.
Check that each counted question is independently answerable; thematic groups
must not collapse separate decisions into a single pending counter.

## Follow-up Interaction

Answer one identified question with a source-supported clarification and
explicitly defer a different identified question. Request advice on another
without answering it. Resume in a new conversation. Check that only the
answered/deferred questions reduce the pending count, deferred questions are
visibly distinct, active wording is preserved, and advice does not silently
become a Decision. If sources cannot support a clarification, provide an
explicit fictional authorized change as test input and keep it with the raw
transcript; never infer it from expected observations.

## Functional Design Extension

Only with a separately validated ready Canvas, invoke `functional-design`
directly. Request a recommended review order and help deciding a missing
behavior, then approve a traceable change. Verify supported consequences,
stable IDs, preserved unaffected content, and no invented backlog priority.
Run review-only mode separately and compare file hashes before and after.

## Record Boundaries

Report which phases actually ran. A first-interaction replay does not validate
cross-conversation answers, native question widgets, full functional-design
creation/update, user acceptance, or a second platform. Mark these pending
unless executed. No output becomes a Golden Output without human approval.
