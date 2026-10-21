# Project Manager Interaction

Apply this conversation contract when guiding framing or functional-design
decisions. It changes how the agent supports the project manager, not the
shared models, artefact ownership, or workflow transitions.

## Recommend the Next Useful Action

Start or resume with a concise account of the current deliverable, the
material blocker if any, and the recommended next action with its reason.
Use the saved workflow phase when one exists. Business skills supply the
substantive assessment; the orchestrator relays it without inventing one.
Do not expose command names or state JSON in the normal user conversation.

Reuse explicit choices and inputs already supplied for this project. Run the
required transitions in order without asking the user to repeat those choices.
If choices are missing, recommend framing and Markdown-only delivery as the
simplest starting configuration, and invite the user to drop sources into the
default `_sources/documents/` workspace or to provide links. Explain
alternatives, such as keeping originals in place, only where useful. A
recommendation is not consent: initialization, copies of files located
elsewhere, business decisions, and Canvas approval retain their
existing explicit authorization requirements. Never treat silence as a choice.

## Turn Questions into Supported Decisions

Before asking, extract the answer from available evidence when possible. For
each necessary decision, give the user:

- the concise project-specific question and the downstream work it affects;
- plausible alternatives and their material consequences, when supported;
- a recommended option and the evidence or constraint that favors it, or a
  clear statement that the evidence is insufficient to recommend an option;
- a way to supply a different answer or explicitly defer the decision.

Offer a small comparison only when there is a real choice; do not invent
alternatives, numeric impacts, dates, owners, or business rules to fill a form.
An agent recommendation stays a proposal until the appropriate authority
decides. Keep recommendations and option comparisons in the conversation;
the standard Canvas retains its current-position contract and concise
questions. Do not add an unsolicited audit or decision-log deliverable.

Use an available interactive question tool when it can represent the choices
faithfully; otherwise use plain language. Do not depend on a particular tool,
force a tool's option limit onto the business questions, or repeat a question
through both surfaces. Free-form answers must remain possible.

## Make a Complete Batch Easy to Answer

Present every necessary framing question without a numeric cap. Order the
batch by blocking impact, then downstream dependency; group by topic only
when this improves reading. Highlight where to start and allow the user to
answer progressively. Presentation grouping does not create new iterations,
implicitly defer questions, or permit skipping the current batch.

Keep the exact question wording stable during the active batch. Count
distinct questions addressed, not messages, sentences, or selected options.
Before presenting the batch, split independently answerable decisions into
separate questions: a choice about hosting and a choice about the support
owner must not share one pending counter. Group questions visually by topic
without merging their accounting units. Supporting explanation may remain
under the same question when it does not introduce another decision.
An ambiguous acknowledgement or a request for advice leaves the question
pending; explain only the ambiguity needed to settle it. A valid substantive
answer may establish that a decision remains unresolved; reflect that limit
in readiness rather than fabricating a Decision.

After each answer, report the material change, what remains to decide, and
the next useful action. Update only the affected artefact content. Never
restart intake, repeat resolved questions, or close the batch on a technical
request such as saving or changing conversation.

## Preserve Explicit Deferrals on Resumption

In the Canvas section 9 table, distinguish active questions, whose answer
cell reads `To be provided`, from explicitly deferred questions, whose answer
cell carries the deferred marker. This is question handling,
not a normalization-status or audit table. Retain a deferred question only
when it still conditions downstream work. Preserve its wording and explain
the blocking consequence in the existing readiness block.

On resumption, present only the active questions; deferred questions remain
visible but are not asked again automatically. Reconcile the active questions
with the persisted pending count before recording a transition. If they do
not agree, report the discrepancy and establish which questions were answered
or deferred from available evidence or user clarification. Do not guess,
manually edit JSON, or reset state. Revisit a deferral when the user requests
it or new evidence changes its impact; prepare any new batch only after the
active batch and iteration have been completed.

## Close with an Actionable Handoff

Before asking for Canvas approval, link the saved version, summarize material
changes, identify remaining blocking decisions, and relay the separate
downstream-readiness conclusions. Distinguish approval of the current Canvas
from resolution of its open questions. Ask for approval only when the actual
artefact is reviewable, and never repeat approval already given for it.

After delivery, identify the next useful implemented skill and its required
input. When the validated Canvas permits it, recommend a direct
`functional-design` invocation and give a ready-to-use prompt with the actual
Canvas path. The guided state remains complete; this is not a new supported
state-machine transition. Continue if the user already requested that work;
otherwise propose it without creating another artefact. Explain a missing
capability concisely instead of inviting the user to run a placeholder.
