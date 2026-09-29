# Globalis Project Design

Marketplace Globalis fournissant le plugin `project-design` pour Codex et
Claude Code.

Le plugin structure la conception de projets applicatifs et logiciels : cadrage
et Project Canvas, conception fonctionnelle vivante, puis restitution
documentaire en Markdown, Microsoft Word ou Google Docs. Il sépare la
production de la connaissance projet de sa mise en forme, ne crée rien sans
consentement explicite et regroupe tous ses livrables sous `_project-design/`
à la racine du projet cible.

## Installation recommandée pour une équipe

Pour des utilisateurs non techniques dans un workspace ChatGPT/Codex, un
administrateur peut installer ce plugin puis le publier dans le workspace en
sélectionnant les rôles autorisés. Les utilisateurs l'installent ensuite depuis
le répertoire graphique des plugins, sans manipuler de ligne de commande.

Le dépôt GitLab est privé : chaque installation directe depuis GitLab nécessite
un accès valide au groupe `globalis-ms` et une clé SSH enregistrée sur GitLab.

La marketplace et le plugin portent tous deux le nom `project-design`.
L'identifiant d'installation est donc `project-design@project-design`.

## Installation dans Codex

Ajouter une seule fois la marketplace :

```bash
codex plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
```

Installer ensuite le plugin depuis le répertoire des plugins de l'application,
ou avec :

```bash
codex plugin add project-design@project-design
```

Démarrer une nouvelle conversation avant la première utilisation.

## Installation dans Claude Code

Ajouter la marketplace puis installer le plugin :

```bash
claude plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
claude plugin install project-design@project-design
```

La même opération peut être réalisée depuis `/plugin` ou depuis le navigateur
de plugins de Claude Code Desktop. Redémarrer Claude Code avant la première
utilisation.

Les skills Claude Code sont accessibles sous la forme
`/project-design:<skill>`, par exemple :

```text
/project-design:project-design
/project-design:project-framing
/project-design:functional-design
/project-design:document-project-canvas
```

## Mise à jour

Codex :

```bash
codex plugin marketplace upgrade project-design
codex plugin add project-design@project-design
```

Claude Code :

```bash
claude plugin marketplace update project-design
claude plugin update project-design@project-design
```

Rafraîchir la marketplace avant la mise à jour du plugin, sinon l'ancienne
copie reste installée. Démarrer ensuite une nouvelle conversation Codex ou
redémarrer Claude Code.

## Skills disponibles

| Skill | Statut | Rôle | Livrable |
| --- | --- | --- | --- |
| `project-design` | Implémenté | Entrée guidée : présentation, consentement, initialisation, choix d'étape, reprise entre conversations | `_project-design/project-design-state.json` (état de contrôle uniquement) |
| `project-framing` | Implémenté | Étape 1 : cadrage et Project Canvas en dix sections | `_project-design/project-canvas.md` |
| `functional-design` | Implémenté | Étape 2 : conception fonctionnelle vivante à partir d'un Canvas validé | `_project-design/functional-design.md` |
| `document-project-canvas` | Implémenté | Restitution documentaire du Canvas validé | `_project-design/documents/`, `.docx` ou lien Google Docs |
| `technical-design` | Placeholder | Conception technique future | Aucun |
| `product-backlog` | Placeholder | Backlog traçable futur | Aucun |
| `document-functional-design` | Placeholder | Spécifications fonctionnelles futures | Aucun |
| `document-technical-design` | Placeholder | Spécifications techniques futures | Aucun |
| `document-product-backlog` | Placeholder | Document de backlog futur | Aucun |

Un placeholder annonce son statut et ses entrées ou sorties prévues, mais ne
crée aucun fichier. Chaque skill spécialisé reste appelable directement.

Le parcours pas à pas, les questions posées, les intrants et les extrants sont
décrits dans le [guide utilisateur](development/documentation/USER_GUIDE.md).

## Exemples de prompts

Les prompts sont utilisables dans Codex comme dans Claude Code. Remplacer les
chemins, langues et formats par les valeurs du projet.

Démarrer le parcours guidé (`project-design`) :

```text
Utilise le skill project-design pour guider la spécification de l'application
située dans /chemin/vers/mon-projet. Présente les skills disponibles et les
règles du répertoire, puis demande mon consentement explicite avant de créer
ou réutiliser _project-design/.
```

Reprendre après un changement de conversation (`project-design`) :

```text
Reprends le workflow project-design dans /chemin/vers/mon-projet. Vérifie
d'abord le statut persisté et exécute uniquement la prochaine action
enregistrée. Si des réponses de cadrage sont en attente, présente exactement
les questions non répondues déjà présentes dans le Project Canvas.
```

Cadrer directement à partir de sources (`project-framing`) :

```text
Utilise le skill project-framing pour /chemin/vers/mon-projet. Construis un
Project Canvas en français à partir de docs/brief.md et de
docs/notes-atelier.md. Conserve les décisions non tranchées, pose toutes les
questions de décision nécessaires et enregistre l'artefact dans
_project-design/project-canvas.md.
```

Créer la conception fonctionnelle (`functional-design`) :

```text
Utilise functional-design pour /chemin/vers/mon-projet. Construis le
Functional Design en français à partir du Canvas validé
_project-design/project-canvas.md. Utilise des identifiants stables, conserve
les décisions non résolues, définis chaque message une seule fois dans le
catalogue et enregistre l'artefact dans _project-design/functional-design.md,
sans architecture technique ni backlog.
```

Produire le document Word du Canvas (`document-project-canvas`) :

```text
Utilise le skill document-project-canvas pour transformer le Canvas validé
_project-design/project-canvas.md en document Microsoft Word professionnel en
français. Utilise la structure par défaut, conserve tout le sens métier et les
questions ouvertes, enregistre le fichier dans
_project-design/documents/project-canvas.docx et vérifie le résultat avant
livraison.
```

Vérifier la disponibilité d'un placeholder (`technical-design`,
`product-backlog`, `document-functional-design`, `document-technical-design`,
`document-product-backlog`) :

```text
Vérifie le skill technical-design pour /chemin/vers/mon-projet. S'il est
encore un placeholder, présente sa couverture prévue et ne génère aucun
artefact.
```

## Structure

```text
.
├── .agents/plugins/marketplace.json     # Marketplace Codex
├── .claude-plugin/marketplace.json      # Marketplace Claude Code
├── plugins/
│   └── project-design/                  # Bundle installable
│       ├── .codex-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── README.md
│       ├── shared/                      # Modèles, terminologie, règles qualité
│       └── skills/
│           ├── project-design/          # SKILL.md, references/, scripts/
│           ├── project-framing/
│           ├── functional-design/
│           ├── document-project-canvas/
│           └── ...                      # Cinq placeholders
├── development/                         # Tests, fixtures, contexte, docs (non installés)
├── integrations/                        # Notes par plateforme
├── AGENTS.md
├── CLAUDE.md
├── CHANGELOG.md
└── CONTRIBUTING.md
```

Le dossier `plugins/project-design/skills/` est l'unique source des skills.
Les deux plugins et les deux marketplaces utilisent cette même source ;
`development/` reste versionné mais n'est jamais installé.

L'architecture complète (modèles, responsabilités, flux et dépendances) est
décrite dans la
[vue d'ensemble de l'architecture](development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md).

## Validation pour les mainteneurs

Avant chaque publication :

```bash
python3 -m unittest discover -s development/tests/tools -q
claude plugin validate plugins/project-design
claude plugin validate .
```

Valider également le plugin Codex et chaque skill modifié, suivre la
[stratégie de test](development/tests/TESTING.md), puis mettre à jour le
[CHANGELOG](CHANGELOG.md) et le [guide utilisateur](development/documentation/USER_GUIDE.md).

Incrémenter la version de `plugins/project-design/.claude-plugin/plugin.json`
à chaque publication : Claude Code ne détecte pas une mise à jour si la
version reste identique. Créer ensuite le tag correspondant (`vX.Y.Z`).

Vérifier enfin une installation réelle depuis la marketplace et tester dans
une nouvelle conversation ou session.
