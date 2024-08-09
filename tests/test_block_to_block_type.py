import unittest
from src.markdown_blocks import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), "heading")

        block = "### This is a level 3 heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_code(self):
        block = "```\ndef hello():\n    print('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_quote(self):
        block = "> This is a quote\n> It spans multiple lines"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_unordered_list(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_to_block_type(block), "unordered_list")

        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_invalid_ordered_list(self):
        block = "1. First item\n3. Third item\n2. Second item"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_mixed_content(self):
        block = "This is a paragraph with a # symbol."
        self.assertEqual(block_to_block_type(block), "paragraph")

if __name__ == "__main__":
    unittest.main()
