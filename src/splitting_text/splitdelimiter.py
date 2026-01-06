#convert raw markedown text into text nodes, ruturning a list of nodes
#does not support nested inline elements (a bold word inside italics)
from nodes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old_nodes: list of text nodes who's text is raw markdown
    #delimeter: markdown delimeters for different text types
    #text_type: what text the delimiter signifies

    
    new_nodes = [] #final return list
    for old_node in old_nodes: #old_node = single text node with md as text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = [] 
        sections = old_node.text.split(delimiter) #splits single node text at delimiters

        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(sections)): #takes each section of node text and creates new node base on delim location
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes) #extends final list of nodes by individual nodes created by for loop
    return new_nodes #returns list of new nodes 


#nested delimiter function
#recursive function that checks for nested delimiters
#will require key of delimiters to check
#need to update texttypes in text node to be a list
