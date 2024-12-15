Aperçu des scripts
Ce projet se compose de trois scripts Python principaux qui fournissent différentes fonctionnalités pour traiter les fichiers CSV :

search.py :

Objectif : recherche d'une requête spécifique dans une colonne donnée d'un fichier CSV.
Fonction clé : search_inventory(file : str, column : str, query : str)
Prend en entrée le chemin d'accès au fichier, le nom de la colonne et la requête de recherche.
Elle produit les lignes qui correspondent à la requête ou un message d'erreur si elles n'ont pas été trouvées.

report.py :

Objet : Génère un rapport statistique à partir d'un fichier CSV.
Fonction clé : generate_report(file : str, output_file : str)
Lit le fichier d'entrée et crée un rapport enregistré dans le fichier de sortie.
Inclut des descriptions statistiques de toutes les colonnes.

consolidate.py :

Objectif : consolider plusieurs fichiers CSV d'un répertoire en un seul fichier CSV.
Fonction clé : consolidate_csv(test_dir : str, consolidated_file : str)
Combine tous les fichiers CSV non vides dans le répertoire spécifié.
Enregistre le résultat consolidé dans le fichier consolidé.

Traduit avec DeepL.com (version gratuite)
