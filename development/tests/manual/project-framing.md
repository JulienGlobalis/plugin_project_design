# Project Framing and Project Canvas Document Manual Tests

Use this single file to prepare and review the sequential manual test of
`project-framing` followed by `document-project-canvas`.

Do not commit confidential project information, raw client data, a generated
client Canvas, or a completed client test record.

Allowed results:

- `PASS`
- `PASS WITH RESERVATIONS`
- `FAIL`

## Test Procedure

1. Invoke `project-design` and confirm that no directory is initialized before
   explicit consent.
2. Confirm plugin use, verify workspace initialization, and accept the default
   step 1 `project-framing`.
3. Inspect `_project-design/project-design-state.json`, start a new
   conversation if desired, and verify that the workflow resumes at the same
   phase without storing project or source content.
4. Select the optional documentary output and template mode, then select one
   case below.
5. Provide every listed source artefact, excluding the fixture `README.md`.
6. Use the supplied prompt or the applicable entry in the `Prompt` column
   without adding the expected observations or this checklist to the model
   context.
7. Preserve the initial skill launch brief and verify that it identifies the
   skill, inputs, deliverables, and required or optional models or templates.
8. Verify that durable Markdown outputs are grouped under `_project-design/`
   at the target project root.
9. Complete at least one focused question-and-answer iteration and preserve
   the progressively updated Canvas.
10. Preserve the generated Project Canvas artefact before documentary
   restitution.
11. Invoke `document-project-canvas` with that artefact and the documentary
   prompt below. Preserve the produced document separately.
12. Complete the case controls and the bilingual verification grid against
   both the artefact and final document.
13. Record concrete evidence, the result, and any reservations.
14. Return the completed results, generated Canvas, and final document for the
   intervention report without committing confidential material.

## Documentary Prompt

Use this prompt after the selected case has produced its Project Canvas:

```text
Use document-project-canvas to transform the supplied validated Project
Canvas into a final Project Canvas document in [format]. Preserve every
material statement, status, lifecycle perspective, contradiction, Decision,
question classification, readiness qualification, and traceability reference.
Apply the default professional structure unless a compatible template is also
supplied. Do not add, remove, resolve, approve, or reinterpret project
knowledge. Verify the finished document before delivery.
```

Replace `[format]` with `Markdown`, `Microsoft Word`, or `Google Docs`.
Use Markdown when the format itself is not under test.

## PF-MAN-001 — Incomplete Project

**Objective:** verify that the skill produces a useful ten-section Project
Canvas from incomplete sources without inventing missing Scope, ownership,
technical Constraints, success criteria, or Decisions.

**Data to provide:**

- `development/tests/fixtures/incomplete-project/context-note.md`
- `development/tests/fixtures/incomplete-project/discovery-workshop.md`
- `development/tests/fixtures/incomplete-project/service-team-message.md`
- `development/tests/fixtures/incomplete-project/technical-intake.md`
- `development/tests/fixtures/incomplete-project/vocabulary-notes.md`

**Prompt:**

```text
Use project-framing to analyze all supplied sources and produce the Project
Canvas in English. Preserve uncertainty and ambiguous terminology, distinguish
the current handling from the proposed target, classify every important
question by its downstream impact, and state whether functional design,
technical design, and backlog preparation can proceed. Do not invent missing
information.
```

**Expected controls:**

- all ten Canvas sections are present;
- the current mailbox, messages, and spreadsheet remain Existing;
- the workspace and listed capabilities are not presented as an approved MVP;
- ambiguous requester, service-team, site, request, ticket, and case terms
  remain unresolved;
- success measures, service targets, ownership, final Scope, and technical
  details remain explicit gaps;
- no generic questionnaire precedes the useful first Canvas.

| Prompt | Case result | Reservations or observed evidence |
| --- | --- | --- |
| Project-framing prompt above, then Documentary Prompt with `[format]` replaced |  |  |

## PF-MAN-002 — Contradictory Project

**Objective:** verify that the Project Canvas remains coherent while
preserving material conflicts and refusing unsupported Decisions.

**Data to provide:**

- `development/tests/fixtures/contradictory-project/project-charter.md`
- `development/tests/fixtures/contradictory-project/sponsor-message.md`
- `development/tests/fixtures/contradictory-project/operations-workshop.md`
- `development/tests/fixtures/contradictory-project/service-policy-extract.md`
- `development/tests/fixtures/contradictory-project/technical-assumptions.md`
- `development/tests/fixtures/contradictory-project/delivery-plan.md`

**Prompt:**

```text
Use project-framing to produce an English Project Canvas from all supplied
sources. Preserve every material contradiction, separate authoritative
Decisions from preferences and assumptions, keep MVP and outside-MVP scope
unresolved where necessary, and classify the Decisions or information needed
before functional design, technical design, and backlog preparation.
```

**Expected controls:**

- all ten Canvas sections are present;
- two-, three-, five-, and seven-year retention positions remain visible;
- access, approval, response time, reporting, rollout, cutover, dates, and
  priority conflicts are not silently resolved;
- identity and interface assumptions are not promoted to business Decisions;
- success criteria do not reuse conflicting targets as approved measures;
- downstream readiness is qualified by the unresolved authority and Scope.

| Prompt | Case result | Reservations or observed evidence |
| --- | --- | --- |
| Project-framing prompt above, then Documentary Prompt with `[format]` replaced |  |  |

## PF-MAN-003 — Application Modernization

**Objective:** verify separation of Existing, Target, and Transition while
keeping the Canvas at framing level.

**Data to provide:**

- `development/tests/fixtures/application-modernization/business/application-overview.md`
- `development/tests/fixtures/application-modernization/business/user-workshop.md`
- `development/tests/fixtures/application-modernization/documentation/user-guide-extract-2019.md`
- `development/tests/fixtures/application-modernization/technical/system-inventory.md`
- `development/tests/fixtures/application-modernization/technical/interface-notes.md`
- `development/tests/fixtures/application-modernization/operations/support-observations.md`
- `development/tests/fixtures/application-modernization/security/review-notes.md`
- `development/tests/fixtures/application-modernization/migration/constraints.md`
- `development/tests/fixtures/application-modernization/governance/decision-history.md`

**Prompt:**

```text
Use project-framing to produce an English Project Canvas for this
modernization. Distinguish Existing, Target, and Transition information,
separate confirmed Issues from Risks, preserve contradictions and the unknown
applicability of historical Decisions, and stop before detailed functional or
technical design. State the readiness of each downstream step.
```

**Expected controls:**

- all ten Canvas sections are present;
- existing workflows, systems, interfaces, workarounds, and Issues remain
  distinct from target outcomes;
- migration, rollback, archive, training, adoption, and parallel operation
  remain Transition concerns or Options rather than an approved plan;
- the reopening and Central Intake contradictions remain visible;
- no target modules, architecture, technology stack, or MVP sequence is
  invented;
- known continuity and service expectations are preserved without inventing
  additional success targets.

| Prompt | Case result | Reservations or observed evidence |
| --- | --- | --- |
| Project-framing prompt above, then Documentary Prompt with `[format]` replaced |  |  |

## PF-MAN-004 — New Application in French

**Objective:** verify proposed MVP handling, stakeholder/user separation,
known technical Constraints, success criteria, and natural French language.

**Data to provide:**

- `development/tests/fixtures/new-application/business-brief.md`
- `development/tests/fixtures/new-application/stakeholder-interviews.md`
- `development/tests/fixtures/new-application/personas.md`
- `development/tests/fixtures/new-application/functional-expectations.md`
- `development/tests/fixtures/new-application/service-rules.md`
- `development/tests/fixtures/new-application/non-functional-requirements.md`
- `development/tests/fixtures/new-application/integration-notes.md`
- `development/tests/fixtures/new-application/mvp-and-roadmap.md`
- `development/tests/fixtures/new-application/open-decisions.md`

**Prompt:**

```text
Utilise project-framing pour produire en français le Project Canvas de ce
projet à partir de toutes les sources fournies. Conserve le MVP proposé comme
provisoire, distingue les exclusions des options futures, sépare parties
prenantes et utilisateurs, explicite les contraintes techniques connues et
les questions restantes, puis indique la capacité du Canvas à alimenter la
conception fonctionnelle, la conception technique et le backlog. N'invente
aucune information.
```

**Expected controls:**

- les dix sections du Canvas sont présentes ;
- le MVP proposé reste `Provisoire` jusqu’à validation par l’autorité requise ;
- les exclusions explicites restent distinctes des idées futures ;
- les parties prenantes restent distinctes des utilisateurs et personas ;
- les contraintes d’identité, accessibilité, langue, sécurité, confidentialité,
  qualité de service et intégration restent au niveau du cadrage ;
- les objectifs de succès sans mesure ou cible approuvée restent non résolus ;
- la terminologie française est naturelle et respecte les distinctions
  canoniques.

| Prompt | Résultat du cas | Réserves ou preuves observées |
| --- | --- | --- |
| Prompt project-framing ci-dessus, puis prompt documentaire avec `[format]` remplacé |  |  |

## PF-MAN-005 — Controlled Real Project

**Objective:** verify the practical usefulness and downstream readiness of a
Project Canvas in a real but controlled context.

**Data to provide:** a non-confidential, anonymized, or appropriately
controlled project corpus. Do not place that corpus or its completed result in
the repository.

**Prompt:**

```text
Use project-framing on all supplied project sources. Produce the Project
Canvas in the project language for [audience] so it can support [review
purpose]. Preserve source traceability, contradictions, uncertainty, MVP and
outside-MVP distinctions, known business and technical constraints, Decisions,
Risks, questions, and success criteria. Classify each important question and
state downstream readiness. Do not perform detailed functional or technical
design and do not invent missing content.
```

Replace `[audience]` and `[review purpose]` with the actual controlled test
context.

**Expected controls:**

- the Canvas can be reviewed without repeating the complete source analysis;
- every important source statement is represented once and remains traceable;
- explicit gaps are understandable and do not make the document unusable;
- the Canvas supports a concrete functional or technical next step;
- the level of detail is useful without becoming a specification;
- any required future adjustment can be identified and traced.

| Prompt | Case result | Reservations or observed evidence |
| --- | --- | --- |
| Project-framing prompt above with both placeholders replaced, then Documentary Prompt with `[format]` replaced |  |  |

## Test Context

| Field | Value |
| --- | --- |
| Test case |  |
| Project name |  |
| Test date |  |
| Tester |  |
| ChatGPT model or environment |  |
| Source documents or information used |  |
| Requested language |  |
| Review purpose |  |
| Intended audience |  |
| Requested document format |  |
| Template or default structure |  |

## Bilingual Verification Grid

Enter one allowed result and concise evidence or reservations for every row.

| Criterion | Critères FR | Prompt | Result | Evidence, comments, or reservations |
| --- | --- | --- | --- | --- |
| The guided workflow persists and resumes its exact phase | Le workflow guidé persiste et reprend sa phase exacte | Start project-design, complete one transition, then continue in a new conversation and resume only from the next action recorded in project-design-state.json. |  |  |
| A transition cannot skip a required phase | Une transition ne peut pas contourner une phase obligatoire | Before selecting the stage, try to choose the delivery format and verify that the workflow refuses the transition without changing its phase. |  |  |
| The state file contains no project or source business content | Le fichier d'état ne contient aucun contenu métier du projet ou des sources | Inspect project-design-state.json and verify that it contains only consent, phase, choices, presence flags, counts, approvals, references, and transition history. |  |  |
| The state machine enforces one to three questions per framing round | La machine d'état impose une à trois questions par ronde de cadrage | During framing, try to record four questions in one iteration and verify that it is rejected; then record a valid round of at most three questions. |  |  |
| Completion is gated by Canvas approval and the requested native document | La finalisation exige l'approbation du Canvas et le document natif demandé | Try to approve without a saved non-empty Canvas and, when Word or Google Docs is selected, try to complete without the verified file or URL; both attempts must fail. |  |  |
| The plugin requests explicit consent before initializing its project workspace | Le plugin demande un consentement explicite avant d'initialiser son espace projet | Present the project-design skills and ask me to confirm that I want to use the plugin for my project specifications. Do not create any directory before my answer. |  |  |
| Stage selection proposes step 1 project-framing by default | Le choix de l'étape propose par défaut l'étape 1 project-framing | Ask which project-design stage I want to perform, propose step 1 project-framing by default, and clearly identify the stages that are not implemented yet. |  |  |
| The optional document format and template source are resolved before framing input | Le format documentaire optionnel et la source du modèle sont définis avant les entrées de cadrage | Before requesting project content, ask whether I also want Word or Google Docs and whether I will supply a local template, a Drive template, or use the default structure. |  |  |
| The Canvas is co-constructed through focused question-and-answer iterations | Le Canvas est co-construit par des itérations ciblées de questions-réponses | Build a first working Canvas from my description or sources, then ask at most three high-value questions per round and update the affected chapters after each answer. |  |  |
| The response first presents the selected skill, available and missing inputs, expected deliverables, and required or optional models or templates | La réponse présente d'abord le skill sélectionné, les entrées disponibles ou manquantes, les livrables attendus et les modèles obligatoires ou optionnels | Before execution, briefly present the selected project-design skill, its available and missing inputs, the deliverables it will generate, and every required or optional model or template. |  |  |
| Durable Markdown outputs are grouped under the target project's `_project-design/` directory without silent overwrite | Les sorties Markdown durables sont regroupées dans le répertoire `_project-design/` du projet cible sans écrasement silencieux | Save every durable Markdown artefact under `_project-design/` at the target project root, using the business-artefact and document paths defined by the plugin. |  |  |
| The primary output is a Project Canvas | La sortie principale est un Project Canvas | Use `project-framing` on all supplied sources and produce a structured Project Canvas, not a free-form report. |  |  |
| All ten required sections are present or explicitly insufficiently informed | Les dix sections obligatoires sont présentes ou explicitement signalées comme insuffisamment renseignées | Produce the ten-section Project Canvas and keep every unsupported or missing section explicitly visible. |  |  |
| The Canvas clarifies the expression of need instead of only summarizing sources | Le Canvas clarifie l'expression de besoin au lieu de seulement résumer les sources | Clarify the business problem, objectives, value, and boundaries from the supplied sources instead of only summarizing them. |  |  |
| Content remains faithful and traceable to source material | Le contenu reste fidèle et traçable aux sources | Preserve source fidelity and provide concise traceability for every material Canvas statement. |  |  |
| No unsupported information is invented | Aucune information non étayée n'est inventée | Do not invent missing owners, dates, measures, budgets, Constraints, Requirements, or Decisions; expose them as gaps or questions. |  |  |
| Objectives and expected value are correct and distinct | Les objectifs et la valeur attendue sont corrects et distincts | Separate supported Objectives from expected value and do not turn benefits into unsupported commitments. |  |  |
| Project Stakeholders and users are correctly distinguished | Les parties prenantes du projet et les utilisateurs sont correctement distingués | Distinguish Project Stakeholders, authority, contributors, direct users, and indirect users from the supplied evidence. |  |  |
| MVP, outside MVP, explicit exclusions, future Options, and unresolved Scope are distinct | Le MVP, le hors MVP, les exclusions explicites, les options futures et le périmètre non résolu sont distincts | Separate MVP, Outside MVP, explicit exclusions, future Options, and Unresolved Scope without inventing approval. |  |  |
| Known business and technical Constraints are represented without detailed design | Les contraintes métier et techniques connues sont représentées sans conception détaillée | Represent known business and technical Constraints at framing level and stop before detailed solution design. |  |  |
| Existing, Target, and Transition are correctly distinguished | L'existant, la cible et la transition sont correctement distingués | Distinguish Existing, Target, and Transition information wherever mixing them would change meaning. |  |  |
| Decisions remain distinct from Assumptions, preferences, and proposals | Les décisions restent distinctes des hypothèses, préférences et propositions | Keep authoritative Decisions separate from Assumptions, preferences, proposals, and Options. |  |  |
| Risks and confirmed Issues are correctly distinguished | Les risques et les problèmes avérés sont correctement distingués | Separate uncertain Risks from confirmed current Issues and retain their supported impacts. |  |  |
| Established, Provisional, and Unresolved statuses remain visible | Les statuts Établi, Provisoire et Non résolu restent visibles | Preserve Established, Provisional, and Unresolved status for every material statement where status affects use. |  |  |
| Contradictions remain visible without unsupported resolution | Les contradictions restent visibles sans résolution non étayée | Expose every material contradiction and do not resolve it without sufficient evidence and authority. |  |  |
| Questions are project-specific, useful, and classified by impact | Les questions sont propres au projet, utiles et classées selon leur impact | Produce project-specific Open Questions and classify each by downstream impact and known decision authority. |  |  |
| Success criteria are supported or explicitly unresolved without invented thresholds | Les critères de succès sont étayés ou explicitement non résolus sans seuil inventé | Include only source-supported success criteria and leave missing measures or thresholds explicitly unresolved. |  |  |
| The Canvas remains outside detailed functional and technical design | Le Canvas reste en dehors de la conception fonctionnelle et technique détaillée | Produce framing only; do not create detailed features, journeys, architecture, APIs, components, or backlog items. |  |  |
| French terminology is natural and professionally appropriate when requested | La terminologie française est naturelle et adaptée à un contexte professionnel lorsqu'elle est demandée | Produce the Canvas in natural professional French while preserving canonical distinctions and project-specific terms. |  |  |
| Functional-design readiness is stated and justified | La capacité à démarrer la conception fonctionnelle est indiquée et justifiée | State and justify whether functional design can start, including blocking and non-blocking questions. |  |  |
| Technical-design readiness is stated and justified | La capacité à démarrer la conception technique est indiquée et justifiée | State and justify whether technical design can start independently, including remaining technical blockers. |  |  |
| Backlog-preparation readiness is stated and justified | La capacité à préparer le backlog est indiquée et justifiée | State and justify whether backlog preparation can start without pretending that insufficiently designed Scope is ready. |  |  |
| The Canvas is usable despite explicit non-blocking unknowns | Le Canvas reste exploitable malgré des inconnues non bloquantes explicites | Produce a useful first Canvas despite non-blocking unknowns and identify only the questions that truly block progress. |  |  |
| Later adjustments can be traced and do not silently rewrite validated information | Les ajustements ultérieurs peuvent être tracés et ne réécrivent pas silencieusement les informations validées | Revise the supplied Canvas from new founded evidence, trace the adjustment, and never silently rewrite validated information or Decisions. |  |  |
| The final document preserves every material Canvas element without changing business meaning | Le document final préserve chaque élément matériel du Canvas sans modifier le sens métier | Use `document-project-canvas` on the validated Canvas and preserve every material element, status, contradiction, question, readiness qualification, and traceability reference. |  |  |
| The ten sections, explicit gaps, statuses, contradictions, Decisions, and questions remain visible in the document | Les dix sections, les lacunes explicites, les statuts, les contradictions, les décisions et les questions restent visibles dans le document | Produce the final document with all ten sections and keep every explicit gap, status, contradiction, Decision, and question visible. |  |  |
| The document hierarchy, registers, and tables are readable and consistent | La hiérarchie, les registres et les tableaux du document sont lisibles et cohérents | Apply the default professional structure in `[format]` and verify headings, registers, lists, and tables for readability. |  |  |
| No title metadata, template field, summary, owner, date, or approval is invented | Aucun titre, champ de template, résumé, responsable, date ou approbation n'est inventé | Apply the supplied template or default structure without inventing metadata, summaries, owners, dates, approvals, or missing content. |  |  |
| The requested format is native and verified rather than simulated | Le format demandé est natif et vérifié plutôt que simulé | Produce the Project Canvas document in `[format]` and verify the actual native Markdown, Word, or Google Docs result before delivery. |  |  |

## Feedback Summary

| Topic | Notes |
| --- | --- |
| What worked well / Points positifs |  |
| Friction / Irritants |  |
| Missing content / Contenu manquant |  |
| Unnecessary content / Contenu inutile |  |
| Terminology to improve / Terminologie à améliorer |  |
| Recommended skill changes / Évolutions recommandées |  |

## Reuse Decision

| Question | Decision and comments |
| --- | --- |
| Is the Canvas usable as input to `functional-design`? |  |
| Is the Canvas usable as input to `technical-design`? |  |
| Is the Canvas usable before backlog preparation? |  |
| Does the final document preserve the validated Canvas without documentary distortion? |  |
| Is the produced format ready for stakeholder review? |  |
| Is another test required before broader use? |  |
| Overall result |  |
| Reservations |  |

## ChatGPT Report Input

Provide ChatGPT with:

- the selected test-case identifier;
- the completed test context;
- the generated Project Canvas;
- the produced Project Canvas document and requested format;
- the completed bilingual verification grid;
- the feedback summary;
- the reuse decision and reservations.

Ask it to format the information without changing results, inventing evidence,
resolving unanswered questions, or exposing confidential data.
