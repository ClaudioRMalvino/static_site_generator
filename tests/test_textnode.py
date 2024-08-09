import unittest

from src.textnode import TextNode


class TestTextMode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "italic", "www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", "italic", "www.boot.dev")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", "bold", url="www.boot.dev")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", "bold", url=None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
