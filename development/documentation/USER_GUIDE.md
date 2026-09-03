# Guide utilisateur de `project-design`

Ce guide résume les actions prises en charge par le plugin, les questions qu'il
pose, les informations à lui fournir et les livrables obtenus.

Dernière vérification : 3 septembre 2026.

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
| 1. Autorisation | Accord pour utiliser le plugin et créer ou réutiliser `_project-design/` | Confirmation explicite | Espace de travail et fichier d'état |
| 2. Étape | Quelle étape lancer ; `project-framing` est proposé par défaut | Choix de `project-framing` | Étape enregistrée |
| 3. Livrables | Canvas seul, Word ou Google Docs ; modèle par défaut, local ou Drive | Format et modèle éventuel | Choix documentaire enregistré |
| 4. Sources | Conserver les sources en place ou les centraliser | Stratégie de sources et autorisations de copie | Sources référencées ou `_sources/` initialisé |
| 5. Projet | Description, documents sources ou les deux | Brief, notes, règles, décisions ou liens utiles | Intrants prêts pour l'analyse |
| 6. Cadrage | Questions de décision réellement nécessaires | Réponses complètes, partielles ou reports explicites | Canvas progressivement complété |
| 7. Validation | Approbation du Canvas ou demande d'une nouvelle itération | Accord ou corrections | Canvas validé |
| 8. Document | Rien de plus si le format et le modèle sont déjà enregistrés | Éventuelles contraintes de présentation déjà annoncées | Document natif vérifié |

### Questions posées pendant le cadrage

Le plugin pose uniquement les questions dont la réponse conditionne le projet,
par exemple :

- quel périmètre doit être retenu ;
- quelle décision bloque la conception fonctionnelle ;
- quelle contrainte doit être connue avant la conception technique ;
- quelle information manque avant de préparer un backlog fiable.

Il n'applique aucune limite arbitraire au nombre de questions. Vous pouvez
répondre à tout le lot, répondre partiellement ou reporter explicitement une
question. Les questions restantes sont conservées dans le Canvas et reprises
à l'identique dans une conversation suivante.

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

Si vous choisissez de centraliser les sources, chaque copie locale exige votre
accord. L'original n'est pas modifié, la copie n'écrase aucun fichier et son
empreinte SHA-256 est enregistrée. Les documents Google natifs restent des
liens. Le dossier `/_sources/` est ajouté au `.gitignore` par défaut.

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

Un bloc non numéroté indique ensuite séparément si la conception
fonctionnelle, la conception technique et la préparation du backlog sont
prêtes, prêtes avec réserves ou non prêtes.

Le Canvas décrit uniquement la position courante validée. Un audit demandé
explicitement reste séparé dans
`_project-design/project-canvas-audit.md`.

## Extrant documentaire optionnel

Après approbation du Canvas, `document-project-canvas` peut produire :

- `_project-design/documents/project-canvas.md` ;
- `_project-design/documents/project-canvas.docx` ;
- un lien vers un Google Docs natif vérifié.

Le skill conserve strictement le contenu du Canvas. Il n'invente ni résumé, ni
sous-titre, ni métadonnée, ni approbation et ne fusionne pas un audit séparé
sans demande explicite.

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
└── _sources/                     # seulement si la centralisation est choisie
```

## Maintenance de ce guide

Ce guide doit être vérifié à chaque modification du plugin. Il doit être mis à
jour dès qu'une action disponible, une étape, une question, un intrant, un
extrant, un format, un chemin de livraison ou le statut d'un skill change. Si
aucune mise à jour n'est nécessaire, le compte rendu de validation doit le
signaler.
