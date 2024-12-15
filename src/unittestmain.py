import unittest
import os
import pandas as pd
from search import search_inventory
from report import generate_report
from consolidate import consolidate_csv

class TestSearch(unittest.TestCase):
    def setUp(self):
        # Create a test CSV file
        self.test_file = "test_search.csv"
        self.test_data = pd.DataFrame({
            "name": ["chair", "table", "lamp"],
            "price": [50, 150, 30]
        })
        self.test_data.to_csv(self.test_file, index=False)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_search_valid(self):
        result = search_inventory(self.test_file, "name", "chair")
        self.assertEqual(result, 1)

    def test_search_no_match(self):
        result = search_inventory(self.test_file, "name", "sofa")
        self.assertIsNone(result)

    def test_search_invalid_column(self):
        result = search_inventory(self.test_file, "nonexistent_column", "chair")
        self.assertEqual(result, 0)

    def test_search_file_not_found(self):
        result = search_inventory("missing_file.csv", "name", "chair")
        self.assertEqual(result, 0)


class TestReport(unittest.TestCase):
    def setUp(self):
        # Create a test CSV file
        self.test_file = "test_report.csv"
        self.test_output = "test_output.csv"
        self.test_data = pd.DataFrame({
            "name": ["chair", "table", "lamp"],
            "price": [50, 150, 30]
        })
        self.test_data.to_csv(self.test_file, index=False)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_generate_report_valid(self):
        result = generate_report(self.test_file, self.test_output)
        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(self.test_output))

    def test_generate_report_file_not_found(self):
        result = generate_report("missing_file.csv", self.test_output)
        self.assertEqual(result, 0)


class TestConsolidate(unittest.TestCase):
    def setUp(self):
        # Create a test directory with CSV files
        self.test_dir = "test_dir"
        self.consolidated_file = "consolidated.csv"
        os.makedirs(self.test_dir, exist_ok=True)

        self.file1 = os.path.join(self.test_dir, "file1.csv")
        self.file2 = os.path.join(self.test_dir, "file2.csv")

        pd.DataFrame({"name": ["chair"], "price": [50]}).to_csv(self.file1, index=False)
        pd.DataFrame({"name": ["table"], "price": [150]}).to_csv(self.file2, index=False)

    def tearDown(self):
        if os.path.exists(self.consolidated_file):
            os.remove(self.consolidated_file)
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_consolidate_valid(self):
        result = consolidate_csv(self.test_dir, self.consolidated_file)
        self.assertEqual(result, 0)
        self.assertTrue(os.path.exists(self.consolidated_file))

    def test_consolidate_no_csv_files(self):
        # Clear the directory
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        result = consolidate_csv(self.test_dir, self.consolidated_file)
        self.assertEqual(result, 1)

    def test_consolidate_directory_not_found(self):
        result = consolidate_csv("nonexistent_dir", self.consolidated_file)
        self.assertEqual(result, 1)

    def test_consolidate_empty_file(self):
        empty_file = os.path.join(self.test_dir, "empty.csv")
        pd.DataFrame().to_csv(empty_file, index=False)  # Create an empty CSV file
        result = consolidate_csv(self.test_dir, self.consolidated_file)
        self.assertEqual(result, 1)  # Consolidation should still work

    def test_consolidate_unreadable_file(self):
        unreadable_file = os.path.join(self.test_dir, "unreadable.csv")
        with open(unreadable_file, "w") as f:
            f.write("\x00\x00\x00")  # Write unreadable content
        result = consolidate_csv(self.test_dir, self.consolidated_file)
        self.assertEqual(result, 0)  # Should return an error code


if __name__ == "__main__":
    unittest.main()
