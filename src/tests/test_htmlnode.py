import unittest

from src.nodes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_repr(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(node.__repr__(), "HTMLNode(div, Hello, world!, Children: None, {'class': 'greeting', 'href': 'https://boot.dev'})")

    def test_values(self):
        node1 = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual("div", node1.tag)
        self.assertEqual("Hello, world!", node1.value)
        self.assertEqual(None, node1.children)
        self.assertEqual({"class": "greeting", "href": "https://boot.dev"}, node1.props)

