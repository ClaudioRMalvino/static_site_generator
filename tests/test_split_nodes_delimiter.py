import unittest
from src.textnode import TextNode
from src.split_node import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_delimiter_bold(self):
        old_node = TextNode("This is a **bold** text", "text")
        expected = [
            TextNode("This is a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text"),
        ]
        result = split_nodes_delimiter([old_node], "**", "bold")
        self.assertEqual(result, expected)

    def test_delimiter_italic(self):
        old_node = TextNode("This is an *italic* text", "text")
        expected = [
            TextNode("This is an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text"),
        ]
        result = split_nodes_delimiter([old_node], "*", "italic")
        self.assertEqual(result, expected)

    def test_delimiter_code(self):
        old_node = TextNode("There is `code` in this text", "text")
        expected = [
            TextNode("There is ", "text"),
            TextNode("code", "code"),
            TextNode(" in this text", "text"),
        ]
        result = split_nodes_delimiter([old_node], "`", "code")
        self.assertEqual(result, expected)

    def test_bad_syntax(self):
        with self.assertRaises(Exception):
            old_node = TextNode("There is `code` in this text", "text")
            expected = "Invalid Markdown syntax utilized as delimiter."
            result = split_nodes_delimiter([old_node], "'", "code")

    def test_non_text_type(self):
        old_node = TextNode("`code`", "code")
        expected = [TextNode("`code`", "code")]
        result = split_nodes_delimiter([old_node], "`", "code")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
