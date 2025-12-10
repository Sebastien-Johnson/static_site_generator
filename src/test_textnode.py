import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        #checks if nodes are equal

    def test_not_eq(self):
        node = TextNode("Im not him", TextType.BOLD, "boot.dev")
        node2 = TextNode("Im not her", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("Where's the link?", TextType.TEXT)
        self.assertFalse(node.url)

    def test_text_type(self):
        node = TextNode("Same but different", TextType.TEXT)
        node2 = TextNode("Same but different", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_code_block(self):
        node = TextNode("test = 'Really cool'", TextType.CODE)
        self.assertIsInstance(node, TextNode)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
    
    def test_italics(self):
        node = TextNode("This is an italicized text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')

    def test_italics(self):
        node = TextNode("This is an code block node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')

    def test_italics(self):
        node = TextNode("This is a linked node", TextType.LINK, url="https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.props, {"href" : "https://www.boot.dev"})

if __name__ == "__main__":
    unittest.main()