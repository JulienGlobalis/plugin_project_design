# Short Fictional Functional Design Example

This example illustrates structure, granularity, stable identifiers, and
cross-references. It is not a template, Golden Output, fixture result, or
source of reusable project facts.

# Functional Design — Muzzo

## Artefact Controls

- Applicable Canvas: Muzzo Project Canvas, validated baseline supplied for the
  exercise.
- Review status: Working draft.

### Change History

| Date | Affected IDs | Change type | Reason or source | Decision status |
| --- | --- | --- | --- | --- |
| To be defined | FNC-001, MSG-001 | Addition | Initial functional design from the supplied Canvas | Working draft |

## 1. Actors and Roles

| Actor ID | Actor or role | Responsibilities | Main interactions | Known rights or limits | Status |
| --- | --- | --- | --- | --- | --- |
| ACT-001 | Responsable associatif | Déposer une demande et consulter son état | FNC-001 | À définir | Établi |
| ACT-002 | Agent d'accueil | Examiner et accepter ou refuser une demande | FNC-001 | À définir | Établi |

## 2. Spécifications générales

### 2.1 Processus globaux

#### PRC-001 — Traiter une demande de réservation

- Déclencheur : un responsable associatif souhaite réserver une salle.
- Acteurs : ACT-001 et ACT-002.
- Étapes : dépôt, examen, décision, consultation de l'état.
- Résultat : la demande possède un état consultable.
- Fonctionnalités : FNC-001.
- Question : le mode d'approbation doit être décidé.

### 2.2 Produits, modules et fonctionnalités

| Feature ID | Product | Module | Feature | Objective | Target actors | Scope or maturity | Dependencies | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FNC-001 | Muzzo | Réservations | Déposer une demande | Permettre la saisie d'une demande de réservation | ACT-001 | MVP validé | Mode d'approbation à décider | [FNC-001](#31-fnc-001--déposer-une-demande) |

### 2.3 Règles de gestion globales

À définir.

## 3. Spécifications fonctionnelles détaillées

### 3.1 FNC-001 — Déposer une demande

#### Informations générales

| Property | Value |
| --- | --- |
| Stable ID | FNC-001 |
| Name | Déposer une demande |
| Product / module | Muzzo / Réservations |
| Functional maturity | Provisoire |
| Objective | Permettre à ACT-001 de transmettre une demande de réservation |
| Target actors | ACT-001 |
| Prerequisites | Le responsable associatif accède au service |
| Postconditions | La demande est enregistrée avec un état consultable |
| Dependencies | Le mode d'approbation reste à décider |
| Applicable global rules | À définir |
| Traceability | Project Canvas — périmètre fonctionnel et question d'approbation |

#### Scénario nominal

1. ACT-001 ouvre la saisie d'une demande.
2. Le service demande les informations de réservation.
3. ACT-001 renseigne les informations obligatoires et transmet la demande.
4. Le service enregistre la demande et confirme sa prise en compte.

#### Scénarios alternatifs valides

À définir.

#### Erreurs et exceptions

| Case ID | Trigger or condition | Expected handling | Resulting state | Visible feedback | Related message |
| --- | --- | --- | --- | --- | --- |
| ERR-FNC-001-01 | Une information obligatoire manque | La transmission est refusée et le champ concerné est signalé | La demande n'est pas transmise | Le champ concerné est identifié | MSG-001 |

#### Critères d'acceptation

- **AC-FNC-001-01** — Lorsque toutes les informations obligatoires sont
  valides, la demande est enregistrée et un état consultable lui est associé.
- **AC-FNC-001-02** — Lorsqu'une information obligatoire manque, la demande
  n'est pas transmise et l'information concernée est identifiée.

#### Questions et décisions nécessaires

- Quel mode d'approbation doit s'appliquer après le dépôt ?
- Quelles informations de réservation sont obligatoires ?

#### Interfaces et champs

##### UI-001 — Formulaire de demande

| Field ID | Label or information | Expected value / format | Required | Editable | Visibility | Default or source | Validation and behavior | Rule refs | Message refs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-001 | Salle demandée | Salle existante | À définir | Oui | ACT-001 | Aucune | Une valeur doit être fournie avant transmission | À définir | MSG-001 |
| FLD-002 | Date souhaitée | Date de réservation | À définir | Oui | ACT-001 | Aucune | Les règles de disponibilité restent à définir | À définir | MSG-001 |

#### Règles de gestion propres à la fonctionnalité

À définir.

#### Messages

| Message ID | Trigger | Channel | Recipient or audience | Purpose |
| --- | --- | --- | --- | --- |
| MSG-001 | Une information obligatoire manque | Information à l'écran | ACT-001 | Identifier l'information à compléter |

## 4. Annexes

### 4.1 Catalogue global des messages

| Message ID | Name | Channel | Trigger | Recipient or audience | Functional content or exact approved wording | Dynamic information | Conditions | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MSG-001 | Information obligatoire manquante | Information à l'écran | Transmission incomplète | ACT-001 | Indiquer l'information à compléter ; formulation exacte à définir | Libellé de l'information | Au moins une information obligatoire manque | Provisoire |

## Capacité à poursuivre

### Conception technique — Prête avec réserves

La structure fonctionnelle peut être étudiée, mais les champs obligatoires et
le mode d'approbation restent à décider.

### Préparation du backlog — Non prête

Les règles d'approbation et le contenu minimal d'une demande conditionnent le
découpage fiable des éléments de backlog.
