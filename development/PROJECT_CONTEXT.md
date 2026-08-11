# Project Design - Contexte de continuité

Dernière mise à jour : 2026-08-11

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

- `project-design` : entrée guidée avec machine d'état version 0.2 implémentée
  pour présenter les skills, obtenir le consentement, initialiser le répertoire,
  imposer les transitions, reprendre entre conversations et transmettre au
  skill spécialisé ; orchestration complète multi-disciplines future ;
- `project-framing` : étape 1, cadrage et Project Canvas ;
- `functional-design` : placeholder installé pour l'étape 2, conception
  fonctionnelle future ;
- `technical-design` : placeholder installé pour l'étape 2 bis, conception
  technique future,
  complémentaire ou parallèle ;
- `product-backlog` : placeholder installé pour la transformation future de
  la conception validée en backlog traçable ;
- `document-project-canvas` : méthodologie documentaire version 0.1
  implémentée pour restituer un Project Canvas validé en Markdown natif,
  Microsoft Word ou Google Docs ; validation manuelle combinée en attente ;
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

1. **Orchestration globale** — `project-design` assure désormais l'entrée
   guidée, le consentement, l'initialisation et la sélection de l'étape. Il
   déterminera ensuite les étapes utiles,
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
3. **Skills documentaires** — `document-project-canvas` met en forme le Canvas
   validé sans en devenir propriétaire. Les trois autres skills documentaires
   restent des placeholders. Aucun ne peut inventer de contenu, résoudre une
   question ou modifier une Decision.

Formats actuellement pris en charge par `document-project-canvas` :

- Markdown natif par défaut ;
- Microsoft Word ;
- Google Docs.

Formats encore prévisionnels et non disponibles :

- `document-functional-design` et `document-technical-design` : Markdown
  natif, Microsoft Word et Google Docs ;
- `document-product-backlog` : Markdown natif, Google Sheets, Microsoft Excel,
  Microsoft Word et Google Docs.

Les trois placeholders restants ne contiennent aucune méthodologie, aucun
exemple runtime, aucun template et aucune intégration. Le skill
`document-project-canvas` contient uniquement sa méthodologie et ses références
runtime de structure, formats et qualité ; aucun template ou script n'est
embarqué.

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
- [Shared Document Model v0.1](../plugins/project-design/shared/document-model/README.md)
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
- Le Shared Document Model version 0.1 est le contrat documentaire commun,
  indépendant des disciplines, pour tous les skills `document-<discipline>`.
- Un document représente un artefact métier mais ne devient jamais sa source
  de vérité ; un changement de format ou de template ne peut modifier le sens,
  les statuts, les Decisions, les contradictions ou la traçabilité.
- La vue d'ensemble officielle de l'architecture est
  `development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md` ; elle consolide
  les contrats existants sans remplacer les modèles ou les `SKILL.md`
  normatifs.
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
- Avant d'exécuter un skill, présenter très brièvement le skill ou l'ordre des
  skills, les entrées disponibles ou manquantes, les livrables attendus et les
  modèles ou templates obligatoires, optionnels ou remplacés par un défaut.
- Tous les Markdown durables générés par le plugin sont regroupés sous
  `_project-design/` à la racine du projet cible. Les artefacts métier utilisent
  la racine de ce dossier et les documents `_project-design/documents/`.
- Un placeholder annonce son statut et ses entrées/sorties prévisionnelles,
  mais ne crée aucun fichier ni répertoire de livraison.
- `project-design` doit obtenir un consentement explicite avant de créer ou
  réutiliser `_project-design/` pour un nouveau parcours. Un refus ne crée rien.
- L'initialisation est idempotente et ne crée que `_project-design/` et
  `_project-design/documents/`, sans artefact vide.
- Le choix d'étape propose `project-framing` comme étape 1 par défaut. Les
  placeholders restent visibles mais ne sont jamais présentés comme exécutables.
- Le Markdown métier reste obligatoire. Word ou Google Docs est un complément
  optionnel dont le format et le modèle local, Drive ou par défaut sont choisis
  avant la collecte du contenu projet.
- `project-framing` présente les dix chapitres, accepte une description dans le
  prompt, des documents sources ou les deux, puis co-construit le Canvas par
  rondes de trois questions au maximum.
- Le workflow guidé persiste uniquement son état de contrôle dans
  `_project-design/project-design-state.json` et l'actualise atomiquement.
- Ce fichier ne contient aucune description projet, source, question, réponse,
  connaissance métier ou contenu du Canvas.
- Chaque transition exige la phase attendue ; aucune étape ne peut être sautée
  sur la seule base de l'historique conversationnel.
- Une reprise commence par la commande `status` et suit uniquement
  `next_action`. Il n'existe volontairement aucune commande de réinitialisation.
- La phase `complete` exige un Canvas non vide explicitement approuvé puis, si
  demandé, un `.docx` sous `_project-design/documents/` ou un lien Google Docs
  natif vérifié.

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
| 8.4 / Itération 12 avancée - Document Project Canvas | `document-project-canvas` implémenté pour tester la chaîne complète avec `project-framing` | Implémentation et validation technique terminées — validation manuelle combinée en attente |
| 8.5 - Shared Document Model | Contrat documentaire commun formalisé pour tous les skills documentaires | Fondation architecturale terminée — validation technique documentée |
| 8.6 - Plugin Architecture & Coherence Review v1.0 | Modèles, skills, propriétaires, flux, dépendances et roadmap audités et documentés | Revue terminée — architecture prête pour `functional-design` avec réserves documentaires non bloquantes |
| 8.7 - Entrée guidée | Consentement, initialisation sûre, choix d'étape, options documentaires et cadrage itératif implémentés | Validation technique terminée — rejeu manuel utilisateur en attente |
| 8.8 - Workflow guidé persistant | Machine d'état, transitions obligatoires, reprise, validations du Canvas et du document implémentées | Validation technique terminée — rejeu manuel utilisateur en attente |

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
├── document-project-canvas          # implemented methodology
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

### Avancement anticipé de `document-project-canvas`

Après la livraison de l'architecture définitive, l'utilisateur a demandé
d'implémenter immédiatement `document-project-canvas` afin de tester dans le
même rejeu le Canvas métier et son document final. Cette instruction avance
l'itération 12 sans modifier l'ordre prévu des autres méthodologies.

Le contrat version 0.1 retenu est :

- entrée obligatoire : Project Canvas validé produit par `project-framing` ou
  artefact équivalent conforme ;
- Markdown natif par défaut, Microsoft Word et Google Docs sur demande ;
- structure professionnelle native si aucun template compatible n'est fourni ;
- template optionnel, jamais utilisé pour ajouter, supprimer ou altérer une
  connaissance métier ;
- préservation intégrale des dix sections, statuts, perspectives, conflits,
  Decisions, questions, readiness et références de traçabilité ;
- vérification du contenu et du format natif avant livraison ;
- retour vers `project-framing` lorsqu'un défaut porte sur l'artefact métier,
  sans correction documentaire silencieuse.

Le skill ne contient aucun template, script ou intégration spécifique. Il
utilise les outils documentaires natifs disponibles sur la plateforme et doit
annoncer explicitement toute impossibilité de produire ou vérifier un format
externe.

La validation manuelle devient séquentielle : `project-framing`, conservation
de l'artefact brut, puis `document-project-canvas`, conservation du document et
évaluation séparée de la fidélité métier et de la qualité documentaire. Le
fichier manuel Markdown et l'onglet `project-framing` du Google Sheet `Recette`
comportent désormais une colonne `Prompt`. Chaque cas et chacun des 30 critères
proposent ainsi le ou les prompts types à exécuter. Les colonnes de résultat et
de commentaires restent séparées, et les listes de validation de résultat du
Google Sheet sont préservées. L'onglet conserve les critères métier et les cinq
contrôles sur la fidélité documentaire, la structure, la lisibilité, la
non-invention et le format natif vérifié.

Le marketplace Codex actif ne pointe plus vers l'ancien clone iCloud. Il
référence désormais le bon dépôt sous
`/Users/julienoger/Documents/Dev/perso_project_design`. Le dépôt ayant été
renommé, la source locale du marketplace a été corrigée puis le plugin a été
réinstallé depuis ce chemin le 10 août 2026. Après la formalisation du
Shared Document Model, le cachebuster installé après le retour de validation
du 10 août 2026 est `0.1.0+codex.20260810124338`. Il expose les neuf skills, le
`document-project-canvas` implémenté avec ses trois références runtime et la
nouvelle fondation documentaire référencée par les quatre skills
documentaires. Un nouveau fil Codex est nécessaire pour charger ce registre
mis à jour.

Rapport :
[Document Project Canvas Implementation Review](tests/executions/2026-08-05-document-project-canvas-implementation.md).

### Retour de validation sur l'invocation et les livrables

Le retour utilisateur du 10 août 2026 ajoute deux règles transverses sans
modifier les modèles métier ou documentaires :

- la première réponse d'un skill doit présenter rapidement le skill utilisé,
  les éléments attendus en entrée, les livrables générés et les modèles ou
  templates que l'utilisateur doit fournir ;
- tous les Markdown durables générés par les skills `project-design` doivent
  être regroupés dans `_project-design/` à la racine du projet cible.

La convention d'emplacement est :

```text
_project-design/
├── project-canvas.md
├── functional-design.md
├── technical-design.md
├── product-backlog.md
└── documents/
    ├── project-canvas.md
    ├── functional-design.md
    ├── technical-design.md
    └── product-backlog.md
```

Seuls les fichiers produits par des méthodologies implémentées et réellement
demandés sont créés. La convention est portée par les règles qualité partagées
et référencée par les neuf skills. Le test manuel Markdown et l'onglet
`project-framing` du Google Sheet `Recette` contiennent deux critères
supplémentaires pour cette présentation initiale et ce répertoire, portant la
grille à 30 critères.

État Git de cette implémentation :

- branche : `main` ;
- base : `dfba5f1` (`Finalize document skill architecture`) ;
- l'arbre de travail contient les modifications non commitées de
  `document-project-canvas`, de ses tests et de la documentation associée ;
- aucun commit et aucun push n'ont été demandés ou effectués.

### Itération 8.7 - Entrée guidée et cadrage itératif

Le retour utilisateur du 11 août 2026 rend le démarrage du plugin directif
sans mettre en œuvre l'orchestration complète :

- `project-design` présente les skills et demande un consentement explicite
  avant toute initialisation ;
- après accord, le script installé
  `skills/project-design/scripts/init_workspace.py` crée ou réutilise de façon
  idempotente `_project-design/` et `_project-design/documents/` ;
- le skill demande l'étape et propose `project-framing` par défaut ;
- il présente l'étape, conserve le Markdown métier obligatoire et collecte le
  choix éventuel Word ou Google Docs ainsi que le modèle local, Drive ou la
  structure professionnelle par défaut ;
- `project-framing` présente les dix chapitres, demande ensuite une description
  projet ou des documents sources, construit un premier Canvas et l'améliore
  par rondes de trois questions à forte valeur au maximum ;
- `document-project-canvas` réutilise le choix documentaire sans redemander et
  conserve Word sous `_project-design/documents/project-canvas.docx` ou livre
  le lien Google Docs natif.

Le script refuse de s'exécuter sans `--confirmed`, refuse la racine du système
et le dossier personnel, n'écrase aucun fichier, prend en charge `--dry-run` et
retourne un résultat JSON. Ses quatre tests unitaires passent.

Le fichier manuel et l'onglet `project-framing` du Google Sheet `Recette`
contiennent quatre critères supplémentaires, soit 34 critères : consentement,
étape par défaut, restitution/modèle et construction itérative. La lecture
après écriture confirme les valeurs, le retour à la ligne, les validations de
résultat et la conservation des résultats précédents.

Rapport :
[Guided Project Design Workflow Review](tests/executions/2026-08-11-guided-project-design-workflow-review.md).

Le cachebuster généré et réinstallé depuis le dépôt Documents est
`0.1.0+codex.20260811094254`, sous
`/Users/julienoger/.codex/plugins/cache/project-design/project-design/`.
Un nouveau fil Codex est nécessaire pour charger ce registre de skills.

État Git : modifications non commitées conservées ; aucun commit ni push n'a
été demandé ou effectué.

### Itération 8.8 - Workflow guidé persistant

Après constat que le guidage 8.7 reposait encore en partie sur le respect des
instructions par le LLM, l'utilisateur a demandé sa mise en œuvre technique.
Le script installé `skills/project-design/scripts/workflow.py` fournit une
machine d'état persistante et retourne systématiquement la phase et la
`next_action` autorisée.

Phases implémentées :

```text
awaiting_stage
-> awaiting_delivery
-> awaiting_sources
-> framing_iterations
-> awaiting_canvas_approval
-> awaiting_document (si demandé)
-> complete
```

Contrats durables :

- `start --confirmed` crée le workspace et le fichier d'état ou reprend l'état
  existant sans le réinitialiser ;
- chaque commande refuse une phase inattendue sans faire avancer l'état ;
- les placeholders sont refusés comme étapes exécutables ;
- Word ou Google Docs exige un mode de modèle ; un modèle local doit exister et
  un modèle Drive doit utiliser une URL Google ;
- au moins une description ou un document doit être réellement disponible ;
- une ronde de cadrage contient entre une et trois questions ; seuls les
  compteurs sont persistés ;
- l'approbation exige `_project-design/project-canvas.md` non vide et une
  confirmation explicite ;
- Word exige un `.docx` existant sous `_project-design/documents/` et Google
  Docs un lien natif avant la phase `complete` ;
- aucune commande de reset n'est exposée afin d'empêcher une perte silencieuse
  de continuité.

Les 16 tests unitaires couvrent l'initialisation, la reprise, les transitions
hors ordre, les placeholders, les modèles, les intrants, la limite de trois
questions, l'approbation du Canvas et les livraisons. Les neuf skills et le
plugin passent leurs validateurs officiels.

La recette Markdown et l'onglet `project-framing` du Google Sheet `Recette`
comptent désormais 39 critères. Les cinq nouveaux contrôles portent sur la
reprise, le refus de contournement, l'absence de contenu métier dans l'état, la
limite de questions et les conditions de finalisation. La lecture connecteur
confirme les valeurs, le retour à la ligne, les listes de validation et la
conservation des lignes existantes.

Rapport :
[Stateful Guided Workflow Review](tests/executions/2026-08-11-stateful-guided-workflow-review.md).

Le cachebuster stateful généré et réinstallé depuis le dépôt Documents est
`0.1.0+codex.20260811123622`, sous
`/Users/julienoger/.codex/plugins/cache/project-design/project-design/`.
Un nouveau fil Codex est nécessaire pour charger cette version.

Livraison Git : l'utilisateur a demandé le commit et le push de l'ensemble de
la série le 11 août 2026. Le journal Git constitue la source de vérité pour
l'identifiant du commit et l'état de synchronisation avec `origin/main`.

### Formalisation du Shared Document Model

L'itération d'architecture suivante a extrait le contrat commun déjà appliqué
par `document-project-canvas` dans une fondation indépendante des disciplines :
`plugins/project-design/shared/document-model/README.md`.

Le modèle version 0.1 définit :

- l'artefact métier structuré, versionnable et indépendant des formats ;
- le document comme représentation humaine, jamais source de vérité métier ;
- le flux unidirectionnel artefact -> skill documentaire -> document ;
- les responsabilités des formats et des templates sans mutation sémantique ;
- la préservation des Decisions, questions, contradictions, statuts,
  perspectives, références et qualifications de readiness ;
- le contrat minimal de tous les skills `document-<discipline>` ;
- une dépendance sans cycle : les skills documentaires référencent le modèle,
  qui ne dépend d'aucune discipline ni d'aucun skill.

`document-project-canvas` référence désormais explicitement cette fondation.
Sa méthodologie, `project-framing`, les autres méthodologies métier et tous les
artefacts métier restent inchangés par cette intervention.

Rapport :
[Shared Document Model Architecture Review](tests/executions/2026-08-05-shared-document-model-review.md).

État Git de cette formalisation :

- branche : `main` ;
- base commune des modifications non commitées : `dfba5f1` ;
- l'intervention complète la série non commitée de
  `document-project-canvas` ;
- aucun commit et aucun push n'ont été demandés ou effectués.

### Itération 8.6 - Plugin Architecture & Coherence Review v1.0

La revue complète confirme une architecture sans cycle et une responsabilité
unique pour chaque artefact métier et chaque représentation documentaire. La
vue officielle est :
[Plugin Architecture Overview v1.0](documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md).

Constats durables :

- les quatre fondations stables couvrent la sémantique, la connaissance
  extraite, la vue projet normalisée et la restitution documentaire ;
- aucun modèle ne dépend d'un skill et aucun skill ne redéfinit un modèle ;
- les 28 documents Markdown du bundle forment 73 dépendances locales directes
  sans cycle ;
- `functional-design` et `technical-design` sont complémentaires et peuvent
  être parallèles ; le pipeline ne doit pas être présenté comme strictement
  linéaire ;
- aucun producteur runtime autonome du Knowledge Model ou du Project Model
  n'est implémenté. `project-framing` prépare actuellement une vue de travail
  conforme à ces contrats lorsque seules des sources brutes sont fournies ;
- aucune fondation partagée supplémentaire n'est nécessaire avant
  l'implémentation de `functional-design` ;
- la validation manuelle combinée de `project-framing` et
  `document-project-canvas` reste un garde qualité en attente, sans constituer
  une dépendance architecturale nouvelle.

Réserves documentaires détectées, sans correction dans cette revue :

- les sections historiques `Next Iteration` des modèles et de l'ADR ne
  reflètent plus la roadmap courante ;
- `plugins/project-design/README.md` emploie une formulation ambiguë sur les
  « four skills without the document- prefix », alors que l'orchestrateur est
  également sans ce préfixe mais ne produit aucun artefact métier ;
- `development/examples/README.md` indique encore qu'aucun exemple runtime
  n'est approuvé, malgré l'exemple Project Canvas installé ;
- `development/tests/golden-outputs/README.md` présente encore toutes les
  méthodologies détaillées comme futures, alors que deux sont implémentées ;
- le minimum exact d'artefacts conçus requis par `product-backlog` reste une
  décision de sa future méthodologie.

Ces réserves ne créent ni chevauchement de responsabilité ni fondation
manquante. Elles sont classées dans le rapport entre corrections nécessaires,
améliorations facultatives et évolutions futures.

Rapport :
[Plugin Architecture and Coherence Review v1.0](tests/executions/2026-08-05-plugin-architecture-coherence-review-v1.0.md).

État Git de cette revue :

- branche : `main` ;
- base commune des modifications non commitées : `dfba5f1` ;
- les modifications non commitées des itérations 8.4 et 8.5 ont été
  préservées ;
- aucun modèle, `SKILL.md`, fixture ou Golden Output n'a été modifié ;
- aucun commit et aucun push n'ont été demandés ou effectués.

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
| Document Project Canvas | [Revue](tests/executions/2026-08-05-document-project-canvas-implementation.md) |
| Shared Document Model | [Revue](tests/executions/2026-08-05-shared-document-model-review.md) |
| Architecture globale v1.0 | [Revue](tests/executions/2026-08-05-plugin-architecture-coherence-review-v1.0.md) |
| Invocation et répertoire de livrables | [Revue](tests/executions/2026-08-10-skill-invocation-workspace-review.md) |

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

La revue 8.6 confirme que les fondations sont suffisantes. La prochaine
méthodologie à implémenter est `functional-design`. Le rejeu manuel combiné
8.2 reste à terminer comme garde qualité amont, sans imposer une nouvelle
fondation ni une révision des modèles.

| Itération | Objectif prévu | Garde-fous principaux |
| --- | --- | --- |
| Validation 8.2 combinée | Rejouer `project-framing`, puis `document-project-canvas` sur le Canvas conservé | Évaluer séparément la fidélité métier et la qualité documentaire ; ne déclarer aucune méthodologie pleinement validée avant retour utilisateur |
| 9 | Implémenter `functional-design` | Consommer le Project Canvas et le Project Model, sans refaire le cadrage ni anticiper l'architecture technique |
| 10 | Implémenter `technical-design` comme étape complémentaire ou parallèle | Consommer le Canvas, distinguer architecture, décisions, intégrations, qualités et risques sans redéfinir les besoins métier |
| 11 | Implémenter `product-backlog` | Transformer le périmètre conçu et validé en backlog traçable sans inventer de priorité, estimation, exigence ou décision |
| 12 avancée | Terminer la validation de `document-project-canvas`, déjà implémenté avant la fin de la validation 8.2 | Produire et vérifier le document sans modifier l'artefact métier |
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
- Définir les formats et contrats de modèles réellement pris en charge par les
  trois skills documentaires encore futurs avant d'annoncer ces formats comme
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

Reprends à la section "Roadmap prévue". La revue d'architecture 8.6 confirme
qu'aucune fondation supplémentaire n'est nécessaire. La prochaine itération
méthodologique est `functional-design`, uniquement lorsque son prompt détaillé
est fourni ; ne déduis pas sa méthodologie. Le rejeu manuel combiné de
`project-framing` puis `document-project-canvas` avec
development/tests/manual/project-framing.md reste un garde qualité en attente.
Conserve séparément l'artefact Canvas et le document final lors de ce rejeu.
Vérifie aussi la présentation initiale du skill et la création des sorties
Markdown sous `_project-design/` à la racine du projet cible.
```
