# Les déterminants de la performance olympique : 

Projet Python pour l'économiste - 2A ENSAE - 2021-2022

Auteures : Clémence Briodeau, Natalie Esteve, Lucie Tissot

## Comment expliquer le nombre de médailles gagnées par un pays aux JO ?

## Introduction

**Objectif** : Nous avons souhaité étudier les facteurs socio-économiques déterminant les résultats des pays aux Jeux Olympiques. Nous nous sommes pour cela aidées de l'article de recherche suivant :

Blais-Morisset Paul, Boucher Vincent, Fortin Bernard, « L’impact des dépenses publiques consacrées au sport sur les médailles olympiques », Revue économique, 2017/4 (Vol. 68), p. 623-642. DOI : 10.3917/reco.684.0623. URL : https://www.cairn.info/revue-economique-2017-4-page-623.htm

Celui-ci a permis d'orienter notre travail en identifiant quatre variables explicatives du succès aux Jeux Olympiques d'un pays, mesuré en nombre de médailles obtenues : la taille de la population, le PIB/habitant, le montant des investissements dans le sport, et le fait que le pays soit hôte ou non des Jeux Olympiques. Nous avons également étudié l'influence de l'espérance de vie à la naissance. Notre objectif a donc été de mesurer l'importance de ces facteurs dans la performance olympique. Nous avons pour cela restreint notre étude aux Jeux Olympiques d'été de 1992 à 2020, soit 8 Jeux Olympiques. Le choix de débuter notre étude en 1992 provient du fait qu'il n'y a pas de données économiques individualisées pour les pays de l'ex-bloc soviétique avant 1992,

**Projet** : Tout d'abord, nous avons récupéré les données par webscrapping pour les résultats olympiques, sur le site de la banque mondiale pour les données de population, de PIB/habitant et d'espérance de vie à la naissance, et sur le site du FMI pour les données d'investissement dans le sport, et les avons nettoyées et fusionnées afin de les rendre exploitables. Nous avons ensuite effectué des statistiques descriptives et visualisé le lien entre chaque variable explicative et les résultats olympiques, chaque variable étant étudiée indépendamment des autres. Cette analyse descriptive et graphique nous a confirmé que quatre facteurs (taille de la population, PIB/habitant, investissements dans le sport, pays hôte) sur les cinq que nous voulions tester avaient un impact sur le nombre de médailles gagnées. Enfin, nous avons tenté de modéliser et mesurer précisément l'importance de ces déterminants dans les résultats olympiques grâce à une régression linéaire multiple prenant en compte l'ensemble des variables étudiées.


## Récapitulatif des notebooks :

**- Recuperation_donnees.ipynb** : récupération des données olympiques par webscrapping, récupération et nettoyage des données de la Banque Mondiale et du FMI (données sur l'investissement dans le sport, la population,le PIB/hab et l'espérance de vie), et fusion des données pour constituer la base de données de travail

**- Visualisation.ipynb** : visualisation du lien entre le nombre de médailles gagnées aux JO et les différentes variables explicatives

**- Modelisation.ipynb** : Régression linéaire multiple pour quantifier l'impact de chaque variable explicative sur les résultats aux JO

**Mode d'emploi :**
1) exécuter Recuperation_donnees
2) exécuter Visualisation
3) exécuter Modélisation

## Conclusion : 
Les résultats obtenus confirment une corrélation positive entre le nombre de médailles obtenues et la taille de la population, ainsi que le PIB/habitant. Concernant la variable "pays hôte", le fait de n'avoir étudié que 8 éditions limite l'interprétation du résultat, le coefficient est très probablement surestimé notamment car les pays qui ont accueilli les JO ces dernières années sont des pays qui habituellement gagnent beaucoup de médailles. En revanche, l'espérance de vie à la naissance n'a pas d'impact sur la performance olympique. Le peu de données dont nous disposons sur l'investissement dans le sport ne permet pas de quantifier son impact de manière précise, néanmoins le coefficient de corrélation positif entre l'investissement et le total des médailles nous montre que plus un pays a investi dans le sport, plus il est performant.

## Limites :
Nous n'avons pas trouvé suffisamment de données sur l'investissement dans le sport pour pouvoir déterminer précisément l'influence de la variable dans notre modèle, nous savons seulement que cet impact est positif. 
D'autre part, nous avons choisi de n'étudier que les pays qui avaient gagné au moins 1 médaille aux JO depuis 1992, et non tous les pays participants, car ils ne figuraient pas dans les tableaux que nous avons webscrappé. Nous avons estimé que cela ne biaiserait pas trop nos résultats étant donné qu'il y a un nombre très important de pays qui n'ont gagné qu'une seule médaille. L'objectif de notre projet étant d'étudier les déterminants permettant de gagner davantage de médailles et d'être plus performants, ce choix nous a paru pertinent.
Enfin, le choix de débuter notre étude en 1992 a facilité notre travail mais une autre piste aurait été de débuter plus tôt, en étudiant éventuellement séparément le bloc soviétique, afin d'avoir davantage de données sur lesquelles nous appuyer.



