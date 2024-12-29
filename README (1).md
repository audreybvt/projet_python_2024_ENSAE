# Projet Python 

*Par Maël Dieudonné et Guillaume Lévy, 2023.*

# Table des matières
1. [Définitions](#definitions)
2. [Objectifs](#objectifs)
3. [Sources des données](#sources)
4. [Présentation du dépôt](#pres)
5. [Licence](#licence)



## 1. Définitions <a name="definitions">

**Dette publique au sens de Maastricht :** 

La dette au sens de Maastricht, ou dette publique notifiée, couvre l'ensemble des administrations publiques au sens des comptes nationaux : l'État, les organismes divers d'administration centrale (ODAC), les administrations publiques locales et les administrations de sécurité sociale. 

(Source : https://www.insee.fr/fr/metadonnees/definition/c1091.)

**Indice de développement humain :**

Indice agrégé, moyenne géométrique de trois sous-indices relatifs respectivement à la santé, l'éducation et le revenu de la population. Compris entre 0 (exécrable) et 1 (excellent), les valeurs actuelles vont, en 2021, de 0,95+ (Europe du Nord) à 0,4- (certains pays d'Afrique), avec une médiane autour de 0,7.

## 2. Objectifs <a name="objectifs">

Si modeste cela soit-il, nous cherchons à déterminer l'influence de la dette publique sur le développement humain des États. Plus précisément, nous allons croiser des données de dette publique au sens de Maastricht avec des données d'IDH. La population de l'État et sa croissance seront convoquées comme variables explicatives annexes dans une seconde partie, dans l'espoir d'affiner les conclusions.

## 3. Sources des données <a name="sources">

Nous nous sommes reposés de façon essentielle sur les sources suivantes : 

- Wikipédia (pour une liste des codes ISO);
- le FMI (pour l'endettement);
- la Banque mondiale (pour la population);
- l'ONU (pour les données d'IDH).

Les données sont récupérées autant que possible en utilisant les API publiques des sources.

## 4. Présentation du dépôt <a name=pres>

Notre production est essentiellement localisée dans deux versions d'un fichier ```main.ipynb```.
- La première ne contient que le code non exécuté et les commentaires entre les cellules. 
- Le code dans la seconde a été préalablement exécuté, afin de pouvoir présenter les résultats même en cas  d'inaccessibilité temporaire des sources. 

C'est cette version exécutée qui tient lieu de rapport final.

Le dossier ```data``` contient une copie locale d'une partie des données tirées de nos sources. Les API  correspondantes ont été indisponibles pendant quelques jours durant le projet, ce qui nous a contraint à trouver une parade.

Le dossier ```scripts``` contient, comme on l'imagine, une multitude de fonctions utiles, afin de rendre notre code plus lisible et maintenanble. 

Quant au fichier ```requirements.txt```, il est appelé par pip afin d'installer les paquets nécessaires en début d'exécution.

## 5. Licence <a name="licence">

Ce projet est sous licence GPLv3.

