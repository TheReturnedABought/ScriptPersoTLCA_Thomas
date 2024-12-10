import argparse

def main():
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire automatisé")
    parser.add_argument("action", choices=["consolidate", "search", "report"], help="Action à effectuer")
    parser.add_argument("--input", help="Fichier ou répertoire d'entrée")
    parser.add_argument("--output", help="Fichier de sortie")
    parser.add_argument("--column", help="Colonne pour la recherche")
    parser.add_argument("--query", help="Valeur à rechercher")
    args = parser.parse_args()

    if args.action == "consolidate" and args.input and args.output:
        consolidate_csv(args.input, args.output)
    elif args.action == "search" and args.input and args.column and args.query:
        search_inventory(args.input, args.column, args.query)
    elif args.action == "report" and args.input and args.output:
        generate_report(args.input, args.output)
    else:
        print("Arguments invalides. Veuillez consulter l'aide avec --help.")

def generate_report(file: str, output_file: str):
    """
    Génère un rapport récapitulatif exportable à partir d'un fichier CSV.
    """
    try:
        df = pd.read_csv(file)
        report = df.describe(include='all')  # Récapitulatif des statistiques
        report.to_csv(output_file)
        print(f"Rapport généré dans : {output_file}")
    except FileNotFoundError:
        print("Fichier introuvable.")

# Exemple d'utilisation
# generate_report('inventaire_consolidé.csv', 'rapport_statistiques.csv')

def search_inventory(file: str, column: str, query: str):
    """
    Recherche dans le fichier CSV une valeur spécifique dans une colonne donnée.
    """
    try:
        df = pd.read_csv(file)
        results = df[df[column].str.contains(query, case=False, na=False)]
        if not results.empty:
            print(results)
        else:
            print(f"Aucun résultat trouvé pour '{query}' dans la colonne '{column}'.")
    except FileNotFoundError:
        print("Fichier introuvable.")
    except KeyError:
        print(f"Colonne '{column}' non trouvée dans le fichier.")

# Exemple d'utilisation
# search_inventory('inventaire_consolidé.csv', 'nom_du_produit', 'chaise')

import pandas as pd
import os

def consolidate_csv(directory: str, output_file: str):
    """
    Combine tous les fichiers CSV d'un répertoire donné en un seul fichier CSV.
    """
    all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]
    if not all_files:
        print("Aucun fichier CSV trouvé dans le répertoire.")
        return

    df_list = [pd.read_csv(file) for file in all_files]
    consolidated_df = pd.concat(df_list, ignore_index=True)
    consolidated_df.to_csv(output_file, index=False)
    print(f"Fichiers consolidés dans : {output_file}")

# Exemple d'utilisation
# consolidate_csv('chemin/vers/dossier_csv', 'inventaire_consolidé.csv')

if __name__ == "__main__":
    main()
