import unittest

from src.nodes.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_diff_tags(self):
        node = LeafNode("div", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_links(self):
        node = LeafNode("a", "link", {"href" : "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">link</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")