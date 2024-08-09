import unittest
from src.textnode import TextNode
from src.split_node import split_nodes_image, split_nodes_link


class TestSplitNodesLinkImage(unittest.TestCase):

    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is text with an image ![alt text](https://example.com/image.jpg)",
            "text",
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", "text"),
            TextNode("alt text", "image", "https://example.com/image.jpg"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode("Images: ![img1](url1) and ![img2](url2)", "text")
        result = split_nodes_image([node])
        expected = [
            TextNode("Images: ", "text"),
            TextNode("img1", "image", "url1"),
            TextNode(" and ", "text"),
            TextNode("img2", "image", "url2"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_image(self):
        node = TextNode("Just plain text", "text")
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_split_nodes_image_incomplete_syntax(self):
        node = TextNode("Incomplete ![alt text](url and ![alt", "text")
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link_single(self):
        node = TextNode("This is a [link](https://example.com)", "text")
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a ", "text"),
            TextNode("link", "link", "https://example.com"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode("Links: [link1](url1) and [link2](url2)", "text")
        result = split_nodes_link([node])
        expected = [
            TextNode("Links: ", "text"),
            TextNode("link1", "link", "url1"),
            TextNode(" and ", "text"),
            TextNode("link2", "link", "url2"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_link(self):
        node = TextNode("Just plain text", "text")
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link_incomplete_syntax(self):
        node = TextNode("Incomplete [link](url and [link", "text")
        result = split_nodes_link([node])
        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()
