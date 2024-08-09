import unittest
from src.textnode import TextNode
from src.text_to_node import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_simple(self):
        text = "This is **text** with an *italic* word and a `code block`"
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_with_image_and_link(self):
        text = "This is an ![image](https://example.com/image.jpg) and a [link](https://example.com)"
        expected = [
            TextNode("This is an ", "text"),
            TextNode("image", "image", "https://example.com/image.jpg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://example.com"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_complex(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://example.com/image.jpg) and a [link](https://example.com)"
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://example.com/image.jpg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://example.com"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_no_special_text(self):
        text = "This is just plain text"
        expected = [TextNode("This is just plain text", "text")]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_text_to_textnodes_multiple_special_texts(self):
        text = "**Bold** and *italic* and **more bold** and *more italic*"
        expected = [
            TextNode("Bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" and ", "text"),
            TextNode("more bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("more italic", "italic"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)


if __name__ == "__main__":
    unittest.main()
