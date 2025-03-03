import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("Hello world", TextType.TEXT)
        node2 = TextNode("Goodbye world", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Hello world", TextType.TEXT)
        node2 = TextNode("Hello world", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("Hello world", TextType.LINK, "https://example.com")
        node2 = TextNode("Hello world", TextType.LINK, "https://example.org")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
            node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
            node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
            self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
