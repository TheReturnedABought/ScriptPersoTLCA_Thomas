Ce projet fournit un système automatisé de gestion d'inventaire permettant de consolider des fichiers CSV, de rechercher des enregistrements d'inventaire et de générer des rapports statistiques. Toutes les fonctionnalités sont accessibles via une interface de ligne de commande.

Ce programme consolide plusieurs fichiers CSV en un seul fichier, recherche les données d'inventaire sur la base de colonnes et de requêtes spécifiées, génère des rapports statistiques au format CSV et fournit une interface de ligne de commande simple et efficace pour des opérations rapides.

Pour l'installer, clonez d'abord ce dépôt en exécutant :

git clone (https://github.com/TheReturnedABought/ScriptPersoTLCA_Thomas)
cd <répertoire_du_référentiel>

Ensuite, installez les dépendances à l'aide de pip :

pip install pandas



Pour consolider les fichiers, utilisez la commande suivante :

python main.py consolidate --input <chemin_du_répertoire> --output <fichier_de_sortie>.

Par exemple :

python main.py consolidate --input ./data --output consolidated_inventory.csv


Pour effectuer une recherche dans l'inventaire, utilisez la commande suivante :

python main.py search --input <file_path> --column <column_name> --query <search_query>

Par exemple :

python main.py search --input consolidated_inventory.csv --column nom_du_produit --query chaise



Pour générer un rapport, utilisez la commande suivante :

python main.py report --input <file_path> --output <report_file>

Par exemple :

python main.py report --input consolidated_inventory.csv --output inventory_report.csv



Pour valider les fonctionnalités, exécutez les tests unitaires :

python -m unittest unittestmain.py
