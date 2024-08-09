import unittest
from src.markdown_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        markdown = "This is a single block."
        expected = ["This is a single block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = """
        # Heading

        This is a paragraph.

        * List item 1
        * List item 2
        """
        expected = ["# Heading", "This is a paragraph.", "* List item 1\n* List item 2"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_with_inline_formatting(self):
        markdown = """
        # Heading with **bold**

        Paragraph with *italic* and `code`.

        * List with **bold** item
        * Another *italic* item
        """
        expected = [
            "# Heading with **bold**",
            "Paragraph with *italic* and `code`.",
            "* List with **bold** item\n* Another *italic* item",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_lines_between_blocks(self):
        markdown = """
        Block 1


        Block 2


        Block 3
        """
        expected = ["Block 1", "Block 2", "Block 3"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_code_block(self):
        markdown = """
        Here's a code block:

        ```
        def hello_world():
            print("Hello, World!")
        ```

        And some text after.
        """
        expected = ["Here's a code block:", '```\n        def hello_world():\n            print("Hello, World!")\n        ```', 'And some text after.']
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)


if __name__ == "__main__":
    unittest.main()
