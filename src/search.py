import pandas as pd
import os
def search_inventory(file: str, column: str, query: str):
    """
    Recherche dans le fichier CSV une valeur spécifique dans une colonne donnée.
    """
    try:
        df = pd.read_csv(file)
        results = df[df[column].str.contains(query, case=False, na=False)]
        if not results.empty:
            print(results)
            return results
        else:
            print(f"Aucun résultat trouvé pour '{query}' dans la colonne '{column}'.")
            return None
    except FileNotFoundError:
        print("Fichier introuvable.")
        return "Fichier introuvable."
    except KeyError:
        print(f"Colonne '{column}' non trouvée dans le fichier.")
        return f"Colonne '{column}' non trouvée dans le fichier."
# Exemple d'utilisation
# search_inventory('inventaire_consolidé.csv', 'nom_du_produit', 'chaise')