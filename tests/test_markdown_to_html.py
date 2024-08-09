import unittest
from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.markdown_to_html import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraph(self):
        markdown = "This is a paragraph with **bold** and *italic* text."
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("p", [
                LeafNode("This is a paragraph with "),
                LeafNode("bold", "b"),
                LeafNode(" and "),
                LeafNode("italic", "i"),
                LeafNode(" text."),
            ])
        ])
        self.assertEqual(html_node, expected)

    def test_heading(self):
        markdown = "# This is a heading"
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode("This is a heading")])
        ])
        self.assertEqual(html_node, expected)

    def test_code_block(self):
        markdown = "```\nprint('Hello, World!')\n```"
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("pre", [
                ParentNode("code", [LeafNode("print('Hello, World!')")])
            ])
        ])
        self.assertEqual(html_node, expected)

    def test_quote(self):
        markdown = "> This is a quote\n> It spans multiple lines"
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("blockquote", [LeafNode("This is a quote It spans multiple lines")])
        ])
        self.assertEqual(html_node, expected)

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode("Item 1")]),
                ParentNode("li", [LeafNode("Item 2")]),
                ParentNode("li", [LeafNode("Item 3")]),
            ])
        ])
        self.assertEqual(html_node, expected)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [LeafNode("First item")]),
                ParentNode("li", [LeafNode("Second item")]),
                ParentNode("li", [LeafNode("Third item")]),
            ])
        ])
        self.assertEqual(html_node, expected)

    def test_multiple_blocks(self):
        markdown = """
                    # Heading
                    This is a paragraph.
                    * List *item 1 italicized*
                    * List item 2
                    > This is a quote
                    """
        html_node = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode("Heading")]),
            ParentNode("p", [LeafNode("This is a paragraph.")]),
            ParentNode("ul", [
                ParentNode("li", [LeafNode("List"), LeafNode("item 1 italicized", "i")]),
                ParentNode("li", [LeafNode("List item 2")]),
            ]),
            ParentNode("blockquote", [LeafNode("This is a quote")]),
        ])
        print(f"html_node: {html_node}")
        print(f"expected: {expected}")
        self.assertEqual(html_node, expected)

if __name__ == '__main__':
    unittest.main()
