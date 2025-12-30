#convert raw text to text nodes
from src.nodes.textnode import TextNode, TextType
from src.splitting_text.splitting_markdown import split_nodes_image, split_nodes_link
from src.splitting_text.splitdelimiter import split_nodes_delimiter

def text_to_textnodes(text): #takes raw markdown text and returns (potential) list of split, filtered nodes
    old_node = [TextNode(text, TextType.TEXT)] 
    #split nodes by each delimiter and return list of new nodes
    new_nodes = split_nodes_delimiter(old_node, "**", TextType.BOLD) 
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

    