# Documentation Technique : Migration MongoDB & Docker

## 1. Contexte du projet
Ce dépôt contient les scripts et la configuration nécessaires pour migrer les données médicales d'un client (format CSV) vers un environnement Big Data scalable horizontalement. La solution repose sur une base de données NoSQL (MongoDB) conteneurisée via Docker.

## 2. Logique de migration (ETL)
Le processus de migration est géré par le script Python `migrate.py`.
* **Extraction :** Lecture du fichier source `healthcare_dataset.csv` via la librairie Pandas.
* **Transformation et intégrité :** Nettoyage des chaînes de caractères (uniformisation de la casse pour éviter les doublons), vérification du typage, et conversion du DataFrame en dictionnaire BSON.
* **Chargement :** Purge de la collection cible (idempotence du script) et injection en lot (`insert_many`) dans MongoDB.

## 3. Modélisation : Schéma de la base de données
Bien que MongoDB soit "schema-less", la collection respecte une structure de document précise pour garantir la cohérence des données exploitées.

* **Base de données :** `hopital`
* **Collection :** `patients`
* **Structure d'un document type :**
```json
{
  "_id": {"$oid": "Identifiant_unique_genere"},
  "Patient_Name": "String",
  "Age": "Integer",
  "Gender": "String",
  "Blood_Type": "String",
  "Medical_Condition": "String",
  "Date_of_Admission": "Date (YYYY-MM-DD)",
  "Doctor": "String",
  "Hospital": "String",
  "Billing_Amount": "Float"
}
```

## 4. Sécurité, Authentification et Rôles
La base de données est sécurisée dès l'initialisation du conteneur. Aucun accès anonyme n'est permis.
* **Authentification :** L'accès root est protégé par des identifiants stricts gérés via un fichier `.env` (ignoré du dépôt public).
* **Rôle Administrateur (Root) :** L'utilisateur `admin` possède des droits d'administration globaux sur le cluster.
* **Rôle Applicatif (Data Worker) :** Via le script `init-mongo.js`, un rôle restreint `data_worker` est créé automatiquement. Le script Python l'utilise pour se connecter, limitant ses droits aux seules actions de lecture et d'écriture sur la base de données `hopital` (Principe du moindre privilège).

## 5. Guide de déploiement local
Pour exécuter ce projet localement :

1. Clonez ce dépôt et créez un fichier nommé `.env` à la racine du projet, en respectant ce modèle :
   ```env
   MONGO_ROOT_USER=votre_nom_utilisateur_admin
   MONGO_ROOT_PASSWORD=votre_mot_de_passe_fort
2. Placez le fichier source `healthcare_dataset.csv` à la racine du répertoire (ignoré du dépôt pour des raisons de confidentialité).
3. À la racine du projet, exécutez la commande d'orchestration :
   ```bash
   docker-compose up --build
   ```
4. MongoDB va s'initialiser, créer les rôles sécurisés, puis le script Python effectuera la migration. Les données sont persistées sur l'hôte grâce au volume Docker `mongo_data`.