import unittest
from src.markdown_utils import extract_markdown_images, extract_markdown_links


class TestMarkdownUtils(unittest.TestCase):

    def test_extract_markdown_images(self):
        text_with_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        result = extract_markdown_images(text_with_images)
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text_with_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        result = extract_markdown_links(text_with_links)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
