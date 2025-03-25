import unittest

from textnode import BlockType, TextNode, TextType, block_to_blocktype, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold")

    def test_italic(self):
        node = TextNode("italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic")

    def test_code(self):
        node = TextNode("code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code")

    def test_link(self):
        node = TextNode("link", TextType.LINK, url="www.link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "www.link.com"})
        self.assertEqual(html_node.value, "link")

    def test_image(self):
        node = TextNode("image", TextType.IMAGE, url="/path/to/image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"alt": "image", "src": "/path/to/image"})
        self.assertEqual(html_node.value, "")

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_h1(self):
        result = block_to_blocktype("# H1 Header")
        self.assertEqual(
            BlockType.HEADING, result
        )
    def test_heading_h6(self):
        result = block_to_blocktype("###### H6 Header")
        self.assertEqual(
            BlockType.HEADING, result
        )
    def test_heading_no_space(self):
        result = block_to_blocktype("###H3 Header without space after hashes")
        self.assertEqual(
            BlockType.PARAGRAPH, result
        )
    def test_code_empty(self):
        result = block_to_blocktype("``````")
        self.assertEqual(
            BlockType.CODE, result
        )
    def test_code_example(self):
        result = block_to_blocktype("```def hello(param):\n\tprint(f\"Hello {param}!\")```")
        self.assertEqual(
            BlockType.CODE, result
        )
    def test_code_invalid(self):
        result = block_to_blocktype("``one backtick is missing in the front```")
        self.assertEqual(
            BlockType.PARAGRAPH, result
        )
    def test_quote_single_line(self):
        result = block_to_blocktype("> Be careful that you write accurately rather than much. - Erasmus")
        self.assertEqual(
            BlockType.QUOTE, result
        )
    def test_quote_multiple_lines(self):
        result = block_to_blocktype("> Be careful that you write accurately rather than much.\n> - Erasmus")
        self.assertEqual(
            BlockType.QUOTE, result
        )
    def test_quote_invalid(self):
        result = block_to_blocktype("> Be careful that you write accurately rather than much.\n- Erasmus")
        self.assertEqual(
            BlockType.PARAGRAPH, result
        )
    def test_unordered_list_single_line(self):
        result = block_to_blocktype("- apples")
        self.assertEqual(
            BlockType.UNORDERED_LIST, result
        )
    def test_unordered_list_multiple_lines(self):
        result = block_to_blocktype("- apples\n- oranges\n- bananas")
        self.assertEqual(
            BlockType.UNORDERED_LIST, result
        )
    def test_unordered_list_invalid(self):
        result = block_to_blocktype("- apples\n- oranges\n -bananas")
        self.assertEqual(
            BlockType.PARAGRAPH, result
        )
    def test_ordered_list_single_line(self):
        result = block_to_blocktype("1. apples")
        self.assertEqual(
            BlockType.ORDERED_LIST, result
        )
    def test_ordered_list_multiple_lines(self):
        result = block_to_blocktype("1. apples\n2. oranges\n3. bananas")
        self.assertEqual(
            BlockType.ORDERED_LIST, result
        )
    def test_ordered_list_invalid(self):
        result = block_to_blocktype("1. apples\n2. oranges\n3.bananas")
        self.assertEqual(
            BlockType.PARAGRAPH, result
        )

if __name__ == "__main__":
    unittest.main()
