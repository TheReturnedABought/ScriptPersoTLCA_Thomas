Aperçu du projet

Ce projet fournit trois scripts Python pour gérer et analyser les fichiers CSV :

search.py : Recherche des valeurs spécifiques dans une colonne d'un fichier CSV.

report.py : Génère un rapport de synthèse statistique pour un fichier CSV.

consolidate.py : Consolide plusieurs fichiers CSV d'un répertoire en un seul fichier CSV.

Chaque script est accompagné de tests unitaires permettant de valider ses fonctionnalités.

Installation de l'application

Prérequis

Python 3.7+

bibliothèque pandas

Etapes

Clonez ce dépôt :

git clone <repository-url>
cd <référentiel-répertoire>

Installez les dépendances nécessaires :

pip install pandas

Assurez-vous que les scripts et les fichiers de test sont dans le même répertoire.

Utilisation

0. main.py
Pour exécuter le script, faites un clic droit sur le fichier et cliquez sur run dans la ligne de commande, puis tapez python ./src/main.py et cliquez sur enter. vous aurez accès à différentes options. 

1. search.py

Description de l'application

Recherche dans un fichier CSV les lignes correspondant à une requête spécifique dans une colonne donnée.

Fonction

search_inventory(file : str, column : str, query : str)

file : Chemin d'accès au fichier CSV.

column : Nom de la colonne dans laquelle effectuer la recherche.

query : Chaîne de requête à rechercher.

Exemple en code :

search_inventory('exemple.csv', 'nom', 'chaise')


2. report.py

Description de l'application

Génère un rapport de synthèse pour les données d'un fichier CSV.

Fonction

generate_report(file : str, output_file : str)

file : Chemin d'accès au fichier CSV d'entrée.

fichier_de_sortie : Chemin d'accès pour enregistrer le rapport généré.

Exemple en code :

generate_report('example.csv', 'summary.csv')


3. consolider.py

Description de l'application

Combine tous les fichiers CSV d'un répertoire spécifié en un seul fichier CSV.


Fonction

consolidate_csv(test_dir : str, consolidated_file : str)

test_dir : Chemin d'accès au répertoire contenant les fichiers CSV.

fichier_consolidé : Chemin d'accès pour enregistrer le fichier consolidé.


Exemple en code :

consolidate_csv('csv_folder', 'consolidated.csv')



