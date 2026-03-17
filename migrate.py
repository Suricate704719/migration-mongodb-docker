import pandas as pd
from pymongo import MongoClient
import sys

def nettoyer_et_preparer_donnees(fichier_csv):
    print("1. Lecture et nettoyage du fichier CSV...")
    try:
        # Lire le fichier CSV
        df = pd.read_csv(fichier_csv)
        
        # Nettoyage : On met de l'ordre dans la colonne Name (ex: "Bobby JacksOn" -> "Bobby Jackson")
        df['Name'] = df['Name'].str.title()
        
        # Transformation : MongoDB ne lit pas les tableaux, il lit des dictionnaires. 
        # On convertit notre DataFrame en une liste de petits dictionnaires (1 ligne = 1 patient).
        documents = df.to_dict(orient='records')
        print(f"   -> Succès : {len(documents)} dossiers patients prêts pour l'import.")
        return documents
    
    except Exception as e:
        print(f"Erreur lors de la préparation des données : {e}")
        sys.exit(1)

def migrer_vers_mongodb(donnees):
    print("2. Connexion à la base de données MongoDB locale...")
    try:
        # Connexion à ton moteur mongod.exe qui tourne en arrière-plan
        client = MongoClient("mongodb://admin:HopitalPassword2026!@mongodb:27017/")
        
        # On crée une base de données nommée "hopital" et une collection "patients"
        db = client['hopital']
        collection = db['patients']
        
        # Par sécurité, on vide la collection avant d'importer pour éviter les doublons si on relance le script
        collection.delete_many({})
        
        print("3. Injection des données en cours...")
        collection.insert_many(donnees)
        print("   -> MIGRATION TERMINÉE AVEC SUCCÈS !")
        
    except Exception as e:
        print(f"Erreur de connexion ou d'insertion MongoDB : {e}")

# Lancement du script
if __name__ == "__main__":
    fichier_source = "healthcare_dataset.csv"
    donnees_propres = nettoyer_et_preparer_donnees(fichier_source)
    migrer_vers_mongodb(donnees_propres)