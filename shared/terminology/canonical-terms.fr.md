# Terminologie canonique - Français

- Langue : `fr`
- Statut : version initiale
- Référence sémantique normative :
  [Canonical Domain Model v0.1](canonical-domain-model.md)

## Objectif

Ce fichier fournit les libellés français recommandés pour les concepts
canoniques et les constructions partagées du plugin.

Il permet aux skills de produire des documents français cohérents sans
traduire librement le vocabulaire à chaque exécution.

## Limite normative

Les noms anglais et les définitions du Canonical Domain Model restent la
référence normative.

Ce fichier :

- traduit des libellés de présentation ;
- précise les variantes françaises admises ;
- signale les traductions susceptibles de confondre deux concepts ;
- ne crée, ne supprime et ne modifie aucun concept canonique ;
- ne modifie aucune responsabilité du Knowledge Model ou du Project Model.

En cas d'ambiguïté ou de divergence, le sens défini dans
`canonical-domain-model.md` prévaut.

## Concepts canoniques

| Concept canonique | Libellé français recommandé | Variantes admises | Distinction ou règle d'usage |
| --- | --- | --- | --- |
| `Project` | Projet | Initiative ; mission pour le contexte de conseil | Désigne l'initiative bornée, pas le produit ou le logiciel seul. |
| `Organization` | Organisation | Organisme ; entité ; unité organisationnelle selon le contexte | Porte le contexte, l'autorité ou les ressources. |
| `Stakeholder` | Partie prenante | Partie intéressée | Ne pas traduire systématiquement par `Acteur` : une partie prenante peut ne jamais utiliser le système. |
| `Actor` | Acteur | Utilisateur ; rôle utilisateur ; système externe selon le contexte | Ne pas confondre avec `Partie prenante`, qui exprime influence ou intérêt. |
| `Objective` | Objectif | But ; finalité | Décrit le résultat recherché, pas le besoin ni sa mesure. |
| `Scope` | Périmètre | Portée | Inclut les limites explicites et les éléments hors périmètre. |
| `Domain Term` | Terme métier | Terme du domaine ; entrée de glossaire | Conserve le vocabulaire propre au projet et ses ambiguïtés. |
| `Need` | Besoin | Besoin métier ; besoin utilisateur | Explique le problème ou l'attente ; ne pas le traduire comme une exigence approuvée. |
| `Capability` | Capacité | Capacité métier | Décrit ce qui doit être possible ; `Fonctionnalité` est souvent trop spécifique. |
| `Process` | Processus | Flux de travail ; parcours lorsque le sens comportemental est identique | Représente un enchaînement d'activités produisant ou modifiant un résultat. |
| `Requirement` | Exigence | Exigence fonctionnelle ; exigence non fonctionnelle ; exigence de qualité | Ne pas utiliser `Besoin`, qui conserve le pourquoi avant engagement. |
| `Business Rule` | Règle métier | Règle de gestion ; règle de service | Ne pas confondre avec une contrainte technique ou une exigence générale. |
| `Constraint` | Contrainte | Limite ; condition imposée | Restreint les choix acceptables sans exprimer un objectif. |
| `Assumption` | Hypothèse | Postulat provisoire | Ne jamais présenter comme un fait ou une décision validée. |
| `Option` | Option | Alternative ; proposition ; approche candidate | Reste un choix possible tant qu'aucune décision autorisée ne le sélectionne. |
| `Decision` | Décision | Choix validé ; résolution | Suppose une autorité explicite et peut sélectionner, rejeter ou différer une option. |
| `Open Question` | Question ouverte | Point à clarifier ; information attendue ; décision attendue | Représente un besoin explicite de clarification ou de décision. |
| `Risk` | Risque | Menace lorsque seuls les effets négatifs sont considérés | Décrit un événement ou une condition incertaine, pas un problème déjà observé. |
| `Issue` | Problème avéré | Problème actuel ; difficulté constatée | Ne pas traduire par `Risque` ; `Incident` est plus étroit et dépend du contexte. |
| `System Element` | Élément du système | Élément de solution ; application, module, composant ou service selon le contexte | `Composant` ne doit pas être utilisé comme traduction universelle, car il impose une granularité. |
| `Integration` | Intégration | Interface ; connexion ; échange selon le contexte | Représente une interaction gérée entre éléments ou frontières organisationnelles. |
| `Transition` | Transition | Migration ; déploiement ; bascule ; adoption selon l'aspect décrit | Décrit le changement entre une condition existante et une condition cible. |

## Libellés des modèles partagés

Les entrées suivantes facilitent la rédaction mais ne sont pas des concepts
canoniques.

| Libellé anglais | Libellé français recommandé | Couche |
| --- | --- | --- |
| `Knowledge Model` | Modèle de connaissances | Architecture |
| `Assertion` | Assertion | Knowledge Model |
| `Assertion Group` | Groupe d'assertions | Knowledge Model |
| `Provenance` | Provenance | Knowledge Model |
| `Confidence` | Niveau de confiance | Knowledge Model |
| `Uncertainty` | Incertitude | Knowledge Model |
| `Validation Status` | Statut de validation | Knowledge Model |
| `Project Model` | Modèle projet normalisé | Architecture |
| `Project View` | Vue projet | Project Model |
| `Project Element` | Élément projet | Project Model |
| `Project Relationship` | Relation entre éléments du projet | Project Model |
| `Normalization Status` | Statut de normalisation | Project Model |
| `Lifecycle Perspective` | Perspective de cycle de vie | Project Model |
| `Knowledge Basis` | Base de justification | Project Model |

`Base de connaissances` n'est pas recommandé pour `Knowledge Basis`, car
cette expression désigne habituellement un référentiel de connaissances
plutôt que les assertions qui justifient un élément normalisé.

## Valeurs partagées

### Statut de normalisation

| Valeur | Libellé français |
| --- | --- |
| `Established` | Établi |
| `Provisional` | Provisoire |
| `Unresolved` | Non résolu |

### Perspective de cycle de vie

| Valeur | Libellé français |
| --- | --- |
| `Existing` | Existant |
| `Target` | Cible |
| `Transition` | Transition |

### Rôle dans la base de justification

| Valeur | Libellé français |
| --- | --- |
| `Supporting` | À l'appui |
| `Qualifying` | De qualification |
| `Opposing` | En opposition |

## Règles de rédaction

1. Utiliser le libellé recommandé dans les titres, tableaux, statuts et
   structures répétées.
2. Employer une variante admise dans la prose uniquement si elle conserve le
   sens canonique.
3. Préserver les distinctions `Partie prenante` / `Acteur`, `Besoin` /
   `Exigence`, `Option` / `Décision` et `Risque` / `Problème avéré`.
4. Ne pas traduire automatiquement les Domain Terms propres au projet. Leur
   langue, leurs alias et leur définition dépendent des sources et du
   glossaire validé du projet.
5. Conserver les noms canoniques anglais comme clés de référence internes,
   même lorsqu'un document présente uniquement les libellés français.
6. Signaler un libellé manquant ou ambigu au lieu d'inventer une traduction
   qui modifie le sens.

## Résolution de langue

L'anglais canonique reste la langue par défaut lorsqu'aucune langue de sortie
n'est demandée.

Pour une sortie localisée :

1. utiliser la ressource régionale exacte lorsqu'elle existe ;
2. sinon utiliser la ressource de langue de base, par exemple `fr` pour
   `fr-FR` ou `fr-CA` ;
3. si aucune ressource correspondante n'existe, signaler le manque ;
4. n'utiliser l'anglais qu'avec une règle de repli explicite ou l'accord de
   l'utilisateur ;
5. ne jamais utiliser silencieusement une autre langue localisée.

Le suffixe `fr` représente ici le français générique. Une future ressource
`canonical-terms.fr-FR.md` ou `canonical-terms.fr-CA.md` ne devra contenir que
les différences régionales justifiées.

## Points à confirmer par l'usage

- Les variantes réellement utilisées par les premiers livrables de
  `project-framing`.
- Le besoin éventuel de libellés régionaux.
- La traduction des futurs concepts propres aux méthodologies de skills.
- La stratégie de localisation des Domain Terms définis par un projet.
