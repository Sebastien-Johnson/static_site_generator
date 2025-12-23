#convert raw markedown text into text nodes, ruturning a list of nodes
#does not support nested inline elements (a bold word inside italics)
from src.nodes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old_nodes: list of text nodes who's text is raw markdown
    #delimeter: markdown delimeters for different text types
    #text_type: what text the delimiter signifies

    #final return list
    new_nodes = []


    #by re-entering a list of nodes again with a different delimiter, 
    # you can continue splitting text node by node for any number of delimiters
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text.count(delimiter)%2 != 0:
            raise Exception("Invalid markdown syntax, no closing delimiter found.")

        split_texts = old_node.text.split(delimiter)
        text_length = 0
        #return list per markdown delimiter
        split_nodes = []

        for texts in split_texts:
            if texts == "":
                continue
            elif old_node.text[text_length: text_length+len(delimiter)] != f"{delimiter}":
                split_nodes.append(TextNode(f"{texts}", TextType.TEXT))
                text_length += len(texts)
            else:
                split_nodes.append(TextNode(f"{texts}", text_type))
                text_length += len(texts) + 2*len(delimiter)

        new_nodes.extend(split_nodes)
    return new_nodes


#nested delimiter function
#recursive function that checks for nested delimiters
#will require key of delimiters to check
#need to update texttypes in text node to be a list
def split_nested_delimiter(old_nodes):
    delimiters = {
        "**" : TextType.BOLD,
        "_" : TextType.ITALIC,
        "`" : TextType.CODE
    }

    for char in old_nodes.text:
        if char in delimiters:
            old_nodes.text.split()