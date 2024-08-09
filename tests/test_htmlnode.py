import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_with_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_parameters(self):
        node = HTMLNode("p", "Hello", [HTMLNode()], {"class": "text-bold"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertIsInstance(node.children, list)
        self.assertEqual(len(node.children), 1)
        self.assertIsInstance(node.children[0], HTMLNode)
        self.assertEqual(node.props, {"class": "text-bold"})

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "text-bold", "id": "main"})
        result = node.props_to_html()
        self.assertIn(' class="text-bold" id="main"', result)

    def test_repr(self):
        node = HTMLNode("div", "Content", [HTMLNode()], {"class": "container"})
        repr_string = repr(node)

        self.assertIn("HTMLNode(tag='div', value='Content', children=[", repr_string)
        self.assertIn("HTMLNode(", repr_string)  # Check for nested HTMLNode
        self.assertIn("props={'class': 'container'}", repr_string)


if __name__ == "__main__":
    unittest.main()
