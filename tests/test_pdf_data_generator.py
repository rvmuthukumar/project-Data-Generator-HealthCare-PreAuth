

# tests/test_pdf_data_generator.py

import unittest
from unittest.mock import patch, MagicMock
from lambda_src.pdf_data_generator.random_data import generate_patient_data

class TestPdfDataGeneration(unittest.TestCase):

    def test_generate_patient_data(self):
        data = generate_patient_data()
        print(data)
        self.assertIn("First Name", data)
        self.assertIn("Last Name", data)
        # etc. for all essential fields

    @patch("lambda_src.pdf_data_generator.pdf_filler.PdfWriter")
    def test_fill_pdf_mock(self, mock_writer):
        # Example: ensure the fill_pdf function calls PdfWriter and returns bytes
        pass

if __name__ == "__main__":
    unittest.main()
