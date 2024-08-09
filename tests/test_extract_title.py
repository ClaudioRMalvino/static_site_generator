import unittest
from src.markdown_utils import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_simple_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_title_with_leading_trailing_spaces(self):
        markdown = "#    Hello World    "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_title_with_multiple_lines(self):
        markdown = "Some text\n# The Real Title\nMore text"
        self.assertEqual(extract_title(markdown), "The Real Title")

    def test_title_with_multiple_hashtags(self):
        markdown = "## Not the title\n# The Real Title\n### Also not the title"
        self.assertEqual(extract_title(markdown), "The Real Title")

    def test_no_title(self):
        markdown = "Just some text\nWithout a title"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_empty_string(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_title_with_special_characters(self):
        markdown = "# Title with $pecial Ch@racters!"
        self.assertEqual(extract_title(markdown), "Title with $pecial Ch@racters!")

if __name__ == '__main__':
    unittest.main()
