import unittest
from src.textnode import TextNode
from src.htmlnode import LeafNode
from src.text_to_node import text_node_to_leaf_node


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_text(self):
        text_node = TextNode(text_type="text", text="Just plain text")
        expected = LeafNode(value="Just plain text", tag=None, props=None)
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_text_type_bold(self):
        text_node = TextNode(text_type="bold", text="Bold text")
        expected = LeafNode(value="Bold text", tag="b", props=None)
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_text_type_italic(self):
        text_node = TextNode(text_type="italic", text="Italic text")
        expected = LeafNode(value="Italic text", tag="i", props=None)
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_text_type_code(self):
        text_node = TextNode(text_type="code", text="Code text")
        expected = LeafNode(value="Code text", tag="code", props=None)
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_text_type_link(self):
        text_node = TextNode(
            text_type="link", text="Link text", url="http://example.com"
        )
        expected = LeafNode(
            value="Link text", tag="a", props={"href": "http://example.com"}
        )
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_text_type_image(self):
        text_node = TextNode(
            text_type="image",
            text="An image",
            url="http://example.com/image.png",
        )
        expected = LeafNode(
            value="",
            tag="img",
            props={"src": "http://example.com/image.png", "alt": "An image"},
        )
        result = text_node_to_leaf_node(text_node)
        self.assertEqual(result, expected)

    def test_unknown_text_type(self):
        text_node = TextNode(text_type="unknown", text="Unknown text")
        with self.assertRaises(Exception) as context:
            text_node_to_leaf_node(text_node)
        self.assertTrue("Unknown text type" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
