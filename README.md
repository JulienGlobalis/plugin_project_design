# Globalis Project Design

[English](#english) · [Français](#français)

---

## English

Globalis marketplace providing the `project-design` plugin for Codex and
Claude Code.

The plugin structures the design of application and software projects:
framing with a Project Canvas, a living Functional Design, then documentary
restitution in Markdown, Microsoft Word, or Google Docs. It keeps project
knowledge separate from its formatting, creates nothing without explicit
consent, and stores all its deliverables under `_project-design/` at the root
of the target project.

### Contents

- [Installation](#installation)
- [Update and removal](#update-and-removal)
- [Usage](#usage)
- [Available skills](#available-skills)
- [What the plugin writes in a project](#what-the-plugin-writes-in-a-project)
- [Resuming and next steps](#resuming-and-next-steps)
- [Verification commands](#verification-commands)
- [Repository structure](#repository-structure)
- [Maintainer validation](#maintainer-validation)

### Installation

The GitLab repository is private: installing directly from GitLab requires
valid access to the `globalis-ms` group and an SSH key registered on GitLab.

For non-technical users in a ChatGPT/Codex workspace, an administrator can
install this plugin and publish it to the workspace for selected roles. Users
then install it from the graphical plugin directory.

The marketplace and the plugin are both named `project-design`, so the
installation identifier is `project-design@project-design`.

**Claude Code**

```bash
claude plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
claude plugin install project-design@project-design
```

The same can be done from `/plugin` or from the Claude Code Desktop plugin
browser. Restart Claude Code before first use.

**Codex**

```bash
codex plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
codex plugin add project-design@project-design
```

The plugin can also be installed from the application's plugin directory.
Start a new conversation before first use.

### Update and removal

| Action | Claude Code | Codex |
|---|---|---|
| Update | `claude plugin marketplace update project-design` then `claude plugin update project-design@project-design` | `codex plugin marketplace upgrade project-design` then `codex plugin add project-design@project-design` |
| Check installed version | `claude plugin list` | `codex plugin list` |
| Uninstall | `claude plugin uninstall project-design@project-design` | `codex plugin remove project-design@project-design` |
| Remove the marketplace | `claude plugin marketplace remove project-design` | `codex plugin marketplace remove project-design` |

Refresh the marketplace before updating the plugin, otherwise the former copy
stays installed. Restart Claude Code or start a new Codex conversation after
an update.

### Usage

#### Running a skill

| Assistant | Invocation |
|---|---|
| Claude Code | `/project-design:<skill>`, for example `/project-design:project-design` or `/project-design:project-framing` |
| Codex | Name the skill in the request, for example `Use project-design for /path/to/my-project.` |

The skills also trigger on a natural request, such as "frame my project".
Start the assistant from the root of the target project.

#### Default guided run

Launched through `project-design`, the plugin chains these steps:

1. **Consent:** it presents the skills and the folders it will create, then
   asks whether you agree to use the plugin for the project. A refusal creates
   nothing. After agreement it creates `_project-design/`,
   `_project-design/documents/`, the private `_sources/` workspace
   (`documents/`, `source-index.md`, `links.md`), and adds `/_sources/` to the
   `.gitignore`.
2. **Stage:** it asks which stage to run and proposes `project-framing` by
   default, the only stage routed by the guided workflow.
3. **Delivery:** the Markdown Canvas is always produced. It asks whether you
   also want Word or Google Docs and, if so, which template: a local file, a
   Drive link, or the default structure.
4. **Sources:** it invites you to drop documents into `_sources/documents/`,
   to provide links, or to describe the project in the conversation. Each
   document is indexed with its SHA-256; copying a file located elsewhere
   requires your approval, file by file; no original is modified. In the same
   message it asks whether a technical foundation is imposed or already
   chosen, and whether it must prepare future evolutions.
5. **Analysis:** it reads every source completely (OCR or page-by-page reading
   when extraction is poor) and writes a first Project Canvas with ten
   sections. Functional Scope, Risks, Decisions, and Questions are tables. The
   delivery message lists how each source was read.
6. **Question batches:** it presents every necessary decision question with
   options, consequences, and a recommendation. You can answer all, part, or
   explicitly defer some. Unanswered questions show `To be provided`; answered
   ones keep their number and answer. New questions that appear during a
   pending batch are proposed as candidates for the next batch.
7. **Approval:** it links the Canvas, summarizes the changes and remaining
   blockers, and asks for approval or another iteration.
8. **Document:** if requested, `document-project-canvas` produces the `.docx`
   or the native Google Docs and verifies it.

Every transition is recorded in a state file: no step can be skipped, and a
new conversation resumes exactly where the previous one stopped.

#### Typical requests

Commands below are for Claude Code. In Codex, drop the `/project-design:<skill>`
prefix and name the skill in the sentence. Requests may be written in any
language.

| Goal | Command |
|---|---|
| Start the guided workflow | `/project-design:project-design Guide the specification of the application in /path/to/my-project. Ask for my consent before creating _project-design/.` |
| Resume after a conversation change | `/project-design:project-design Resume the workflow in /path/to/my-project from the recorded next action.` |
| Frame directly from sources | `/project-design:project-framing Build a Project Canvas in English from docs/brief.md and docs/workshop-notes.md for /path/to/my-project.` |
| Create the Functional Design | `/project-design:functional-design Build the Functional Design from the validated _project-design/project-canvas.md, with stable identifiers and no technical architecture or backlog.` |
| Produce the Word document of the Canvas | `/project-design:document-project-canvas Turn the validated Canvas into a professional Word document with the default structure and verify it before delivery.` |
| Check a placeholder | `/project-design:technical-design Check this skill. If it is still a placeholder, describe its planned coverage and generate nothing.` |

The more the request says (sources, language, format, decisions already
made), the fewer questions the plugin asks.

### Available skills

| Skill | Status | Role | Deliverable |
|---|---|---|---|
| `project-design` | Implemented | Guided entry: consent, initialization, stage choice, resumption across conversations | `_project-design/project-design-state.json` (control state only) |
| `project-framing` | Implemented | Step 1: framing and ten-section Project Canvas | `_project-design/project-canvas.md` |
| `functional-design` | Implemented | Step 2: living Functional Design from a validated Canvas | `_project-design/functional-design.md` |
| `document-project-canvas` | Implemented | Documentary restitution of the validated Canvas | `_project-design/documents/`, `.docx`, or Google Docs link |
| `technical-design` | Placeholder | Future technical design | None |
| `product-backlog` | Placeholder | Future traceable backlog | None |
| `document-functional-design` | Placeholder | Future functional specifications | None |
| `document-technical-design` | Placeholder | Future technical specifications | None |
| `document-product-backlog` | Placeholder | Future backlog document | None |

A placeholder announces its status and planned inputs and outputs but creates
no file. Each specialized skill stays directly callable.

### What the plugin writes in a project

Only after consent, and only what was requested:

| File | Purpose |
|---|---|
| `_project-design/project-design-state.json` | Guided workflow control state: phase, choices, counters, history; never business content |
| `_project-design/project-canvas.md` | Project Canvas: current validated position of the project |
| `_project-design/project-canvas-audit.md` | Traceability audit, only when explicitly requested |
| `_project-design/functional-design.md` | Living Functional Design, when the skill is called |
| `_project-design/documents/` | Final documents, for example `project-canvas.docx` |
| `_sources/documents/`, `source-index.md`, `links.md` | Private source intake, Git-ignored; originals stay authoritative |

### Resuming and next steps

- A new conversation resumes from the recorded step; pending questions are
  presented again exactly, without duplication. There is no reset command.
- A conversation change or a technical request is never treated as an answer
  or a deferral.
- At the end of framing, the plugin recommends the next useful action, usually
  `functional-design`, which is called directly: the guided workflow does not
  route it yet.

The step-by-step journey, questions, inputs, and outputs are described in the
[user guide](development/documentation/USER_GUIDE.md) (French).

### Verification commands

| Check | Command |
|---|---|
| Installed plugin | `claude plugin list` or `codex plugin list` |
| Current workflow step | `python3 plugins/project-design/skills/project-design/scripts/workflow.py status --project-root <project>` |
| Plugin tests | `python3 -m unittest discover -s development/tests/tools -q` |

### Repository structure

```text
.
├── .agents/plugins/marketplace.json     # Codex marketplace
├── .claude-plugin/marketplace.json      # Claude Code marketplace
├── plugins/
│   └── project-design/                  # Installable bundle
│       ├── .codex-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── README.md
│       ├── shared/                      # Models, terminology, quality rules
│       └── skills/
│           ├── project-design/          # SKILL.md, references/, scripts/
│           ├── project-framing/
│           ├── functional-design/
│           ├── document-project-canvas/
│           └── ...                      # Five placeholders
├── development/                         # Tests, fixtures, context, docs (not installed)
├── integrations/                        # Platform notes
├── AGENTS.md
├── CLAUDE.md
├── CHANGELOG.md
└── CONTRIBUTING.md
```

The `plugins/project-design/skills/` folder is the single source of the
skills. Both plugins and both marketplaces use it; `development/` is versioned
but never installed. The full architecture is described in the
[architecture overview](development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md).

### Maintainer validation

Before each release, run the tests, validate each modified skill, the Codex
plugin, and the Claude Code plugin and marketplace
(`claude plugin validate plugins/project-design`, `claude plugin validate .`),
follow the [test strategy](development/tests/TESTING.md), and update the
[CHANGELOG](CHANGELOG.md) and the user guide. Increment the version in
`plugins/project-design/.claude-plugin/plugin.json` for each release: Claude
Code does not detect an update when the version is unchanged. Then check a
real installation from the marketplace and test in a new conversation or
session. The full checklist is in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Français

Marketplace Globalis fournissant le plugin `project-design` pour Codex et
Claude Code.

Le plugin structure la conception de projets applicatifs et logiciels :
cadrage et Project Canvas, conception fonctionnelle vivante, puis restitution
documentaire en Markdown, Microsoft Word ou Google Docs. Il sépare la
connaissance projet de sa mise en forme, ne crée rien sans consentement
explicite et regroupe tous ses livrables sous `_project-design/` à la racine
du projet cible.

### Sommaire

- [Installation](#installation-1)
- [Mise à jour et désinstallation](#mise-à-jour-et-désinstallation)
- [Utilisation](#utilisation)
- [Skills disponibles](#skills-disponibles)
- [Ce que le plugin écrit dans un projet](#ce-que-le-plugin-écrit-dans-un-projet)
- [Reprise et suite](#reprise-et-suite)
- [Commandes de vérification](#commandes-de-vérification)
- [Structure du dépôt](#structure-du-dépôt)
- [Validation pour les mainteneurs](#validation-pour-les-mainteneurs)

### Installation

Le dépôt GitLab est privé : chaque installation directe depuis GitLab nécessite
un accès valide au groupe `globalis-ms` et une clé SSH enregistrée sur GitLab.

Pour des utilisateurs non techniques dans un workspace ChatGPT/Codex, un
administrateur peut installer ce plugin puis le publier dans le workspace en
sélectionnant les rôles autorisés. Les utilisateurs l'installent ensuite depuis
le répertoire graphique des plugins.

La marketplace et le plugin portent tous deux le nom `project-design` :
l'identifiant d'installation est donc `project-design@project-design`.

**Claude Code**

```bash
claude plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
claude plugin install project-design@project-design
```

La même opération peut être réalisée depuis `/plugin` ou depuis le navigateur
de plugins de Claude Code Desktop. Redémarrer Claude Code avant la première
utilisation.

**Codex**

```bash
codex plugin marketplace add git@gitlab.com:globalis-ms/marketplace/llm_plugin_project_design.git
codex plugin add project-design@project-design
```

Le plugin peut aussi être installé depuis le répertoire des plugins de
l'application. Démarrer une nouvelle conversation avant la première
utilisation.

### Mise à jour et désinstallation

| Action | Claude Code | Codex |
|---|---|---|
| Mettre à jour | `claude plugin marketplace update project-design` puis `claude plugin update project-design@project-design` | `codex plugin marketplace upgrade project-design` puis `codex plugin add project-design@project-design` |
| Vérifier la version installée | `claude plugin list` | `codex plugin list` |
| Désinstaller | `claude plugin uninstall project-design@project-design` | `codex plugin remove project-design@project-design` |
| Retirer la marketplace | `claude plugin marketplace remove project-design` | `codex plugin marketplace remove project-design` |

Rafraîchir la marketplace avant la mise à jour du plugin, sinon l'ancienne
copie reste installée. Redémarrer Claude Code ou démarrer une nouvelle
conversation Codex après une mise à jour.

### Utilisation

#### Lancer un skill

| Assistant | Invocation |
|---|---|
| Claude Code | `/project-design:<skill>`, par exemple `/project-design:project-design` ou `/project-design:project-framing` |
| Codex | Nommer le skill dans la demande, par exemple `Utilise project-design pour /chemin/vers/mon-projet.` |

Les skills se déclenchent aussi sur une demande formulée naturellement, par
exemple « cadre mon projet ». Lancer l'assistant depuis la racine du projet
cible.

#### Déroulé guidé par défaut

Lancé via `project-design`, le plugin enchaîne les étapes suivantes :

1. **Accord :** il présente les skills et les dossiers qu'il va créer, puis
   demande si vous acceptez d'utiliser le plugin pour le projet. Un refus ne
   crée rien. Après accord, il crée `_project-design/`,
   `_project-design/documents/`, l'espace privé `_sources/` (`documents/`,
   `source-index.md`, `links.md`) et ajoute `/_sources/` au `.gitignore`.
2. **Étape :** il demande quelle étape lancer et propose `project-framing` par
   défaut, seule étape routée par le parcours guidé.
3. **Livrables :** le Canvas Markdown est toujours produit. Il demande si vous
   voulez aussi un document Word ou Google Docs et, si oui, quel modèle : un
   fichier local, un lien Drive ou la structure par défaut.
4. **Sources :** il vous invite à déposer vos documents dans
   `_sources/documents/`, à fournir des liens ou à décrire le projet dans la
   conversation. Chaque document est indexé avec son empreinte SHA-256 ;
   copier un fichier situé ailleurs exige votre accord, fichier par fichier ;
   aucun original n'est modifié. Dans le même message, il demande si un socle
   technique est imposé ou déjà choisi et s'il doit préparer des évolutions
   futures.
5. **Analyse :** il lit intégralement chaque source (OCR ou lecture page par
   page si l'extraction est mauvaise) et rédige un premier Project Canvas en
   dix sections. Le périmètre fonctionnel, les risques, les décisions et les
   questions sont présentés en tableaux. Le message de livraison indique
   comment chaque source a été lue.
6. **Lots de questions :** il présente toutes les questions de décision
   nécessaires, avec options, conséquences et recommandation. Vous pouvez tout
   répondre, répondre en partie ou reporter explicitement certaines
   questions. Une question sans réponse affiche « À apporter » ; une question
   répondue garde son numéro et sa réponse. Les nouvelles questions apparues
   pendant un lot en attente sont proposées comme candidates pour le lot
   suivant.
7. **Validation :** il donne le lien du Canvas, résume les changements et les
   blocages restants, puis demande l'approbation ou une nouvelle itération.
8. **Document :** si demandé, `document-project-canvas` produit le `.docx` ou
   le Google Docs natif et le vérifie.

Chaque transition est enregistrée dans un fichier d'état : aucune étape ne
peut être sautée et une nouvelle conversation reprend exactement là où la
précédente s'est arrêtée.

#### Demandes types

Les commandes ci-dessous sont données pour Claude Code. Dans Codex, retirer le
préfixe `/project-design:<skill>` et nommer le skill dans la phrase.

| Objectif | Commande |
|---|---|
| Démarrer le parcours guidé | `/project-design:project-design Guide la spécification de l'application située dans /chemin/vers/mon-projet. Demande mon accord avant de créer _project-design/.` |
| Reprendre après un changement de conversation | `/project-design:project-design Reprends le workflow dans /chemin/vers/mon-projet à partir de la prochaine action enregistrée.` |
| Cadrer directement à partir de sources | `/project-design:project-framing Construis un Project Canvas en français à partir de docs/brief.md et docs/notes-atelier.md pour /chemin/vers/mon-projet.` |
| Créer la conception fonctionnelle | `/project-design:functional-design Construis le Functional Design à partir du Canvas validé _project-design/project-canvas.md, avec des identifiants stables, sans architecture technique ni backlog.` |
| Produire le document Word du Canvas | `/project-design:document-project-canvas Transforme le Canvas validé en document Word professionnel avec la structure par défaut et vérifie-le avant livraison.` |
| Vérifier un placeholder | `/project-design:technical-design Vérifie ce skill. S'il est encore un placeholder, présente sa couverture prévue et ne génère rien.` |

Plus la demande contient d'informations (sources, langue, format, décisions
déjà prises), moins le plugin pose de questions.

### Skills disponibles

| Skill | Statut | Rôle | Livrable |
|---|---|---|---|
| `project-design` | Implémenté | Entrée guidée : consentement, initialisation, choix d'étape, reprise entre conversations | `_project-design/project-design-state.json` (état de contrôle uniquement) |
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

### Ce que le plugin écrit dans un projet

Uniquement après consentement, et seulement ce qui a été demandé :

| Fichier | Rôle |
|---|---|
| `_project-design/project-design-state.json` | État de contrôle du parcours guidé : phase, choix, compteurs, historique ; jamais de contenu métier |
| `_project-design/project-canvas.md` | Project Canvas : position courante validée du projet |
| `_project-design/project-canvas-audit.md` | Audit de traçabilité, uniquement sur demande explicite |
| `_project-design/functional-design.md` | Conception fonctionnelle vivante, quand le skill est appelé |
| `_project-design/documents/` | Documents finaux, par exemple `project-canvas.docx` |
| `_sources/documents/`, `source-index.md`, `links.md` | Espace privé des sources, ignoré par Git ; les originaux font foi |

### Reprise et suite

- Une nouvelle conversation reprend à l'étape enregistrée ; les questions en
  attente sont reposées à l'identique, sans doublon. Il n'existe pas de
  commande de réinitialisation.
- Un changement de conversation ou une demande technique n'est jamais
  considéré comme une réponse ou un report.
- À la fin du cadrage, le plugin recommande la prochaine action utile,
  généralement `functional-design`, qui s'appelle directement : le parcours
  guidé ne la route pas encore.

Le parcours pas à pas, les questions posées, les intrants et les extrants sont
décrits dans le [guide utilisateur](development/documentation/USER_GUIDE.md).

### Commandes de vérification

| Vérifier | Commande |
|---|---|
| Plugin installé | `claude plugin list` ou `codex plugin list` |
| Étape courante du parcours | `python3 plugins/project-design/skills/project-design/scripts/workflow.py status --project-root <projet>` |
| Tests du plugin | `python3 -m unittest discover -s development/tests/tools -q` |

### Structure du dépôt

L'arborescence est identique à celle de la [section anglaise](#repository-structure).
Le dossier `plugins/project-design/skills/` est l'unique source des skills.
Les deux plugins et les deux marketplaces utilisent cette même source ;
`development/` reste versionné mais n'est jamais installé. L'architecture
complète est décrite dans la
[vue d'ensemble de l'architecture](development/documentation/PLUGIN_ARCHITECTURE_OVERVIEW.md).

### Validation pour les mainteneurs

Avant chaque publication, lancer les tests, valider chaque skill modifié, le
plugin Codex, puis le plugin et la marketplace Claude Code
(`claude plugin validate plugins/project-design`, `claude plugin validate .`),
suivre la [stratégie de test](development/tests/TESTING.md) et mettre à jour le
[CHANGELOG](CHANGELOG.md) et le guide utilisateur. Incrémenter la version de
`plugins/project-design/.claude-plugin/plugin.json` à chaque publication :
Claude Code ne détecte pas une mise à jour si la version reste identique.
Vérifier ensuite une installation réelle depuis la marketplace et tester dans
une nouvelle conversation ou session. La liste complète est dans
[CONTRIBUTING.md](CONTRIBUTING.md).
