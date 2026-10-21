# Guide utilisateur de `project-design`

Ce guide résume les actions prises en charge par le plugin, les questions qu'il
pose, les informations à lui fournir et les livrables obtenus.

Dernière vérification : 5 septembre 2026.

## Capacités disponibles

| Skill | Statut | Action | Extrant |
| --- | --- | --- | --- |
| `project-design` | Disponible | Guide le parcours et mémorise son avancement | État du parcours et livrables des skills appelés |
| `project-framing` | Disponible | Clarifie le besoin et construit le Project Canvas | `_project-design/project-canvas.md` |
| `functional-design` | Disponible directement | Crée, vérifie ou fait évoluer la conception fonctionnelle | `_project-design/functional-design.md` |
| `document-project-canvas` | Disponible | Met en forme un Canvas validé sans changer son contenu | Markdown, Word ou Google Docs |
| `technical-design` | Placeholder | Future conception technique | Aucun actuellement |
| `product-backlog` | Placeholder | Future création du Product Backlog | Aucun actuellement |
| `document-functional-design` | Placeholder | Futur document fonctionnel | Aucun actuellement |
| `document-technical-design` | Placeholder | Futur document technique | Aucun actuellement |
| `document-product-backlog` | Placeholder | Futur document de backlog | Aucun actuellement |

Un placeholder explique son futur rôle, ses intrants et ses extrants, mais ne
crée aucun fichier. Le rejeu correctif ciblé des dernières adaptations de
`project-framing` et `document-project-canvas`, ainsi que le rejeu des fixtures
et le test manuel de `functional-design`, restent à réaliser.

## Démarrer le parcours guidé

Prompt conseillé :

```text
Utilise project-design pour cadrer mon projet situé dans
/chemin/vers/mon-projet. Guide-moi étape par étape et demande mon accord avant
de créer ou réutiliser le dossier _project-design/.
```

## Étapes du parcours

| Étape | Ce que le plugin demande | Ce que vous fournissez | Résultat |
| --- | --- | --- | --- |
| 1. Autorisation | Accord pour utiliser le plugin et créer ou réutiliser `_project-design/` et `_sources/` | Confirmation explicite | Espaces de travail et de sources, fichier d'état |
| 2. Étape | Quelle étape lancer ; `project-framing` est proposé par défaut | Choix de `project-framing` | Étape enregistrée |
| 3. Livrables | Canvas seul, Word ou Google Docs ; modèle par défaut, local ou Drive | Format et modèle éventuel | Choix documentaire enregistré |
| 4. Projet | Description, documents déposés dans `_sources/documents/` ou liens, et socle technique imposé ou choisi | Brief, notes, règles, décisions, manuels ou liens utiles | Sources indexées, intrants prêts pour l'analyse |
| 5. Cadrage | Questions de décision réellement nécessaires | Réponses complètes, partielles ou reports explicites | Canvas progressivement complété |
| 6. Validation | Approbation du Canvas ou demande d'une nouvelle itération | Accord ou corrections | Canvas validé |
| 7. Document | Rien de plus si le format et le modèle sont déjà enregistrés | Éventuelles contraintes de présentation déjà annoncées | Document natif vérifié |

Les choix explicites déjà fournis sont réutilisés sans vous les redemander.
Si vous n'avez pas encore choisi, le plugin recommande un démarrage par le
cadrage et un Canvas Markdown seul, puis vous invite à déposer vos sources dans
`_sources/documents/`. Il
enregistre les transitions dans l'ordre et attend les accords nécessaires.

### Un appui pour décider

À chaque point important, le plugin indique le livrable en cours, ce qui bloque
et la prochaine action recommandée. Pour une décision, il explique les options
et leurs conséquences, puis recommande une option lorsque les sources le
permettent. Sinon, il précise l'information manquante pour se prononcer.
Vous pouvez choisir une autre réponse ou reporter explicitement la décision.
Une recommandation ne devient jamais automatiquement une décision du projet.

Les choix peuvent être présentés dans une interface interactive lorsque
l'environnement le permet, ou directement dans la conversation.

### Questions posées pendant le cadrage

Le plugin pose uniquement les questions dont la réponse conditionne le projet,
par exemple :

- quel périmètre doit être retenu ;
- quelle décision bloque la conception fonctionnelle ;
- quelle contrainte doit être connue avant la conception technique ;
- quelle information manque avant de préparer un backlog fiable.

Il n'applique aucune limite arbitraire au nombre de questions. Vous pouvez
répondre à tout le lot, répondre partiellement ou reporter explicitement une
question. Les questions figurent dans un tableau `N° | Question | Réponse` à
numérotation stable : une question sans réponse affiche « À apporter », une
question répondue garde sa ligne avec la réponse retenue. Les questions sans
réponse sont reprises à l'identique dans une conversation suivante. Une
question nouvelle découverte pendant un lot en attente n'est pas ajoutée au
Canvas : elle est proposée sous « Questions candidates pour le prochain lot »
et ouverte à l'itération suivante.

Le lot est ordonné selon les blocages et les dépendances : le plugin indique
par où commencer, sans masquer les autres questions nécessaires. Après une
réponse, il résume le changement et les décisions encore attendues. Les
questions explicitement reportées restent distinctes des questions actives et
ne sont pas automatiquement reposées à la reprise. Un report ne supprime pas
son éventuel effet bloquant.

Exemple de réponse :

```text
Le périmètre validé couvre uniquement la France. L'authentification utilisera
le SSO existant. Je reporte la décision sur la durée d'archivage.
```

## Intrants acceptés

Vous pouvez fournir une simple description et/ou des sources :

- expression de besoin ou brief ;
- comptes rendus d'atelier ;
- spécifications existantes ;
- règles, politiques ou décisions ;
- inventaire fonctionnel ou technique ;
- Project View déjà structuré ;
- fichiers locaux ou liens Google Drive.

Le plugin ne vous demande pas de construire vous-même un Knowledge Model ou un
Project Model.

Le démarrage crée systématiquement `_sources/documents/`, `source-index.md` et
`links.md`, et ajoute `/_sources/` au `.gitignore`. Déposez vos documents dans
`_sources/documents/` ou fournissez des liens : chaque document présent est
indexé avec son empreinte SHA-256. Copier un fichier situé ailleurs exige votre
accord, fichier par fichier ; l'original n'est jamais modifié et aucune copie
n'écrase un fichier. Les documents Google natifs restent des liens. Vous
pouvez, si vous le demandez, conserver vos sources à leur emplacement
d'origine ; `_sources/` n'est alors pas supprimé.

Chaque source est lue intégralement : un document dont le texte extrait est
quasi vide est lu par reconnaissance de caractères ou page par page, et les
tableurs sont lus sans modifier l'original. Le message de livraison indique,
pour chaque source, si elle a été lue et par quelle méthode, et signale toute
source non lue ou partiellement lue.

Dès l'accueil, le plugin demande si un socle technique est imposé ou déjà
choisi et s'il doit préparer des évolutions futures, par exemple d'autres
canaux ou d'autres applications.

## Extrant du cadrage

`project-framing` crée `_project-design/project-canvas.md` avec exactement dix
sections numérotées :

1. contexte métier ;
2. objectifs et valeur attendue ;
3. parties prenantes ;
4. utilisateurs ;
5. périmètre fonctionnel ;
6. contraintes techniques ;
7. risques ;
8. décisions ;
9. questions ;
10. critères de succès.

Le périmètre fonctionnel, les risques, les décisions et les questions sont
présentés en tableaux :

- périmètre : tableaux `MVP` et `Hors MVP` en colonnes
  `Module | Fonctionnalité | Description succincte`, une ligne par
  fonctionnalité commençant par un verbe à l'infinitif, les capacités
  propres à la cible marquées **[Nouveau]** et les prestations incluses
  listées sous le tableau MVP ;
- risques : `Risque | Impact | Solution` ; une solution absente des sources
  est signalée comme proposition à valider dans le message de livraison ;
- décisions : `Thème | Décision` ;
- questions : `N° | Question | Réponse`.

Lorsque des manuels, menus existants ou maquettes définissent le périmètre,
chaque fonctionnalité décrite figure dans le MVP, en Hors MVP avec sa raison,
ou derrière une question.

Un bloc non numéroté indique ensuite séparément si la conception
fonctionnelle, la conception technique et la préparation du backlog sont
prêtes, prêtes avec réserves ou non prêtes.

Le Canvas décrit uniquement la position courante validée. Un audit demandé
explicitement reste séparé dans
`_project-design/project-canvas-audit.md`.

Avant votre approbation, le plugin fournit le lien du Canvas enregistré,
résume les changements et rappelle les blocages et la capacité à poursuivre.
Après livraison, il recommande la prochaine action possible. Si le Canvas
validé le permet, il propose un prompt prêt à utiliser pour `functional-design`.
La fin du cadrage ne signifie pas que toute la conception du projet est terminée.

## Extrant documentaire optionnel

Après approbation du Canvas, `document-project-canvas` peut produire :

- `_project-design/documents/project-canvas.md` ;
- `_project-design/documents/project-canvas.docx` ;
- un lien vers un Google Docs natif vérifié.

Le skill conserve strictement le contenu du Canvas. Il n'invente ni résumé, ni
sous-titre, ni métadonnée, ni approbation et ne fusionne pas un audit séparé
sans demande explicite.

Le parcours refuse un faux fichier Word simplement renommé en `.docx` ou un
paquet Word illisible. Ce contrôle de structure complète la vérification
visuelle et la fidélité au Canvas ; il ne les remplace pas.

## Extrant de conception fonctionnelle

`functional-design` s'utilise directement à partir d'un Project Canvas validé.
La machine d'état guidée ne route pas encore cette étape. Le skill crée ou met
à jour `_project-design/functional-design.md` comme un document vivant :

- acteurs et rôles ;
- processus globaux ;
- tableau des produits, modules et fonctionnalités ;
- spécification détaillée de chaque fonctionnalité, avec scénario nominal,
  variantes valides, erreurs, exceptions, critères d'acceptation, questions,
  interfaces, champs, règles et références de messages ;
- catalogue global des e-mails transactionnels, SMS, notifications et
  informations à l'écran ;
- capacité à alimenter séparément la conception technique et le backlog.

Les éléments conservent des identifiants stables. Une mise à jour modifie
uniquement les sections concernées et ajoute un historique concis ; elle ne
renumérote pas les fonctionnalités et n'efface pas silencieusement les
décisions antérieures. Ce skill ne produit ni architecture, ni tâches de
backlog, ni document Word ou Google Docs.

Le plugin recommande un ordre de revue des fonctionnalités selon leurs
dépendances et les incertitudes, puis vous aide à trancher les comportements
manquants. Cet ordre de revue ne constitue pas une priorité de backlog. Une
revue seule ne modifie pas le fichier ; une évolution conserve les identifiants
et les parties non concernées.

## Prompts utiles

### Reprendre un parcours

```text
Reprends le parcours project-design dans /chemin/vers/mon-projet. Vérifie son
statut et effectue uniquement la prochaine action enregistrée. Si des réponses
sont attendues, repose exactement les questions restantes du Project Canvas.
```

### Créer directement un Canvas

```text
Utilise project-framing pour créer en français le Project Canvas à partir de
docs/brief.md et docs/atelier.md. Pose toutes les questions de décision
nécessaires et enregistre le résultat dans _project-design/project-canvas.md.
```

Le skill demande votre accord si `_project-design/` n'existe pas encore.

### Créer directement un document Word

```text
Utilise document-project-canvas pour transformer le Canvas validé
_project-design/project-canvas.md en document Word. Utilise la structure par
défaut, conserve strictement le contenu et vérifie le fichier natif avant de le
livrer dans _project-design/documents/project-canvas.docx.
```

### Créer ou faire évoluer la conception fonctionnelle

```text
Utilise functional-design à partir du Canvas validé
_project-design/project-canvas.md et des sources du projet. Produis en français
la conception fonctionnelle vivante dans
_project-design/functional-design.md. Utilise des identifiants stables,
référence chaque message depuis le catalogue global, conserve les questions
non résolues et n'ajoute ni architecture ni backlog.
```

Pour une évolution, fournissez aussi le Functional Design actuel et la source
de changement : décision approuvée, compte rendu, règle corrigée ou instruction
explicite.

### Vérifier un placeholder restant

```text
Vérifie si technical-design est disponible. S'il s'agit encore d'un
placeholder, explique ses futurs intrants et extrants sans créer de fichier.
```

## Fichiers obtenus dans un parcours complet actuel

```text
mon-projet/
├── _project-design/
│   ├── project-design-state.json
│   ├── project-canvas.md
│   ├── functional-design.md      # si le skill direct est demandé
│   └── documents/
│       └── project-canvas.docx   # seulement si Word est demandé
└── _sources/                     # créé au démarrage, ignoré par Git
    ├── source-index.md
    ├── links.md
    └── documents/
```

## Maintenance de ce guide

Ce guide doit être vérifié à chaque modification du plugin. Il doit être mis à
jour dès qu'une action disponible, une étape, une question, un intrant, un
extrant, un format, un chemin de livraison ou le statut d'un skill change. Si
aucune mise à jour n'est nécessaire, le compte rendu de validation doit le
signaler.
