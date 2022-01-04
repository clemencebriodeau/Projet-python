# Les déterminants de la performance olympique : 

Projet Python pour l'économiste - 2A ENSAE - 2021-2022

Auteures : Clémence Briodeau, Natalie Esteve, Lucie Tissot

## Comment expliquer le nombre de médailles gagnées par un pays aux JO ?

##Introduction

**Objectif** : Nous avons souhaité étudier les facteurs socio-économiques déterminant les résultats des pays aux Jeux Olympiques. Nous nous sommes pour cela aidées de l'article de recherche suivant :

Blais-Morisset Paul, Boucher Vincent, Fortin Bernard, « L’impact des dépenses publiques consacrées au sport sur les médailles olympiques », Revue économique, 2017/4 (Vol. 68), p. 623-642. DOI : 10.3917/reco.684.0623. URL : https://www.cairn.info/revue-economique-2017-4-page-623.htm

Celui-ci a permis d'orienter notre travail en identifiant quatre variables explicatives du succès aux Jeux Olympiques d'un pays, mesuré en nombre de médailles obtenues : la taille de la population, le PIB/habitant, le montant des investissements dans le sport, et le fait que le pays soit hôte ou non des Jeux Olympiques. Notre objectif a donc été de mesurer l'importance de ces facteurs dans la performance olympique. Nous avons pour cela restreint notre étude aux Jeux Olympiques d'été de 1992 à 2020, soit 8 Jeux Olympiques. Le choix de débuter notre étude en 1992 provient du fait qu'il n'y a pas de données économiques individualisées pour les pays de l'ex-bloc soviétique avant 1992,

**Projet** : Tout d'abord, nous avons récupéré les données par webscrapping pour les résultats olympiques, sur le site de la banque mondiale pour les données de population et de PIB/habitant, et sur le site du FMI pour les données d'investissement dans le sport, et les avons nettoyées et fusionnées afin de les rendre exploitables. Nous avons ensuite effectué des statistiques descriptives et visualisé le lien entre chaque variable explicative et les résultats olympiques, chaque variable étant étudiée indépendamment des autres. Cette analyse descriptive et graphique nous a confirmé que chacun des quatre facteurs que nous voulions tester avait un impact sur le nombre de médailles gagnées. Enfin, nous avons tenté de modéliser et mesurer précisément l'importance de ces déterminants dans les résultats olympiques grâce à une régression linéaire multiple prenant en compte l'ensemble des variables étudiées.



##Récapitulatif des notebooks :

**- webscrapping_medailles.ipynb** : récupération des données sur les résultats olympiques depuis 1992 par webscrapping
**- Recuperation_donnees.ipynb** : récupération et nettoyage des données de la Banque Mondiale et du FMI (données sur l'investissement dans le sport, la population, et le PIB/hab)
**- Fusion_donnees.ipynb** : fusion de toutes les bases de données pour créer notre base de données de travail
**- Visualisation.ipynb** : visualisation du lien entre le nombre de médailles gagnées aux JO et les différentes variables explicatives
**- Modelisation.ipynb** : Régression linéaire multiple pour quantifier l'impact de chaque variable explicative sur les résultats aux JO

**Mode d'emploi : **
Ouvrir d'abord le notebook Visualisation puis le notebook Modélisation.

