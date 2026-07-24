# Project Design - Contexte de continuité

Dernière mise à jour : 2026-07-24

## Utilisation de ce fichier

Ce document permet de reprendre le projet dans un nouveau prompt sans perdre
les décisions, l'historique ou l'état de travail.

Au début d'une nouvelle conversation :

1. fournir ce fichier à l'agent ;
2. lui demander de lire les documents du dépôt concernés par la prochaine
   itération ;
3. lui demander de vérifier `git status` avant toute modification ;
4. considérer l'état courant du dépôt comme prioritaire si ce document est
   devenu partiellement obsolète.

Mettre ce fichier à jour :

- à la fin de chaque itération ;
- après une décision architecturale importante ;
- après une modification de la feuille de route ;
- avant de transférer le projet vers une nouvelle conversation.

## Projet

`project-design` est un plugin Markdown-first et methodology-first destiné à
structurer la conception de projets applicatifs et logiciels.

Compétences prévues :

- `project-design` : orchestration future ;
- `project-framing` : cadrage projet ;
- `functional-design` : conception fonctionnelle ;
- `technical-design` : conception technique ;
- `product-backlog` : préparation du backlog ;
- `document-output` : production documentaire.

Chaque skill spécialisé doit rester utilisable indépendamment.

## Architecture de référence

Le flux d'information accepté est :

```text
Documents sources
    -> Knowledge Model
    -> Project Model
    -> Skills
    -> Artefacts générés
```

Le Canonical Domain Model ne constitue pas une étape de ce flux. Il fournit le
vocabulaire partagé par les modèles et les skills.

Fondations architecturales actuellement considérées comme stables :

- [Information Architecture ADR](../plugins/project-design/shared/project-model/information-architecture.md)
- [Canonical Domain Model v0.1](../plugins/project-design/shared/terminology/canonical-domain-model.md)
- [Minimal Knowledge Model v0.1](../plugins/project-design/shared/knowledge-model/README.md)
- [Minimal Normalized Project Model v0.1](../plugins/project-design/shared/project-model/README.md)
- [French canonical terminology](../plugins/project-design/shared/terminology/canonical-terms.fr.md)

Toute évolution d'une fondation stable doit passer par une décision
architecturale explicite. Un skill ne doit pas créer son propre modèle
concurrent.

## Décisions durables

- L'anglais reste la référence canonique interne.
- Le français est un compagnon terminologique, pas une duplication du modèle.
- Les termes propres au projet restent gouvernés par les sources.
- Aucun repli linguistique silencieux n'est autorisé.
- Les variantes régionales inutiles, comme `fr-FR`, ne sont pas introduites
  sans besoin démontré.
- Les informations `Established`, `Provisional` et `Unresolved` restent
  distinctes.
- Les perspectives `Existing`, `Target` et `Transition` restent distinctes.
- Les couples Stakeholder/Actor, Need/Requirement, Risk/Issue et
  Option/Decision ne doivent pas être confondus.
- Les contradictions ne sont pas résolues sans preuve et autorité suffisantes.
- Les Golden Outputs ne changent qu'après approbation humaine explicite.
- Aucun commit ou push n'est effectué sans demande explicite.
- Après chaque modification, fournir un compte rendu de type CI indiquant
  clairement les contrôles passés, échoués ou non applicables.

## Historique des itérations

| Itération | Résultat | État |
| --- | --- | --- |
| 1 - Initialisation | Architecture du plugin, manifests, skills et ressources partagées initialisés | Terminée |
| 2 - Stratégie de test | Fixtures, scénarios, checklists, exécutions et politique de Golden Outputs définis | Terminée |
| 3 - Corpus permanent | Quatre corpus anonymisés permanents ajoutés | Terminée |
| 4 - Information Architecture | Architecture Documents -> Knowledge Model -> Project Model -> Skills retenue | Terminée |
| 5 - Canonical Domain Model | Vocabulaire canonique v0.1 défini | Terminée |
| 6 - Knowledge Model | Modèle minimal des assertions, sources, incertitudes et contradictions défini | Terminée |
| 7 - Project Model | Vue projet normalisée minimale définie | Terminée |
| Extension linguistique | Compagnon terminologique français ajouté | Terminée |
| 8 - `project-framing` | Premier skill métier complet, tests sur quatre fixtures et workbook manuel | Terminée |
| 8.1 - Packaging Boundary | Bundle installable isolé des ressources de développement et du travail local | Terminée |

Commits principaux :

| Commit | Contenu |
| --- | --- |
| `7761b3c` | Initial commit |
| `0371f0a` | Permanent reference corpus |
| `cb8ab3b` | Information Architecture |
| `2abe33f` | Canonical Domain Model |
| `674d931` | Knowledge Model |
| `3ea36c5` | Project Model |
| `a3b5cdf` | French terminology companion |
| `934f5eb` | `project-framing` version 0.1 |
| `4390f1c` | Réorganisation autour du bundle installable isolé |
| `696abeb` | Clarification des règles qualité et de la roadmap |

## Tests et qualité

Le corpus permanent contient quatre familles :

- `incomplete-project` ;
- `contradictory-project` ;
- `application-modernization` ;
- `new-application`.

Toute évolution métier doit être validée contre les fixtures concernées.

Pour les tests manuels :

- conserver un seul fichier Markdown par skill dans
  `development/tests/manual/` ;
- ne pas créer de sous-répertoire par skill ;
- ne pas commiter de données client confidentielles ;
- utiliser `PASS`, `PASS WITH RESERVATIONS` ou `FAIL` ;
- inclure dans le compte rendu les cas de tests à transmettre à ChatGPT pour
  mise en forme.

Le fichier courant est
[Project Framing Manual Tests](tests/manual/project-framing.md).

## État de `project-framing`

`project-framing` version 0.1 est implémenté et validé.

Le skill :

- accepte un Project View ou des sources projet ;
- produit un premier cadrage sans questionnaire exhaustif ;
- préserve les contradictions et les incertitudes ;
- distingue les informations bloquantes, nécessaires à la phase suivante et
  différables ;
- produit une restitution française naturelle ;
- reste en dehors de la conception fonctionnelle, technique et backlog.

Rapport :
[Project Framing Skill Review](tests/executions/2026-07-23-project-framing-review.md).

## État Git de la série de packaging

Branche : `main`

Base distante avant la série : `934f5eb` (`Implement project-framing skill`)

La série de packaging du 2026-07-24 couvre :

- déplacement du bundle installable vers `plugins/project-design/` ;
- déplacement des tests, exemples, contexte, plan et spécification vers
  `development/` ;
- création du marketplace `.agents/plugins/marketplace.json` pointant
  uniquement vers le bundle ;
- création de `.local/`, ignoré par Git, pour le travail temporaire ou
  confidentiel ;
- déplacement de
  `development/tests/manual/project-framing/manual-test-workbook.md` vers
  `development/tests/manual/project-framing.md` ;
- ajout de cinq cas manuels `PF-MAN-001` à `PF-MAN-005` ;
- maintien de la grille bilingue ;
- déplacement de la checklist normative de `project-framing` dans le bundle ;
- suppression des dépendances runtime vers les fixtures et checklists de
  développement ;
- mise à jour des références et de la documentation du dépôt.

Vérifications effectuées :

- structure plate de `development/tests/manual/` : PASS ;
- absence de référence vers l'ancien workbook : PASS ;
- cinq cas manuels et tableaux : PASS ;
- destination trouvée pour chacun des 85 anciens chemins suivis : PASS ;
- correspondance entre les quatre fixtures et leurs scénarios : PASS ;
- correspondance exacte des 22 concepts canoniques avec le compagnon
  français : PASS ;
- ADR, modèle canonique et compagnon français inchangés au niveau des
  contenus : PASS ;
- validation du plugin Codex depuis `plugins/project-design/` : PASS ;
- validation stricte du plugin Claude : PASS ;
- validation des six skills : PASS ;
- source marketplace et exclusion `.local/` : PASS ;
- absence de dépendance du bundle vers `development/` : PASS ;
- liens du bundle limités à sa frontière installable : PASS ;
- Markdown, liens locaux et blocs de code : PASS.

La réorganisation et les corrections de cohérence sont séparées en commits
dédiés. Le rapport de cohérence et cette mise à jour du contexte appartiennent
au commit documentaire final de la série. Le dépôt et `git log` restent la
source de vérité pour le statut de synchronisation.

Rapports :

- [Packaging Boundary Review](tests/executions/2026-07-24-packaging-boundary-review.md)
- [Packaging Coherence Review](tests/executions/2026-07-24-packaging-coherence-review.md)

## Packaging Boundary

Les tests et documents de développement doivent rester dans Git sans être
installés avec le plugin.

Structure mise en place :

```text
project_design/
├── plugins/
│   └── project-design/       # Bundle installable
│       ├── .codex-plugin/
│       ├── .claude-plugin/
│       ├── skills/
│       └── shared/
├── development/              # Développement versionné
│   ├── PROJECT_CONTEXT.md
│   ├── PLAN.md
│   ├── SPEC.md
│   ├── tests/
│   └── examples/
├── .local/                   # Travail local ignoré
├── .agents/plugins/          # Marketplace du dépôt
├── integrations/
└── documentation du dépôt
```

Le marketplace utilise `./plugins/project-design` comme source. Les règles
nécessaires au fonctionnement sont autonomes dans le bundle. Les tests
valident ces règles sans être une dépendance runtime.

## Prochaines étapes

1. Réaliser un test d'installation depuis le marketplace du dépôt lors de la
   prochaine validation de distribution.
2. Décider avant la prochaine release si les évolutions `Unreleased` restent
   dans la version `0.1.0` ou nécessitent une nouvelle version.
3. Démarrer l'itération 9 consacrée à `functional-design`.

## Prompt de reprise

```text
Tu reprends le développement du plugin project-design.

Lis d'abord development/PROJECT_CONTEXT.md, puis vérifie l'état réel du dépôt
avec git status. Le dépôt reste la source de vérité si une différence existe.

Respecte les fondations architecturales considérées comme stables et ne les
modifie pas sans décision explicite. Utilise les quatre fixtures permanentes
pour toute évolution métier. Après chaque modification, fournis un compte
rendu CI clair.

Ne crée aucun commit et ne pousse aucune modification sans instruction
explicite.

Reprends à la section "Prochaines étapes" de
development/PROJECT_CONTEXT.md et demande les instructions détaillées de la
prochaine itération si elles ne sont pas encore fournies.
```
