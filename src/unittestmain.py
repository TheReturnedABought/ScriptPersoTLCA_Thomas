import unittest
import pandas as pd
import os
from io import StringIO
from search import search_inventory
from report import generate_report
from consolidate import consolidate_csv

class TestSearchInventory(unittest.TestCase):
    def setUp(self):
        # Mock CSV content
        self.csv_content = """nom_du_produit,quantite,prix
chaise,10,25.5
table,5,75.0
armoire,2,150.0
"""
        # Create a temporary file for testing
        self.test_file = "test_inventory.csv"
        with open(self.test_file, "w") as f:
            f.write(self.csv_content)

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_valid_query(self):
        # Test a valid query
        result = search_inventory(self.test_file, "nom_du_produit", "chaise")
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["nom_du_produit"], "chaise")

    def test_no_results(self):
        # Test a query with no results
        result = search_inventory(self.test_file, "nom_du_produit", "canape")
        self.assertIsNone(result)

    def test_invalid_column(self):
        # Test a query with an invalid column
        result = search_inventory(self.test_file, "couleur", "rouge")
        self.assertEqual(result, "Colonne 'couleur' non trouvée dans le fichier.")

    def test_file_not_found(self):
        # Test with a non-existent file
        result = search_inventory("fichier_inexistant.csv", "nom_du_produit", "chaise")
        self.assertEqual(result, "Fichier introuvable.")

class TestGenerateReport(unittest.TestCase):
    def setUp(self):
        # Mock CSV content
        self.csv_content = """nom_du_produit,quantite,prix
chaise,10,25.5
table,5,75.0
armoire,2,150.0
"""
        # Create a temporary file for testing
        self.test_file = "test_inventory.csv"
        self.output_file = "test_report.csv"
        with open(self.test_file, "w") as f:
            f.write(self.csv_content)

    def tearDown(self):
        # Remove temporary files after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_report_success(self):
        # Test generating a report successfully
        result = generate_report(self.test_file, self.output_file)
        self.assertEqual(result, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

    def test_generate_report_file_not_found(self):
        # Test generating a report with a non-existent file
        result = generate_report("fichier_inexistant.csv", self.output_file)
        self.assertEqual(result, "Fichier introuvable.")
class TestConsolidateCSV(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and files for testing
        self.test_dir = "test_csv_dir"
        self.output_file = "consolidated.csv"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create sample CSV files
        self.file1_content = "id,name,age\n1,Alice,30\n2,Bob,25\n"
        self.file2_content = "id,name,age\n3,Charlie,35\n4,David,40\n"
        self.file3_empty = ""

        with open(os.path.join(self.test_dir, "file1.csv"), "w") as f1, \
             open(os.path.join(self.test_dir, "file2.csv"), "w") as f2, \
             open(os.path.join(self.test_dir, "file3.csv"), "w") as f3:
            f1.write(self.file1_content)
            f2.write(self.file2_content)
            f3.write(self.file3_empty)

    def tearDown(self):
        # Remove temporary files and directory after tests
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_consolidate_csv_success(self):
        # Test successful consolidation
        consolidate_csv(self.test_dir, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        consolidated_df = pd.read_csv(self.output_file)
        self.assertEqual(len(consolidated_df), 4)  # 4 rows from file1 and file2
        self.assertEqual(consolidated_df.iloc[0]["name"], "Alice")
        self.assertEqual(consolidated_df.iloc[3]["name"], "David")

    def test_consolidate_csv_empty_files(self):
        # Test handling of empty files
        os.remove(os.path.join(self.test_dir, "file2.csv"))  # Leave only file1 and file3
        consolidate_csv(self.test_dir, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        consolidated_df = pd.read_csv(self.output_file)
        self.assertEqual(len(consolidated_df), 2)  # Only file1 contributes rows

    def test_consolidate_csv_no_csv_files(self):
        # Test with no CSV files in directory
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        consolidate_csv(self.test_dir, self.output_file)
        self.assertFalse(os.path.exists(self.output_file))  # Output file should not be created

if __name__ == "__main__":
    unittest.main()
