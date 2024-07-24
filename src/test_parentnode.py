import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_basic_parent_node(self):
        node = ParentNode("div", [LeafNode("Hello, world!")])
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_parent_node_with_multiple_children(self):
        node = ParentNode(
            "p", [LeafNode("First"), LeafNode("Second"), LeafNode("Third")]
        )
        self.assertEqual(node.to_html(), "<p>FirstSecondThird</p>")

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div", [ParentNode("p", [LeafNode("Nested")]), LeafNode("Sibling")]
        )
        self.assertEqual(node.to_html(), "<div><p>Nested</p>Sibling</div>")

    def test_deeply_nested_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode("Item 1")]),
                        ParentNode("li", [LeafNode("Item 2")]),
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )

    def test_parent_node_with_properties(self):
        node = ParentNode(
            "div", [LeafNode("Content")], {"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(), '<div class="container" id="main">Content</div>'
        )

    def test_parent_node_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_parent_node_with_none_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_parent_node_with_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("Content")]).to_html()

    def test_mixed_leaf_and_parent_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("Text"),
                ParentNode("span", [LeafNode("Nested")]),
                LeafNode("More text"),
            ],
        )
        self.assertEqual(node.to_html(), "<div>Text<span>Nested</span>More text</div>")

    def test_parent_node_with_empty_children_list(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_parent_node_repr(self):
        node = ParentNode("div", [LeafNode("Content")], {"class": "container"})
        expected_repr = "ParentNode(tag='div', children=[LeafNode(value='Content', tag=None, props=None)], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
