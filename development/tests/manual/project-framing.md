# Project Framing Manual Tests

Use this single file to prepare and review manual tests of `project-framing`.
Do not commit confidential project information, raw client data, or a
completed client test record.

Allowed overall results:

- `PASS`
- `PASS WITH RESERVATIONS`
- `FAIL`

## Test Cases

### PF-MAN-001 - Incomplete Project

- **Objective:** verify that the skill produces a useful framing without
  inventing missing information or requiring an exhaustive questionnaire.
- **Input:** source files from
  `development/tests/fixtures/incomplete-project/`, excluding its `README.md`.
- **Invocation:** request an English project-framing document from the
  available sources.
- **Expected behaviour:** known information is used, missing ownership and
  boundaries remain visible, and questions are useful and prioritized.

### PF-MAN-002 - Contradictory Project

- **Objective:** verify that the skill preserves material contradictions
  without selecting an unsupported winner.
- **Input:** source files from
  `development/tests/fixtures/contradictory-project/`, excluding its
  `README.md`.
- **Invocation:** request an English project-framing document that identifies
  the decisions required before approval.
- **Expected behaviour:** conflicting approval, eligibility, retention,
  reporting, rollout, and cutover positions remain visible and traceable.

### PF-MAN-003 - Application Modernization

- **Objective:** verify separation between the existing application, target
  intent, and transition concerns.
- **Input:** source files from
  `development/tests/fixtures/application-modernization/`, excluding its
  `README.md`.
- **Invocation:** request an English framing for the modernization project.
- **Expected behaviour:** current Issues, historical Decisions, target
  outcomes, migration concerns, and unresolved rules remain distinct.

### PF-MAN-004 - New Application in French

- **Objective:** verify provisional MVP handling and natural French
  terminology.
- **Input:** source files from
  `development/tests/fixtures/new-application/`, excluding its `README.md`.
- **Invocation:** request a concise project-framing document in French.
- **Expected behaviour:** proposed Scope remains provisional, future Options
  remain distinct from exclusions, and French wording is natural and
  professionally appropriate.

### PF-MAN-005 - Controlled Real Project

- **Objective:** verify practical usefulness in a real framing context.
- **Input:** a non-confidential, anonymized, or appropriately controlled
  project corpus.
- **Invocation:** request a framing in the project language for a stated
  audience and review purpose.
- **Expected behaviour:** the result is faithful, concise, actionable, and
  useful for preparing or conducting a project workshop.

## Test Procedure

1. Select one test case.
2. Provide the indicated sources or Project View.
3. Invoke `project-framing` with the requested language and purpose.
4. Answer only questions that are useful for the test and defer the others.
5. Review the framing against the source material and criteria below.
6. Record concrete evidence, friction, and improvement requests.

## Test Context

| Field | Value |
| --- | --- |
| Test case | |
| Project name | |
| Test date | |
| Tester | |
| ChatGPT model or environment | |
| Source documents or information used | |
| Requested language | |
| Framing purpose | |
| Intended audience | |

## Items to Verify

Enter one allowed result and concise evidence for each criterion.

| Criterion | Critères FR | Result | Comments or observed examples |
| --- | --- | --- | --- |
| Selected information is relevant to framing | Les informations retenues sont pertinentes pour le cadrage | | |
| Content remains faithful to source material | Le contenu reste fidèle aux sources | | |
| No unsupported information is invented | Aucune information non étayée n'est inventée | | |
| Objectives are identified correctly | Les objectifs sont correctement identifiés | | |
| Scope and out of scope are correct and distinct | Le périmètre et les exclusions sont corrects et clairement distingués | | |
| Stakeholders and Actors are correctly distinguished | Les parties prenantes et les acteurs sont correctement distingués | | |
| Existing, Target, and Transition are correctly distinguished | L'existant, la cible et la transition sont correctement distingués | | |
| Needs and Requirements are correctly distinguished | Les besoins et les exigences sont correctement distingués | | |
| Risks and confirmed Issues are correctly distinguished | Les risques et les problèmes avérés sont correctement distingués | | |
| Assumptions remain visible | Les hypothèses restent visibles | | |
| Contradictions remain visible | Les contradictions restent visibles | | |
| Unresolved questions remain visible and actionable | Les questions non résolues restent visibles et peuvent donner lieu à une action | | |
| Questions asked by the skill are relevant | Les questions posées par le skill sont pertinentes | | |
| Questions are not repeated or unnecessary | Les questions ne sont ni répétitives ni inutiles | | |
| Proposed next steps are useful | Les prochaines étapes proposées sont utiles | | |
| French terminology is natural and professionally appropriate | La terminologie française est naturelle et adaptée à un contexte professionnel | | |
| Document structure and wording are clear | La structure et la formulation du document sont claires | | |
| Level of detail is appropriate | Le niveau de détail est approprié | | |
| Framing is useful for preparing or conducting a project workshop | Le cadrage est utile pour préparer ou conduire un atelier projet | | |

## Feedback Summary

### What Worked Well


### What Created Friction


### Missing or Unnecessary Content


### Terminology to Improve


### Recommended Skill Changes


## Reuse Decision

| Question | Decision and comments |
| --- | --- |
| Is the skill usable on another real project? | |
| Is another test required before broader use? | |
| Overall result | |

## ChatGPT Report Input

Provide ChatGPT with:

- the selected test-case identifier;
- the completed test context;
- the generated framing document;
- the completed verification table;
- the feedback summary;
- the reuse decision.

Ask it to format the information without changing results, inventing evidence,
or resolving unanswered questions.
