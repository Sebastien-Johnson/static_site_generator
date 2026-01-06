#convert raw text to text nodes
from nodes.textnode import TextNode, TextType
from splitting_text.splitting_markdown import split_nodes_image, split_nodes_link
from splitting_text.splitdelimiter import split_nodes_delimiter

def text_to_textnodes(text): #takes raw markdown text and returns (potential) list of split, filtered nodes
    new_nodes = [TextNode(text, TextType.TEXT)] 
    
    #split nodes by each delimiter and return list of new nodes
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD) 
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

    