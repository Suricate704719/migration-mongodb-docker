# 🏥 Migration de Données Médicales vers MongoDB (Projet DataSoluTech)

## 🎯 Contexte de la Mission
Ce projet a été réalisé pour le compte de DataSoluTech afin de répondre aux problèmes de scalabilité d'un client du secteur médical. L'objectif est de migrer des données patients depuis un fichier plat (CSV) vers une base de données NoSQL (MongoDB), tout en conteneurisant l'environnement avec Docker pour garantir la portabilité, la sécurité et la scalabilité de l'infrastructure.

## ⚙️ Logique de Migration et Tests d'Intégrité
Le transfert des données est automatisé par le script Python `migrate.py` (processus ETL) :

1. **Extraction :** Lecture sécurisée du dataset `healthcare_dataset.csv` à l'aide de la librairie Pandas.
2. **Transformation et Tests d'intégrité :**
   Avant l'insertion, le script s'assure de la qualité de la donnée :
   - Vérification du typage des colonnes (ex: s'assurer que l'âge est un entier, le montant facturé un décimal).
   - Nettoyage des chaînes de caractères pour éviter les incohérences.
   - Gestion et audit des valeurs manquantes ou des potentiels doublons.
   - Conversion du tableau en liste de dictionnaires (format BSON compatible MongoDB).
3. **Chargement :** Connexion à l'instance MongoDB et exécution de la commande `insert_many` pour une insertion en lot optimisée.

## 🗂️ Schéma de la Base de Données
Bien que MongoDB soit "schema-less" (sans schéma rigide), nous avons défini une structure de document claire pour maintenir la cohérence des données médicales.

* **Base de données :** `medical_db`
* **Collection :** `patients`
* **Exemple d'un Document type (Format JSON) :**

```json
{
  "_id": {"$oid": "64b8f..."},
  "Patient_Name": "Jean Dupont",
  "Age": 45,
  "Gender": "Male",
  "Blood_Type": "O+",
  "Medical_Condition": "Diabetes",
  "Date_of_Admission": "2023-10-12",
  "Doctor": "Dr. Smith",
  "Hospital": "Hopital Necker",
  "Billing_Amount": 1250.50
}