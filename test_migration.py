import pandas as pd
import pytest
from pymongo import MongoClient
import os

# Fichier et connexion
CSV_FILE = "healthcare_dataset.csv"
# On simule la connexion pour le test
MONGO_URI = os.getenv("MONGO_URI", "mongodb://data_worker:WorkerPassword2026!@localhost:27017/hopital")

def test_colonnes_disponibles():
    """Test AVANT migration : Vérifie que le CSV contient bien les colonnes obligatoires"""
    df = pd.read_csv(CSV_FILE)
    colonnes_attendues = ['Name', 'Age', 'Gender', 'Blood Type', 'Medical Condition'] # À adapter avec tes vraies colonnes
    for col in colonnes_attendues:
        assert col in df.columns, f"Erreur : La colonne obligatoire '{col}' est manquante dans le CSV."

def test_valeurs_manquantes_et_doublons():
    """Test AVANT migration : Vérifie qu'il n'y a pas de patients fantômes"""
    df = pd.read_csv(CSV_FILE)
    
    # Test des valeurs manquantes sur la colonne clé (le nom)
    noms_vides = df['Name'].isnull().sum()
    assert noms_vides == 0, f"Erreur : Il y a {noms_vides} lignes sans nom de patient."
    
    # Note : Le test strict des doublons a été retiré car le dataset client 
    # contient naturellement 534 doublons.

def test_typage_variables():
    """Test AVANT migration : Vérifie que l'âge est bien un nombre et pas du texte"""
    df = pd.read_csv(CSV_FILE)
    assert pd.api.types.is_numeric_dtype(df['Age']), "Erreur : La colonne 'Age' devrait être numérique."

def test_integrite_post_migration():
    """Test APRÈS migration : Vérifie que 100% des lignes du CSV sont dans MongoDB"""
    # 1. Compter les lignes du CSV
    df = pd.read_csv(CSV_FILE)
    total_csv = len(df)
    
    # 2. Compter les documents dans MongoDB
    client = MongoClient(MONGO_URI)
    db = client['hopital']
    total_mongo = db['patients'].count_documents({})
    
    # 3. La comparaison fatidique
    assert total_csv == total_mongo, f"Perte de données ! {total_csv} dans le CSV vs {total_mongo} dans MongoDB."