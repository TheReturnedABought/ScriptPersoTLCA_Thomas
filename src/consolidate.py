import pandas as pd
import os

def consolidate_csv(test_dir, consolidated_file):
    """
    Consolidates multiple CSV files in a directory into a single CSV file.
    """
    all_files = [f for f in os.listdir(test_dir) if f.endswith('.csv')]
    df_list = []

    for file in all_files:
        file_path = os.path.join(test_dir, file)
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                df_list.append(df)
            else:
                print(f"Warning: {file} is empty.")
        except pd.errors.EmptyDataError:
            print(f"Error: {file} is empty or not readable.")

    if df_list:
        consolidated_df = pd.concat(df_list, ignore_index=True)
        consolidated_df.to_csv(consolidated_file, index=False)
# Exemple d'utilisation
# consolidate_csv('chemin/vers/dossier_csv', 'inventaire_consolidé.csv')