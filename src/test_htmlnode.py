import unittest

from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()
