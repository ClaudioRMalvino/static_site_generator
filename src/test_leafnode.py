import unittest

from html import LeafNode


class TestLeadNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(value="This is a text.")
        self.assertIsNone(node.tag)
        self.assertTrue(node.value)
        self.assertIsNone(node.props)

    def test_init_with_parameters(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.boot.dev"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me!")
        self.assertEqual(node.props, {"href": "https://www.boot.dev"})

    def test_to_html(self):
        node1 = LeafNode("Click me!", "a", {"href": "https://www.boot.dev"})
        node2 = LeafNode("This is a paragraph of text", "p")
        node3 = LeafNode("This should return as raw text")
        result1 = node1.to_html()
        self.assertIn('<a href="https://www.boot.dev">Click me!</a>', result1)
        result2 = node2.to_html()
        self.assertIn('<p>This is a paragraph of text</p>', result2)
        result3 = node3.to_html()
        self.assertIn("This should return as raw text", result3)

    def test_repr(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.boot.dev"})
        repr_string = repr(node)
        expected_repr = "LeafNode(value='Click me!', tag='a', props={'href': 'https://www.boot.dev'})"
        self.assertEqual(repr_string, expected_repr)


if __name__ == "__main__":
    unittest.main()
