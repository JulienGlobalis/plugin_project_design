# Évaluation du plugin comme appui au chef de projet

Date : 5 septembre 2026. Base examinée : `921f4ba`.

## Avis

Le plugin possède une base solide pour cadrer un projet et conserver une
conception cohérente. Avant cette correction, son caractère directif reposait
surtout sur l'ordre des étapes et les validations. Il disait davantage au chef
de projet ce qu'il devait fournir que ce qu'il avait intérêt à décider, pourquoi
et avec quelles conséquences.

La correction renforce l'accompagnement dans les capacités existantes. Le
plugin reste un outil de cadrage et de conception : il ne couvre pas encore le
pilotage complet des délais, du budget, des engagements et de l'exécution.

## Évaluation par usage

| Besoin du chef de projet | Évaluation du dépôt initial | Apport de la correction |
| --- | --- | --- |
| Comprendre où commencer | Parcours explicite, mais choix d'une étape unique et risque de questions répétées | Réutilisation des choix fournis et configuration de départ recommandée |
| Transformer un brief en cadrage utilisable | Dix sections, sources et incertitudes bien encadrées | Contradiction sur le bilan de préparation corrigée |
| Être aidé à arbitrer | Questions pertinentes ; options, conséquences et recommandation insuffisamment prescrites | Contrat d'aide à la décision applicable au cadrage et au fonctionnel |
| Répondre progressivement | Réponses partielles et compteurs persistants déjà disponibles | Ordre par impact, indication du point de départ, synthèse après réponse |
| Reprendre après interruption | Machine d'état utile ; report explicite difficile à distinguer dans le Canvas | Questions actives et reportées séparées, rapprochement avec le compteur |
| Valider en connaissance de cause | Approbation obligatoire, sans présentation de revue suffisamment précise | Lien vers le Canvas, changements, blocages et préparation des étapes suivantes |
| Poursuivre après le cadrage | Conception fonctionnelle disponible uniquement en appel direct | Prochaine action et prompt d'appel direct recommandés ; routage automatique toujours absent |
| Faire évoluer la conception | Identifiants stables, traçabilité et historique déjà présents | Revue fonctionnelle orientée dépendances et arbitrages, sans priorité de backlog inventée |
| Recevoir un vrai livrable Word | Le script acceptait un contenu quelconque nommé `.docx` | Contrôle du paquet OOXML avant clôture ; vérifications visuelle et métier toujours requises |
| Piloter le projet au quotidien | Pas de suivi d'engagements, budget, échéances ou avancement d'exécution | Évolution proposée, non implémentée |

## Défauts corrigés et preuves

| Priorité | Constat vérifiable | Correction |
| --- | --- | --- |
| Haute | `complete_document()` contrôlait seulement l'existence, l'emplacement et l'extension ; le test acceptait `b"PK test"` | Refus des fichiers vides, texte renommé, ZIP sans document, XML mal formé, corps absent et type de contenu incorrect ; état conservé après refus |
| Haute | `framing-structure.md` rendait facultatif dans la conversation le bilan que le skill exige dans le Canvas | Bloc non numéroté obligatoire dans le fichier enregistré, avec trois conclusions distinctes |
| Haute | Les questions reportées restaient des questions sans réponse, alors que la reprise demandait de reposer les questions sans réponse | Sous-parties courtes actives/reportées dans la section 9 ; seules les actives sont reprises et confrontées au compteur |
| Haute | Le rejeu a regroupé des arbitrages indépendants sous un seul compteur, rendant les réponses partielles ambiguës | Une décision indépendamment répondable par question comptée ; regroupement visuel autorisé sans fusion des compteurs |
| Moyenne | L'entrée demandait à nouveau consentement et étape, même lorsqu'ils étaient explicitement donnés | Réutilisation de l'autorisation et des choix correspondant au périmètre ; transitions toujours exécutées dans l'ordre |
| Moyenne | Les questions expliquaient leur intérêt sans exiger une aide réelle à l'arbitrage | Alternatives plausibles, conséquences, recommandation fondée ou limite explicite des preuves ; réponse libre possible |
| Moyenne | La clôture annonçait la fin du workflow sans organiser la suite concrète | Handoff fondé sur le Canvas, avec prompt vers une capacité réellement disponible |
| Moyenne | La spécification conservait des formulations obsolètes sur les statuts et contradictions visibles dans le Canvas | Alignement sur la position courante validée, questions concises et analyse conservée hors Canvas |

Les principales modifications runtime sont consultables dans le
[contrat d'interaction](../../plugins/project-design/skills/project-design/references/project-manager-interaction.md),
le [workflow](../../plugins/project-design/skills/project-design/scripts/workflow.py),
le [cadrage](../../plugins/project-design/skills/project-framing/SKILL.md)
et la [conception fonctionnelle](../../plugins/project-design/skills/functional-design/SKILL.md).

## Expérience attendue après correction

Le plugin doit pouvoir dire, en s'appuyant sur les sources du projet :

> Le Canvas est disponible. La décision sur le périmètre empêche de détailler
> les parcours. Voici les options documentées et leurs conséquences. Je
> recommande celle qui respecte la contrainte validée ; ce conseil reste à
> arbitrer. Commençons par cette question, puis traitons les autres points du lot.

Lorsque les sources ne permettent pas de recommander une option, il doit
expliquer ce qui manque. Après une réponse, il indique la modification apportée
et la décision suivante. Une demande de conseil ne vaut pas décision ; un
report ne rend pas un blocage résolu.

## Axes d'amélioration proposés

Ces évolutions sont proposées pour des itérations dédiées. Elles ne sont pas
présentées comme disponibles et ne modifient pas silencieusement la roadmap.

| Ordre recommandé | Évolution | Bénéfice concret | Critère d'acceptation |
| --- | --- | --- | --- |
| 1 | Router `functional-design` depuis le parcours guidé | Continuer à partir du Canvas validé sans devoir connaître le nom du skill | Transition refusée si le Canvas bloque le fonctionnel ; reprise de l'étape et des artefacts existants sans refaire l'intake |
| 2 | Permettre la révision contrôlée après approbation | Gérer un changement de périmètre ou une nouvelle décision après la phase `complete` | Révision identifiée, impacts sur les livrables listés, nouvelle approbation ciblée, ancienne validation conservée sans reset |
| 3 | Fiabiliser la reprise des arbitrages | Réduire la dépendance aux compteurs et à la rédaction du Canvas | Désaccord entre questions actives et état détecté ; correction guidée sans perte ni double comptage. Contrat de stockage à décider avant ajout d'identifiants ou d'un registre |
| 4 | Ajouter une vue de pilotage concise à la demande | Préparer une réunion projet avec décisions attendues, blocages et prochaines actions | Synthèse issue des artefacts, responsables et dates uniquement s'ils sont connus ; aucun second référentiel de vérité |
| 5 | Proposer un atelier adapté au besoin immédiat | Préparer un cadrage, un arbitrage de périmètre ou une revue fonctionnelle avec une durée donnée | Ordre du jour fondé sur les blocages, préparation utile avant questions, conclusion avec décisions acquises et actions restantes ; un atelier court ne masque pas les questions nécessaires |
| 6 | Étendre le pilotage aux engagements, délais et budget | Relier la conception aux contraintes de livraison | Responsabilité méthodologique définie avant implémentation ; distinction entre engagement, hypothèse et estimation ; aucune date ou estimation inventée |
| 7 | Livrer `document-functional-design`, puis les méthodologies manquantes selon la roadmap | Donner au chef de projet des supports partageables et une continuité jusqu'au backlog | Restitution fidèle au fonctionnel validé ; aucune priorité ni estimation créée par la mise en forme |

Je recommande de traiter d'abord la continuité cadrage → conception fonctionnelle
et les révisions après validation. Ces deux capacités aideront davantage le
chef de projet qu'une multiplication de formulaires ou de tableaux de bord.
La vue de pilotage pourra ensuite s'appuyer sur des artefacts et un cycle de
changement réellement maîtrisés.

## Validation et limites

Les preuves et le statut des contrôles figurent dans le
[compte rendu CI](../tests/executions/2026-09-05-project-manager-support-review.md).
Les consignes sont implémentées dans le dépôt ; leur efficacité conversationnelle
requiert une recette utilisateur. Les tests Python ne démontrent pas à eux seuls
la qualité des recommandations ni le confort de l'interface interactive.

Les cinq placeholders, les modèles métier partagés et les Golden Outputs sont
préservés. Aucun commit, push, publication ou remplacement du plugin installé
n'est réalisé dans cette intervention.
