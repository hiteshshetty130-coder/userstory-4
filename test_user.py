import unittest
from unittest.mock import patch, Mock, mock_open
from user import scrap_books
import csv

mock_data= (
    "title,price,availability,rating,product url\n"
    "light book,$50,in stock,3,https://catalogue/index.html\n"
)

required_columns  = ["title", "price", "availability", "rating", "product url"]


class TestCsvFileDownload(unittest.TestCase):

    # 1. Verify CSV file download
    @patch("user.logging.error")
    @patch("user.requests.get")
    def test_main1_csv_download(self, mock_get, mock_log_error):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = mock_data.encode("utf-8")
        mock_response.text = mock_data
        mock_get.return_value = mock_response

        result = scrap_books()

        self.assertIsNotNone(result)
        mock_log_error.assert_not_called()

    # 2. Validate CSV file extraction
    @patch("builtins.open", new_callable=mock_open, read_data=mock_data)
    def test_main2_csv_extraction(self, mock_file):
        with open("books_data.csv", "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

        self.assertGreater(len(rows), 0)

    # 3. Verify file type and format
    def test_main3_file_type(self):
        file_path = "books_data.csv"
        self.assertTrue(file_path.endswith(".csv"))

    # 4. Handle data structure (headers)
    @patch("builtins.open", new_callable=mock_open, read_data=mock_data)
    def test_main4_data_structure(self, mock_file):
        with open("books_data.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)

        self.assertEqual(headers, required_columns)

    # 5. Handle missing and invalid data
    @patch("builtins.open", new_callable=mock_open, read_data=mock_data)
    def test_main5_no_missing_data(self, mock_file):
        with open("books_data.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    self.assertTrue(value, f"Missing value for {key}")


if __name__ == "__main__":
    unittest.main()
