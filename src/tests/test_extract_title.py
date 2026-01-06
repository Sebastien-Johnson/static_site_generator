import unittest
from src.source_to_destination.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        html = "## Tolkien Fan Club"
        title1 = extract_title(html)
        title2 = "Tolkien Fan Club"
        self.assertEqual(title1, title2)