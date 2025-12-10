import unittest

from htmlnode import HTMLNODE

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNODE(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
    
    def test_values(self):
        node = HTMLNODE(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        ) #checks tags
        self.assertEqual(
            node.value,
            "I wish I could read",
        ) #checks children when none
        self.assertEqual(
            node.children,
            None,
        ) #
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNODE(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_eq(self):
        node1 = HTMLNODE(
            "a",
            "https://www.boot.dev",
        )
        node2 = HTMLNODE(
            "a",
            "https://www.boot.dev",
        )
        self.assertEqual(node1.__repr__(), node2.__repr__())

if __name__ == "__main__":
    unittest.main()