# Project Framing Manual Tests

Use this single file to prepare and review manual tests of `project-framing`
after its Project Canvas evolution.

Do not commit confidential project information, raw client data, a generated
client Canvas, or a completed client test record.

Allowed results:

- `PASS`
- `PASS WITH RESERVATIONS`
- `FAIL`

## Test Procedure

1. Select one case below.
2. Provide every listed source artefact, excluding the fixture `README.md`.
3. Use the supplied prompt without adding the expected observations or this
   checklist to the model context.
4. Preserve the generated Project Canvas before reviewing it.
5. Complete the case controls and the bilingual verification grid.
6. Record concrete evidence, the result, and any reservations.
7. Return the completed results and generated Canvas for the intervention
   report without committing confidential material.

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

| Case result | Reservations or observed evidence |
| --- | --- |
|  |  |

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

| Case result | Reservations or observed evidence |
| --- | --- |
|  |  |

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

| Case result | Reservations or observed evidence |
| --- | --- |
|  |  |

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

| Résultat du cas | Réserves ou preuves observées |
| --- | --- |
|  |  |

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

| Case result | Reservations or observed evidence |
| --- | --- |
|  |  |

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

## Bilingual Verification Grid

Enter one allowed result and concise evidence or reservations for every row.

| Criterion | Critères FR | Result | Evidence, comments, or reservations |
| --- | --- | --- | --- |
| The primary output is a Project Canvas | La sortie principale est un Project Canvas |  |  |
| All ten required sections are present or explicitly insufficiently informed | Les dix sections obligatoires sont présentes ou explicitement signalées comme insuffisamment renseignées |  |  |
| The Canvas clarifies the expression of need instead of only summarizing sources | Le Canvas clarifie l'expression de besoin au lieu de seulement résumer les sources |  |  |
| Content remains faithful and traceable to source material | Le contenu reste fidèle et traçable aux sources |  |  |
| No unsupported information is invented | Aucune information non étayée n'est inventée |  |  |
| Objectives and expected value are correct and distinct | Les objectifs et la valeur attendue sont corrects et distincts |  |  |
| Project Stakeholders and users are correctly distinguished | Les parties prenantes du projet et les utilisateurs sont correctement distingués |  |  |
| MVP, outside MVP, explicit exclusions, future Options, and unresolved Scope are distinct | Le MVP, le hors MVP, les exclusions explicites, les options futures et le périmètre non résolu sont distincts |  |  |
| Known business and technical Constraints are represented without detailed design | Les contraintes métier et techniques connues sont représentées sans conception détaillée |  |  |
| Existing, Target, and Transition are correctly distinguished | L'existant, la cible et la transition sont correctement distingués |  |  |
| Decisions remain distinct from Assumptions, preferences, and proposals | Les décisions restent distinctes des hypothèses, préférences et propositions |  |  |
| Risks and confirmed Issues are correctly distinguished | Les risques et les problèmes avérés sont correctement distingués |  |  |
| Established, Provisional, and Unresolved statuses remain visible | Les statuts Établi, Provisoire et Non résolu restent visibles |  |  |
| Contradictions remain visible without unsupported resolution | Les contradictions restent visibles sans résolution non étayée |  |  |
| Questions are project-specific, useful, and classified by impact | Les questions sont propres au projet, utiles et classées selon leur impact |  |  |
| Success criteria are supported or explicitly unresolved without invented thresholds | Les critères de succès sont étayés ou explicitement non résolus sans seuil inventé |  |  |
| The Canvas remains outside detailed functional and technical design | Le Canvas reste en dehors de la conception fonctionnelle et technique détaillée |  |  |
| French terminology is natural and professionally appropriate when requested | La terminologie française est naturelle et adaptée à un contexte professionnel lorsqu'elle est demandée |  |  |
| Functional-design readiness is stated and justified | La capacité à démarrer la conception fonctionnelle est indiquée et justifiée |  |  |
| Technical-design readiness is stated and justified | La capacité à démarrer la conception technique est indiquée et justifiée |  |  |
| Backlog-preparation readiness is stated and justified | La capacité à préparer le backlog est indiquée et justifiée |  |  |
| The Canvas is usable despite explicit non-blocking unknowns | Le Canvas reste exploitable malgré des inconnues non bloquantes explicites |  |  |
| Later adjustments can be traced and do not silently rewrite validated information | Les ajustements ultérieurs peuvent être tracés et ne réécrivent pas silencieusement les informations validées |  |  |

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
| Is another test required before broader use? |  |
| Overall result |  |
| Reservations |  |

## ChatGPT Report Input

Provide ChatGPT with:

- the selected test-case identifier;
- the completed test context;
- the generated Project Canvas;
- the completed bilingual verification grid;
- the feedback summary;
- the reuse decision and reservations.

Ask it to format the information without changing results, inventing evidence,
resolving unanswered questions, or exposing confidential data.
