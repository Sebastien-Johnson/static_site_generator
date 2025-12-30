#splitting raw markdown into text nodes
from src.splitting_text.extract_markdown import extract_markdown_images, extract_markdown_links
from src.nodes.textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes: #iterates through list of nodes
        if old_node.text_type != TextType.TEXT: #if not a text type (already a split node), 
            new_nodes.append(old_node) # appends current old_node as is
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text) #creates list of (alt, link) tuples

        if len(images) == 0: #if no links, append current old_node as is
            new_nodes.append(old_node) # append current old_node as is
            continue
        for image in images: #iterates through each set of tuples
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1) #splits original text by tuple(alt, link)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            
            if sections[0] != "": #checks if empty section: link split text at begining or end
                new_nodes.append(TextNode(sections[0], TextType.TEXT)) #creates text node if not empty section 
            new_nodes.append(TextNode( image[0], TextType.IMAGE, image[1]))
            #creates link node after potential text node to be in order in final list
            original_text = sections[1] #sets original text to next section
            
        if original_text != "": #creates text node from remaining  text if possible
            new_nodes.append(TextNode(original_text, TextType.TEXT)) 
    return new_nodes #returns list of text nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes: #iterates through list of nodes
        if old_node.text_type != TextType.TEXT: #if not a text type (already a split node), 
            new_nodes.append(old_node) # appends current old_node as is
            continue
        original_text = old_node.text 
        links = extract_markdown_links(original_text) #creates list of (alt, link) tuples

        if len(links) == 0: #if no links, 
            new_nodes.append(old_node) # append current old_node as is
            continue

        for link in links: #iterates through list of links
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1) #splits original text by tuple(alt, link) ONCE
            if len(sections) != 2: #should  only be 2 sections if only ONE link is removed
                raise ValueError("invalid markdown, link section not closed") 
            
            if sections[0] != "": #checks if empty section: link split text at begining or end
                new_nodes.append(TextNode(sections[0], TextType.TEXT)) #creates text node if not empty section 
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1])) 
            #creates link node after potential text node to be in order in final list
            original_text = sections[1] #sets original text to 2nd section to check for next possible links

        if original_text != "": #creates text node from remaining  text if possible
            new_nodes.append(TextNode(original_text, TextType.TEXT)) 
    return new_nodes #returns list of old text nodes

