# Short Fictional Project Canvas Example

This example demonstrates the standard current-state business view. It is not
a Golden Output, fixture result, or source of reusable project facts.

## Project Canvas — Muzzo

### 1. Contexte métier

Le centre associatif gère actuellement les demandes de réservation de salles
par courriel et dans un tableur partagé. Le rapprochement manuel des
disponibilités provoque des doubles réservations.

### 2. Objectifs et valeur attendue

- Réduire les doubles réservations confirmées.
- Donner aux associations une visibilité sur le traitement de leur demande.

### 3. Parties prenantes

- La direction du centre porte le projet et décide du périmètre.
- L'équipe d'accueil traite les demandes.
- L'équipe logistique tient les disponibilités des salles à jour.

### 4. Utilisateurs

- Les responsables associatifs déposent une demande de réservation.
- Les agents d'accueil examinent la demande et enregistrent la réponse.

### 5. Périmètre fonctionnel

#### MVP

| Module | Fonctionnalité | Description succincte |
| --- | --- | --- |
| Réservations | Créer une demande de réservation | Le responsable associatif choisit une salle et un créneau libres ; la demande est créée « En attente ». |
| Réservations | Lister et filtrer les demandes | Un responsable associatif ne voit que les demandes de son association. |
| Réservations | Annuler une réservation acceptée | Possible jusqu'à 48 heures avant le créneau, qui redevient libre. |
| Salles | Visualiser les disponibilités d'une salle | Les créneaux affichés sont ceux tenus à jour par l'équipe logistique. |
| Salles | Gérer les salles : lister, créer, éditer, supprimer | Référentiel tenu par l'équipe logistique. |
| Notifications | Notifier le demandeur de la réponse | **[Nouveau]** Un courriel est envoyé à chaque acceptation ou refus. |

Prestations incluses :

- reprise des réservations à venir du tableur partagé ;
- formation des agents d'accueil.

#### Hors MVP

| Module | Fonctionnalité | Description succincte |
| --- | --- | --- |
| Paiements | Payer une réservation en ligne | Exclu du MVP. |
| Réservations | Exporter le tableur des réservations | Supprimée, remplacée par la liste des demandes. |

### 6. Contraintes techniques

À définir.

### 7. Risques

| Risque | Impact | Solution |
| --- | --- | --- |
| Disponibilités des salles non tenues à jour | Doubles réservations malgré le nouvel outil | Mise à jour hebdomadaire des disponibilités par l'équipe logistique. |

### 8. Décisions

| Thème | Décision |
| --- | --- |
| Nom du produit | Le nom officiel est Muzzo. |
| Paiement | Les paiements en ligne sont exclus du MVP. |

### 9. Questions à décider

| N° | Question | Réponse |
| --- | --- | --- |
| 1 | Quel mode d'approbation des demandes doit être retenu pour le MVP ? | À apporter |
| 2 | Un responsable associatif peut-il annuler une réservation acceptée ? | Oui, jusqu'à 48 heures avant le créneau. |

### 10. Critères de succès

- Le nombre de doubles réservations confirmées diminue après la mise en
  service.

## Capacité à poursuivre

### Conception fonctionnelle — Non prête

Le mode d'approbation des demandes (question n° 1) doit être décidé avant de
détailler le processus fonctionnel.

### Conception technique — Prête avec réserves

L'étude de l'existant peut commencer, mais les contraintes techniques restent
à définir avant de valider une architecture.

### Préparation du backlog — Non prête

Le découpage détaillé attend la décision sur le mode d'approbation
(question n° 1) et la conception fonctionnelle correspondante.
