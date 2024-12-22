from search import search_inventory
from report import generate_report
from consolidate import consolidate_csv
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

if __name__ == "__main__":
    main()
