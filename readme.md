# Entretien Technique

## Instructions

Le but de l'exercice est de simuler une situation réelle dans la journée d'un développeur Amarena.
Toutes les sources d'informations sont autorisées, que ce soit les documentations, Google, ou tout simplement
les personnes de l'entretien.

Un fichier `requirements.txt` est disponible contenant tout les paquets nécessaires à l'entretien. N'hésitez-pas à créer
un virtualenv (`python3 -m venv .venv` et `.venv/bin/activate`) pour être plus serein.


## Contexte

La bibliothèque municipale de Château-sur-Mer a besoin d'un logiciel afin de connaître les livres qu'elle possède et si
ils sont empruntés par des lecteurs. Ce logiciel est utilisé par la bibliothécaire qui s'occupe d'enregistrer les
changements d'état des livres.

Les développeurs déjà présent sur le projet ont décidés de construire une API interne permettant d'effectuer les
manipulations classiques sur les modèles : Create, Read, Update, Delete.
Vous rejoignez le projet avec un ensemble de User Stories à réaliser.

### Etat actuel des fonctionnalités :

Une première ébauche de la plateforme existe en Django. Elle utilise SQLite comme base de donnée et a déjà un certain
nombre de modèles implémentés.

* Book model
    * Title
    * Author
    * Genre
    * ISBN
    * Release date
* User model
    * First Name
    * Last Name
    * Inscription date
    * Blocked
* Author model
    * First Name
    * Last Name
    * Birth date

## Règles Business

* Il n'existe qu'un seul et unique livre pour une référence donnée dans la bibliothèque.
* La lectrice ne peut emprunter qu'un livre à la fois.
* La lectrice doit rendre le livre avant la date limite.
* La lectrice doit payer une amende si elle rend le livre après la date limite.
* L'amende est calculée comme suit : 3,00€ si le livre est ramené une semaine après, 0,50€ de plus pour chaque jour après
  cette première semaine. Un jour commencé est un jour dû.
    * Example : la lectrice ramène un livre trois jours en retard, elle paye 3,00€
    * Example : la lectrice ramène un livre huit jours en retard, elle paye 3,00+0,50=3,50€

## User Stories

### User Stories I : Emprunter un livre

> En tant que bibliothécaire, je souhaite pouvoir enregistrer l'emprunt d'un livre par un utilisateur si ce dernier n'a
> pas de livre déjà emprunté. Si il a déjà un livre emprunté, je veux savoir de quel livre il s'agit et la date de
> retour
> afin de lui communiquer ces informations.

### User Stories II : Ramener un livre

> En tant que bibliothécaire, je souhaite pouvoir enregistrer le retour d'un livre par un utilisateur. Si ce dernier ne
> l'a pas rendu dans les temps, je souhaite connaître le montant de l'amende à faire payer.

### User Stories III : Récupérer la liste des utilisateurs qui ont dépassés la limite

> En tant que bibliothécaire, je souhaite pouvoir avoir la liste des lecteurs, leurs coordonnées, les livres qu'ils ont
> empruntés et leurs amendes afin de pouvoir les contacter.

### User Stories IV : Soumettre un livre

> En tant que lecteur, je souhaite pouvoir soumettre des références de livres à la bibliothèque afin qu'ils puissent les
> acheter.


