# Project Design - Contexte de continuité

Dernière mise à jour : 2026-08-05

## Utilisation de ce fichier

Ce document permet de reprendre le projet dans un nouveau prompt sans perdre
les décisions, l'historique ou l'état de travail.

Il constitue la source centrale et unique du contexte de continuité du projet.
Les fichiers racine `AGENTS.md` pour Codex et `CLAUDE.md` pour Claude doivent
uniquement pointer vers ce document et ne doivent pas maintenir une copie
concurrente de ses instructions.

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
- dès qu'un résultat de validation, un changement matériel de l'état du dépôt,
  une prochaine étape ou un blocage non résolu serait perdu avec l'historique
  de la conversation ;
- avant de transférer le projet vers une nouvelle conversation.

Ne pas attendre que l'utilisateur annonce un changement de conversation :
enregistrer les éléments durables au cours du même tour de travail. Ne pas
modifier ce fichier pour un échange qui n'ajoute aucun contexte durable au
projet.

## Projet

`project-design` est un plugin Markdown-first et methodology-first destiné à
structurer la conception de projets applicatifs et logiciels.

Compétences prévues :

- `project-design` : placeholder installé pour l'orchestration globale
  future, non implémentée ;
- `project-framing` : étape 1, cadrage et Project Canvas ;
- `functional-design` : placeholder installé pour l'étape 2, conception
  fonctionnelle future ;
- `technical-design` : placeholder installé pour l'étape 2 bis, conception
  technique future,
  complémentaire ou parallèle ;
- `product-backlog` : placeholder installé pour la transformation future de
  la conception validée en backlog traçable ;
- `document-project-canvas` : placeholder installé pour le futur document
  Project Canvas ;
- `document-functional-design` : placeholder installé pour les futures
  spécifications fonctionnelles ;
- `document-technical-design` : placeholder installé pour les futures
  spécifications techniques ;
- `document-product-backlog` : placeholder installé pour le futur document de
  backlog.

Les neuf répertoires de skills de l'architecture officielle sont présents.
Chaque skill spécialisé doit rester utilisable indépendamment.

### Catégories de responsabilités

L'architecture cible distingue trois catégories :

1. **Orchestration globale** — `project-design` déterminera les étapes utiles,
   appellera les skills spécialisés, transmettra leurs artefacts, maintiendra
   leur cohérence et organisera les retours tracés vers une étape précédente.
   Cette orchestration complète n'est pas implémentée et ne doit pas absorber
   les méthodologies spécialisées.
2. **Skills métier** — `project-framing` est la seule méthodologie métier
   implémentée. Elle produit l'artefact Project Canvas. `functional-design`,
   `technical-design` et `product-backlog` restent des placeholders installés
   dont les méthodologies et artefacts structurés sont futurs. Aucun skill
   métier ne connaît un format documentaire, un template, une mise en forme
   finale ou un export.
3. **Skills documentaires** — les quatre placeholders documentaires mettront
   en forme leur artefact métier correspondant sans en devenir propriétaires.
   Ils ne pourront ni inventer de contenu, ni résoudre une question, ni
   modifier une Decision.

Formats prévisionnels, non disponibles actuellement :

- `document-project-canvas`, `document-functional-design` et
  `document-technical-design` : Markdown natif, Microsoft Word et Google Docs ;
- `document-product-backlog` : Markdown natif, Google Sheets, Microsoft Excel,
  Microsoft Word et Google Docs.

Ces formats sont futurs. Les placeholders ne contiennent aucune méthodologie,
aucun exemple runtime, aucun template et aucune intégration.

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
- Le Project Canvas est l'artefact métier principal de `project-framing`.
- Ses dix sections restent présentes ou explicitement insuffisamment
  renseignées ; une structure obligatoire ne justifie jamais l'invention.
- L'objectif métier de fiabilité à 80-90 % reste qualitatif et ne devient
  jamais un score calculé ou affiché.
- Les ajustements ultérieurs du Canvas doivent être tracés, justifiés, limités
  et ne jamais réécrire silencieusement une information validée ou une
  Decision.
- La production de connaissance métier reste séparée de sa restitution
  documentaire.
- La convention `<discipline>` pour l'artefact métier et
  `document-<discipline>` pour son document est définitive et obligatoire.
- Les exemples nécessaires au raisonnement d'un skill installé appartiennent
  à son répertoire `references/` et doivent être liés depuis son `SKILL.md`.
- `development/examples/` ne contient que des exemples brouillons ou non
  approuvés ; les conclusions attendues des fixtures ne deviennent jamais des
  exemples runtime.
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
| 8.2 - Project Canvas | Architecture prévisionnelle révisée et `project-framing` repositionné autour du Project Canvas | Implémentation terminée — validation manuelle utilisateur en attente |
| 8.3 - Architecture documentaire définitive | Quatre placeholders `document-<discipline>` installés et ancien placeholder générique supprimé | Terminée techniquement — aucune méthodologie documentaire implémentée |

## Historique des prompts directeurs

Cette section synthétise les prompts qui ont dirigé le projet. Elle ne les
reproduit pas mot pour mot, mais conserve leurs objectifs, interdictions,
décisions attendues et résultats. Le dépôt reste la source de vérité pour le
contenu effectivement livré.

### Itération 1 - Initialisation du plugin

Le prompt initial demandait de créer uniquement les fondations de
`project-design` :

- utiliser les générateurs officiels de plugin et de skills ;
- cibler Codex et Claude Code avec une implémentation de skills commune ;
- créer un orchestrateur futur et cinq skills spécialisés indépendants ;
- rester utilisable sans GitHub Spec Kit tout en préparant une frontière
  d'intégration optionnelle ;
- privilégier Markdown, YAML et JSON ;
- écrire les sources du plugin en anglais ;
- créer les manifests, placeholders, intégrations et documents initiaux ;
- utiliser la version initiale `0.1.0` ;
- ne pas implémenter de méthodologie détaillée, runtime, moteur de workflow,
  exporter, persistance, API, MCP, hook, agent ou commande.

Résultat : structure initiale, manifests, six squelettes de skills, ressources
partagées et documentation de dépôt.

### Itération 2 - Stratégie de test

Le prompt demandait une stratégie légère, documentation-first et centrée sur
la qualité méthodologique plutôt que sur l'identité du texte :

- toute évolution d'un skill doit mettre à jour et exécuter ses tests ;
- les critères portent sur structure, cohérence, fidélité, traçabilité,
  raisonnement, incertitude, frontières et absence d'invention ;
- exactement quatre fixtures permanentes doivent être conservées ;
- scénarios, checklists, Golden Outputs, régression et preuves d'exécution
  doivent rester séparés ;
- Codex et Claude doivent utiliser les mêmes données et critères ;
- les Golden Outputs exigent une approbation humaine explicite ;
- aucun moteur de test complexe ne doit être introduit.

Résultat : stratégie de test et structure de validation. Les livrables des
itérations 2 et 3 ont finalement été regroupés dans le commit `0371f0a`.

### Itération 3 - Corpus permanent anonymisé

Le prompt demandait de construire le benchmark permanent du plugin :

- quatre projets fictifs seulement : incomplet, contradictoire,
  modernisation et nouvelle application ;
- informations réparties entre plusieurs artefacts réalistes et hétérogènes ;
- corpus réutilisable par tous les futurs skills et indépendant de leur
  méthodologie ;
- aucune donnée réelle ou confidentielle ;
- aucune sortie attendue ni Golden Output ;
- contradictions implicites, documentation incomplète et incertitudes
  suffisamment réalistes pour empêcher les skills d'inventer.

Résultat : quatre fixtures multi-artefacts permanentes et leurs scénarios.

### Itération 4 - Décision d'architecture de l'information

Le prompt demandait d'évaluer objectivement au moins :

- un Project Model unique ;
- un Knowledge Model suivi d'un Project Model ;
- toute solution alternative réellement supérieure.

La comparaison devait couvrir simplicité, complexité, maintenance,
traçabilité, conflits, incertitude, raisonnement IA, Spec Kit et évolution,
sans implémenter de modèle.

Décision : retenir le flux :

```text
Documents -> Knowledge Model -> Project Model -> Skills -> Artefacts
```

Le Knowledge Model préserve ce qui a été extrait et son état épistémique. Le
Project Model représente la compréhension normalisée consommée par les
skills.

### Itération 5 - Canonical Domain Model

Le prompt demandait le vocabulaire métier commun minimal, dérivé du corpus :

- modèle purement conceptuel, indépendant des technologies et méthodes ;
- définition, rôle, alias, relations et exemples pour chaque concept ;
- exclusion des notions non justifiées par le corpus ou plusieurs skills ;
- aucune implémentation du Knowledge Model, Project Model, schéma ou format de
  sérialisation.

Résultat : 22 concepts canoniques version 0.1. Le modèle canonique est devenu
le contrat sémantique partagé et ne peut évoluer que par décision
architecturale explicite.

À ce stade, la roadmap a volontairement été étendue : Canonical Domain Model,
Knowledge Model et Project Model devaient être stabilisés dans trois
itérations distinctes avant le premier skill métier.

### Itération 6 - Minimal Knowledge Model

Le prompt figeait le Canonical Domain Model et demandait de représenter :

- assertions et concepts canoniques concernés ;
- provenance et emplacement source ;
- confiance, incertitude et statut de validation ;
- contradictions et coexistence de plusieurs assertions.

Le modèle devait préserver l'information sans normaliser le projet, résoudre
les conflits, générer des artefacts ou modifier un concept canonique.

Résultat : Minimal Knowledge Model version 0.1.

### Itération 7 - Minimal Normalized Project Model

Le prompt figeait le Canonical Domain Model et le Knowledge Model. Il
demandait une vue cohérente et normalisée du projet :

- état courant et éléments canoniques normalisés ;
- relations entre éléments ;
- information résolue et incertitudes restantes ;
- statuts `Established`, `Provisional` et `Unresolved` ;
- perspectives `Existing`, `Target` et `Transition` ;
- traçabilité vers la Knowledge Basis.

Le Project Model ne devait ni recopier chaque assertion, ni produire des
documents, ni exécuter une méthodologie.

Résultat : Minimal Normalized Project Model version 0.1.

### Extension linguistique française

La discussion qui a suivi l'architecture a établi que :

- l'anglais reste la référence canonique interne ;
- le français est un compagnon terminologique, pas une copie du modèle ;
- les termes propres au projet restent gouvernés par les sources ;
- aucun repli linguistique silencieux n'est accepté ;
- aucune variante `fr-FR` ou `fr-CA` n'est créée sans besoin démontré ;
- les libellés doivent rester naturels dans les documents clients.

Résultat : compagnon français complet pour les 22 concepts et les libellés des
modèles partagés. Le libellé `Issue -> Problème avéré` reste notamment à
surveiller dans les restitutions réelles.

### Itération 8 - `project-framing`

Le prompt lançait le premier skill métier complet en conservant les quatre
fondations stables :

- transformer des sources ou une Project View en cadrage fiable et concis ;
- couvrir contexte, objectifs, périmètre, participants, états, contraintes,
  hypothèses, décisions, risques, problèmes avérés et questions ;
- préserver contradictions, inconnues et statuts de normalisation ;
- éviter les questionnaires préalables exhaustifs ;
- permettre un cadrage incomplet et classer les questions selon leur impact ;
- produire une restitution naturelle dans la langue demandée ;
- rester hors de la conception fonctionnelle, technique et du backlog ;
- valider le comportement sur les quatre fixtures ;
- fournir un support léger de test manuel.

Résultat : `project-framing` version 0.1, sa structure de restitution, son
contrat qualité et ses validations.

### Ajustements des tests manuels

Les échanges suivants ont précisé la convention :

- ajouter une colonne `Critères FR` traduisant chaque critère ;
- fournir dans les comptes rendus les cas à transmettre à ChatGPT pour mise
  en forme ;
- conserver un seul fichier Markdown par skill ;
- ne pas créer de sous-répertoire manuel par skill ;
- maintenir cinq cas `PF-MAN-001` à `PF-MAN-005` ;
- ne jamais commiter de données client confidentielles.

Résultat : `development/tests/manual/project-framing.md`.

### Itération 8.1 - Frontière de packaging

La discussion a distingué trois responsabilités :

- `plugins/project-design/` pour le bundle réellement installable ;
- `development/` pour les tests, fixtures, rapports, plans, spécifications,
  exemples et contexte versionnés ;
- `.local/` pour les travaux temporaires, confidentiels ou propres à une
  machine, ignorés par Git.

Le marketplace du dépôt devait pointer uniquement vers le bundle. Aucun skill
installé ne devait dépendre des tests. Les règles qualité nécessaires au
runtime ont donc été rendues autonomes dans le bundle.

Résultat : nouvelle frontière de packaging, seconde revue de cohérence et
trois commits séparés.

### Décision sur les exemples runtime

Après la revue du packaging, il a été confirmé que les exemples destinés à
alimenter le contexte d'un skill et à limiter les hallucinations doivent être
installés avec ce skill.

La convention retenue est :

- exemples runtime validés dans
  `plugins/project-design/skills/<skill-name>/references/` ;
- lien direct et condition de lecture dans le `SKILL.md` concerné ;
- exemples brouillons ou expérimentaux dans `development/examples/` ;
- Golden Outputs et conclusions attendues des fixtures exclus des
  instructions runtime pour ne pas biaiser les tests ;
- aucun dossier racine `examples/` ajouté au bundle sans consommateur
  explicite.

### Reprise de l'itération 8 - Project Canvas

L'intervention du 2026-08-05 a repris `project-framing` afin de transformer son
ancienne restitution flexible en Project Canvas obligatoire et exploitable.

Le Canvas constitue désormais la sortie principale de l'étape 1 et couvre :

1. contexte métier ;
2. objectifs et valeur attendue ;
3. parties prenantes du projet ;
4. utilisateurs ;
5. périmètre fonctionnel, avec MVP, hors MVP et périmètre non résolu ;
6. contraintes techniques connues au cadrage ;
7. risques ;
8. décisions ;
9. questions ;
10. critères de succès.

Une section insuffisamment renseignée reste visible comme telle. Le Canvas ne
doit pas inventer une information, un découpage MVP, une valeur, un objectif,
un critère de succès, un seuil ou une décision pour paraître complet.

La fiabilité attendue de 80-90 % signifie qualitativement que l'information
matérielle fournie est exploitée, les contradictions et inconnues sont
visibles, les frontières sont compréhensibles et les étapes suivantes n'ont
pas à refaire entièrement le cadrage. Aucun score n'est calculé.

`functional-design` et `technical-design` pourront révéler de nouvelles
informations fiables. Toute évolution du Canvas devra être tracée, justifiée
par une source nouvelle ou corrigée, limitée à un enrichissement, une
clarification ou une correction fondée, et ne jamais réécrire silencieusement
une information validée ou une Decision.

Références runtime ajoutées :

- `plugins/project-design/skills/project-framing/references/project-canvas.md` ;
- `plugins/project-design/skills/project-framing/references/project-canvas-example.md`.

L'exemple est fictif, court, étranger aux fixtures et n'est ni un Golden
Output ni une source de faits réutilisables.

Cette architecture prévisionnelle a ensuite été remplacée par la séparation
définitive entre artefacts métier et documents. L'architecture officielle est :

```text
project-design
├── project-framing
├── functional-design
├── technical-design
├── product-backlog
├── document-project-canvas          # placeholder
├── document-functional-design       # placeholder
├── document-technical-design        # placeholder
└── document-product-backlog         # placeholder
```

Les quatre skills documentaires mettent en forme leur artefact métier
correspondant sans le modifier. L'ancien placeholder documentaire générique a
été supprimé : l'orchestration globale reste la responsabilité future unique
de `project-design`.

Les quatre fixtures ont été rejouées avec succès. Les sorties brutes restent
hors Git sous `.local/test-runs/2026-08-05-project-canvas/`. Les tests manuels
ont été actualisés, mais leur rejeu par l'utilisateur reste requis.

Rapport :
[Project Canvas Evolution Review](tests/executions/2026-08-05-project-canvas-review.md).

### Séparation définitive des skills documentaires

La décision structurante suivante remplace la recommandation documentaire
provisoire des deux rapports précédents :

- chaque discipline métier produit un artefact métier et ne connaît aucun
  format documentaire ;
- chaque `document-<discipline>` produit uniquement le document correspondant ;
- les quatre placeholders documentaires sont installés pour stabiliser
  l'arborescence, sans méthodologie, template, exemple ou intégration ;
- l'ancien placeholder générique a été supprimé, car les manifests découvrent
  directement les neuf répertoires et sa suppression ne casse pas le plugin ;
- `project-design` reste l'unique futur orchestrateur global et ne produit ni
  contenu métier ni document.

Rapport :
[Definitive Document Skill Architecture](tests/executions/2026-08-05-definitive-document-skill-architecture.md).

État Git de cette intervention :

- branche : `main` ;
- base : `ff72ce5` (`Clarify project document architecture`) ;
- `main`, `origin/main` et `origin/HEAD` étaient alignés sur cette base au
  début de l'intervention ;
- l'utilisateur a explicitement autorisé le commit et le push de l'ensemble
  de l'intervention le 2026-08-05 ; le journal Git reste la source de vérité
  pour l'identifiant du commit de livraison.

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
| `3b21750` | Rapport de cohérence du packaging |
| `0332597` | Évolution de `project-framing` autour du Project Canvas |
| `ff72ce5` | Clarification de l'architecture documentaire provisoire |

Rapports d'itération et de revue :

| Sujet | Rapport |
| --- | --- |
| Information Architecture | [Revue](tests/executions/2026-07-23-information-architecture-review.md) |
| Canonical Domain Model | [Revue](tests/executions/2026-07-23-canonical-domain-model-review.md) |
| Knowledge Model | [Revue](tests/executions/2026-07-23-knowledge-model-review.md) |
| Project Model | [Revue](tests/executions/2026-07-23-project-model-review.md) |
| Terminologie française | [Revue](tests/executions/2026-07-23-french-terminology-review.md) |
| `project-framing` | [Revue](tests/executions/2026-07-23-project-framing-review.md) |
| Frontière de packaging | [Revue](tests/executions/2026-07-24-packaging-boundary-review.md) |
| Cohérence du packaging | [Revue](tests/executions/2026-07-24-packaging-coherence-review.md) |
| Project Canvas | [Revue](tests/executions/2026-08-05-project-canvas-review.md) |
| Architecture documentaire | [Audit](tests/executions/2026-08-05-document-architecture-audit.md) |
| Architecture documentaire définitive | [Revue](tests/executions/2026-08-05-definitive-document-skill-architecture.md) |

Les itérations 1 à 3 n'ont pas de rapport d'exécution dédié. Leur historique
est conservé par les commits, la stratégie de test, les fixtures et la
présente synthèse.

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

`project-framing` version 0.2 est techniquement implémenté. Sa validation
manuelle utilisateur reste en attente.

Le skill :

- accepte un Project View ou des sources projet ;
- reprend et clarifie l'expression de besoin ;
- produit un artefact Project Canvas couvrant les dix sections obligatoires ;
- produit un premier Canvas sans questionnaire exhaustif ;
- préserve les contradictions et les incertitudes ;
- distingue les informations bloquantes, nécessaires avant la conception
  fonctionnelle, la conception technique ou le backlog, et différables ;
- indique la capacité du Canvas à alimenter chaque étape suivante ;
- produit une restitution française naturelle ;
- reste en dehors de la conception fonctionnelle, technique et backlog ;
- encadre les ajustements ultérieurs par des règles de traçabilité et de
  justification.

Rapport :
[Project Canvas Evolution Review](tests/executions/2026-08-05-project-canvas-review.md).

## État Git de l'intervention Project Canvas

- Branche : `main`.
- Base de l'intervention : `19f8abf` (`Document prompt history and runtime
  example policy`).
- Commit livré : `0332597` (`Evolve project framing around Project Canvas`).
- `main`, `origin/main` et `origin/HEAD` étaient alignés sur `0332597` au début
  de l'audit documentaire du 2026-08-05.
- Les sorties brutes de fixture restent ignorées sous `.local/`.

## État Git de la série de packaging

Branche : `main`

Base distante avant la série : `934f5eb` (`Implement project-framing skill`)

Dernier commit de la série poussé sur `origin/main` :
`3b21750` (`Document packaging coherence review`).

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
dédiés. Le rapport de cohérence et la première version du contexte
appartiennent au commit documentaire final de la série.

Les enrichissements ultérieurs de l'historique des prompts, de la roadmap et
de la politique des exemples sont conservés dans ce document. Le dépôt,
`git status` et `git log` restent la source de vérité pour le statut de
synchronisation.

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

## Roadmap prévue

Les points suivants ne bloquent pas le développement métier, mais doivent être
traités avant une distribution :

1. réaliser une installation réelle depuis le marketplace du dépôt dans un
   environnement propre ;
2. décider si les changements `Unreleased` appartiennent à `0.1.0` ou à une
   nouvelle version ;
3. aligner ensuite manifests, spécification, changelog, tags et politique de
   cache Codex.

Séquence métier prévue :

| Itération | Objectif prévu | Garde-fous principaux |
| --- | --- | --- |
| Validation 8.2 | Rejouer les tests manuels du Project Canvas | Ne pas déclarer la méthodologie pleinement validée avant retour utilisateur |
| 9 | Implémenter `functional-design` | Consommer le Project Canvas et le Project Model, sans refaire le cadrage ni anticiper l'architecture technique |
| 10 | Implémenter `technical-design` comme étape complémentaire ou parallèle | Consommer le Canvas, distinguer architecture, décisions, intégrations, qualités et risques sans redéfinir les besoins métier |
| 11 | Implémenter `product-backlog` | Transformer le périmètre conçu et validé en backlog traçable sans inventer de priorité, estimation, exigence ou décision |
| 12 | Implémenter `document-project-canvas` | Produire le document Project Canvas sans modifier l'artefact métier |
| 13 | Implémenter `document-functional-design` | Produire les spécifications fonctionnelles sans modifier l'artefact métier |
| 14 | Implémenter `document-technical-design` | Produire les spécifications techniques sans modifier l'artefact métier |
| 15 | Implémenter `document-product-backlog` | Produire le document de backlog sans créer, prioriser ou estimer de contenu |
| 16 | Implémenter l'orchestration `project-design` | Router les skills, transmettre les artefacts et maintenir la cohérence sans produire de contenu ni de documents |

Chaque itération métier doit recevoir son propre prompt détaillé avant
implémentation. Cette roadmap fixe l'ordre et les frontières, pas encore la
méthodologie des skills futurs.

## Améliorations et décisions différées

- Tester l'installation réelle du bundle depuis le marketplace.
- Trancher la gouvernance de version avant la prochaine release.
- Envisager des scripts sous `development/tools/` et une CI GitLab pour les
  contrôles structurels, sans automatiser l'approbation méthodologique.
- Évaluer les libellés français dans des livrables clients réels.
- Attendre plusieurs skills consommateurs avant de formaliser les identités,
  versions, schémas YAML ou JSON et la propagation des changements du Project
  Model.
- Ne pas restructurer de nouveau le dépôt avant qu'un besoin concret soit
  démontré par les prochains skills.
- Définir les formats et contrats de modèles réellement pris en charge par
  chaque futur skill documentaire avant d'annoncer ces formats comme
  disponibles.

## Prompt de reprise

```text
Tu reprends le développement du plugin project-design.

Lis d'abord development/PROJECT_CONTEXT.md, puis development/PLAN.md,
development/SPEC.md, development/tests/TESTING.md et les fondations
architecturales liées à l'itération demandée.

Vérifie ensuite l'état réel du dépôt avec git status et git log. Le dépôt
reste la source de vérité si une différence existe.

Respecte les fondations architecturales considérées comme stables et ne les
modifie pas sans décision explicite. Utilise les quatre fixtures permanentes
pour toute évolution métier. Après chaque modification, fournis un compte
rendu CI clair.

Ne crée aucun commit et ne pousse aucune modification sans instruction
explicite.

Reprends à la section "Roadmap prévue". La prochaine étape attendue est le
rejeu manuel du Project Canvas avec
development/tests/manual/project-framing.md. Après validation utilisateur,
l'itération métier suivante sera consacrée à functional-design. Si son prompt
détaillé n'est pas fourni, ne déduis pas sa méthodologie : demande les
instructions.
```
