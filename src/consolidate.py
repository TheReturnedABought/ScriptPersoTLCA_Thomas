import pandas as pd
import os

def consolidate_csv(test_dir, consolidated_file):
    """
    Consolidates multiple CSV files in a directory into a single CSV file.

    Parameters:
    - test_dir (str): The directory containing CSV files.
    - consolidated_file (str): The path for the output consolidated CSV file.

    Returns:
    - str: A message indicating success or the encountered issue.
    """
    if not os.path.isdir(test_dir):
        print("Error: The specified directory does not exist. Please enter a valid directory.")
        return 1

    all_files = [f for f in os.listdir(test_dir) if f.endswith('.csv')]
    if not all_files:
        print("Error: No CSV files found in the specified directory.")
        return 1
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
            return 1
        except Exception as e:
            print(f"Error reading {file}: {e}")
            return 1

    if df_list:
        consolidated_df = pd.concat(df_list, ignore_index=True)
        consolidated_df.to_csv(consolidated_file, index=False)
        print(f"Success: Consolidated CSV saved to {consolidated_file}.")
        return 0
    else:
        print("Error: No valid data to consolidate. All files are empty or unreadable.")
        return 1
