import unittest

from src.nodes.textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This text", TextType.TEXT)
        node2 = TextNode("Is different from this one", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_diff_type(self):
        node = TextNode("Same but different", TextType.TEXT)
        node2 = TextNode("Same but different", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a code block", TextType.CODE, url=None)
        node2 = TextNode("This is a code block", TextType.CODE, url=None)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")  

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")  
    
    def test_link(self):
        node = TextNode("link to boot.dev", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link to boot.dev")
        self.assertEqual(html_node.props,  {" href": "https://www.boot.dev"})

    def test_image(self):
        node = TextNode("image of boot.dev", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-small.webp")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,  
            {
                "src": "https://www.boot.dev/img/bootdev-logo-full-small.webp",
                "alt": "image of boot.dev"
            }
            )