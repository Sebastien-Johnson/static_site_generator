#splitting raw markdown into text nodes
from src.splitting_text.extract_markdown import extract_markdown_images, extract_markdown_links
from src.nodes.textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        #appends and progresses if not a link/image node
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        #grabs alt texts and links from current node
        images = extract_markdown_images(original_text)

        #appends and progresses if no link/image 
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        i = 0
        current_image = f"![{images[i][0]}]({images[i][1]}"

        while i <= len(images):

            #update current section to be rest of previous split text


            sections = original_text.split(f"![{images[0]}]({images[1]})", 1)
            #removes if not both alt text and link present in section
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

