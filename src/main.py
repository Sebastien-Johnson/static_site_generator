from nodes.textnode import TextNode, TextType
from nodes.splitdelimiter import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word and a `second code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
main()