import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_create_node(self):
        node = HTMLNode(tag="h1", value="Test", props={"class": "test"}, children=[HTMLNode(tag="p", value="Hello World!")])
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Test")
        self.assertEqual(node.props, {"class": "test"})
        if node.children is not None:
            self.assertEqual(node.children[0].tag, "p")
            self.assertEqual(node.children[0].value, "Hello World!")

    def test_props_to_html(self):
        node = HTMLNode(tag="h1", value="Test", props={"class": "test", "id": "test-id"}, children=[HTMLNode(tag="p", value="Hello World!")])
        self.assertEqual(node.props_to_html(), ' class="test" id="test-id"')

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Test", props={"class": "test", "id": "test-id"}, children=[HTMLNode(tag="p", value="Hello World!")])
        self.assertEqual(repr(node), '<h1 class="test" id="test-id">Test<p>Hello World!</p></h1>')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    def test_leaf_to_html_no_tag(self):
            node = LeafNode(None, "Hello, world!")
            self.assertEqual(node.to_html(), "Hello, world!")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == '__main__':
    unittest.main()
