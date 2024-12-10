import pandas as pd
import os
def generate_report(file: str, output_file: str):
    """
    Génère un rapport récapitulatif exportable à partir d'un fichier CSV.
    """
    try:
        df = pd.read_csv(file)
        report = df.describe(include='all')  # Récapitulatif des statistiques
        report.to_csv(output_file)
        print(f"Rapport généré dans : {output_file}")
        return output_file
    except FileNotFoundError:
        print("Fichier introuvable.")
        return "Fichier introuvable."
# Exemple d'utilisation
# generate_report('inventaire_consolidé.csv', 'rapport_statistiques.csv')