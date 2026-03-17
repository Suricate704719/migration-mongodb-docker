# 🏥 Projet de Migration de Données de Santé (ETL)

## 🎯 Objectif du Projet
Ce projet est un pipeline ETL (Extract, Transform, Load) conteneurisé. Son but est d'extraire des données médicales brutes depuis un fichier CSV, de les nettoyer et de les transformer via Python (Pandas), puis de les charger dans une base de données NoSQL (MongoDB) pour faciliter leur exploitation.

## 🛠️ Architecture et Technologies
* **Langage :** Python 3.11
* **Bibliothèques :** Pandas (Transformation), PyMongo (Connexion base de données)
* **Base de données :** MongoDB (NoSQL Orienté Document)
* **Infrastructure :** Docker & Docker Compose (Conteneurisation)
* **Gestion de versions :** Git & GitHub

## 📂 Structure du Dépôt
* `migrate.py` : Le script d'extraction, transformation et chargement (ETL).
* `Dockerfile` : Le plan de construction de l'environnement Python.
* `docker-compose.yml` : Le chef d'orchestre qui relie Python et MongoDB.
* `requirements.txt` : Les dépendances Python à installer.
* `.gitignore` : Sécurise le dépôt en ignorant les données sensibles.

## 🔒 Note sur la confidentialité (RGPD)
Afin de respecter la confidentialité des données et les normes RGPD, le fichier source `healthcare_dataset.csv` a été volontairement ignoré via le fichier `.gitignore` et n'est pas présent sur ce dépôt public. 

## 🚀 Comment lancer le projet en local ?

### Prérequis
1. Avoir **Docker Desktop** installé (et WSL 2 activé si vous êtes sous Windows).
2. Avoir téléchargé le jeu de données source.

### Instructions pas-à-pas
1. Clonez ce dépôt sur votre machine locale :
   `git clone [URL_DE_TON_DEPOT_GITHUB]`
2. Placez le fichier `healthcare_dataset.csv` à la racine du dossier du projet.
3. Ouvrez un terminal dans ce dossier et lancez la commande suivante :
   `docker-compose up --build`
4. Le script va s'exécuter automatiquement. Vous pouvez vérifier l'importation des données en vous connectant à `localhost:27017` via MongoDB Compass. Les données seront persistées localement grâce à un volume Docker.