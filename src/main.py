from search import search_inventory
from report import generate_report
from consolidate import consolidate_csv

def main():
    print("Système de gestion d'inventaire automatisé")
    print("Veuillez choisir une action à effectuer :")
    print("1. Consolidate CSV files")
    print("2. Search inventory")
    print("3. Generate report")

    action_choice = input("Entrez le numéro de l'action que vous souhaitez effectuer (1, 2, ou 3) : ").strip()

    if action_choice == "1":
        input_path = input("Entrez le chemin du fichier ou du répertoire d'entrée : ").strip()
        output_path = input("Entrez le chemin du fichier de sortie : ").strip()
        consolidate_csv(input_path, output_path)
    elif action_choice == "2":
        input_path = input("Entrez le chemin du fichier d'entrée : ").strip()
        column = input("Entrez la colonne à rechercher : ").strip()
        query = input("Entrez la valeur à rechercher : ").strip()
        search_inventory(input_path, column, query)
    elif action_choice == "3":
        input_path = input("Entrez le chemin du fichier d'entrée : ").strip()
        output_path = input("Entrez le chemin du fichier de sortie : ").strip()
        generate_report(input_path, output_path)
    else:
        print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
