# 🏢 RH Manager - Système de Gestion des Ressources Humaines

**RH Manager** est une application web full-stack développée avec **Django** (Python) pour le backend et **Bootstrap** pour une interface utilisateur fluide et responsive. Ce projet a été conçu pour simplifier la gestion administrative des employés au sein d'une organisation, notamment le suivi des fiches personnels et le traitement des demandes de congés.

---

## 🚀 Fonctionnalités Principales

### 👤 Espace Employé
* **Tableau de bord personnalisé :** Vue d'ensemble sur le profil de l'utilisateur connecté.
* **Suivi des soldes :** Affichage en temps réel du solde de congés restants.
* **Historique individuel :** Consultation transparente de ses propres demandes de congés et de leur statut (En attente, Approuvé, Rejeté).

### 👔 Espace RH & Administration
* **Gestion des dossiers :** Centralisation des informations des employés (Service, Poste, Date d'embauche).
* **Validation en un clic :** Interface dédiée permettant aux administrateurs et membres du personnel RH d'approuver ou de rejeter instantanément les demandes de congé en attente.
* **Filtrage de sécurité :** Isolation stricte des données pour s'assurer qu'un employé ne puisse ni modifier ni visualiser les requêtes de ses collègues.

---

## 🛠️ Technologies Utilisées

* **Backend :** Django 4.1 & Python 3.13
* **Base de données :** MySQL (gérée via phpMyAdmin)
* **Frontend :** HTML5, CSS3, Vanilla Django Template Language (DTL)
* **Framework CSS :** Bootstrap 5

---

## 📂 Architecture de la Base de Données

Le système repose sur une structure relationnelle propre modélisant les entités clés de l'organisation :

* **`Employe` :** Étend le modèle utilisateur natif de Django (`User`) en y associant un service, un poste et une date d'embauche.
* **`Conge` :** Gère le cycle de vie d'une demande (Date de début, Date de fin, Motif, Statut). Les statuts disponibles incluent :
  * `en_attente` (par défaut)
  * `approuve`
  * `rejete`

---

## 💻 Installation et Configuration Locale

Suivez ces étapes pour cloner et exécuter le projet sur votre machine :

### 1. Prérequis
Assurez-vous d'avoir installé **Python 3.13** et un serveur MySQL local (comme **XAMPP** ou **WampServer** pour accéder à phpMyAdmin).

### 2. Cloner le dépôt
```bash
git clone [https://github.com/votre-compte/rh_project.git](https://github.com/votre-compte/rh_project.git)
cd rh_project

Projet Django:
FATY SOW
CCP DAW ISEP DIAMNIADIO
