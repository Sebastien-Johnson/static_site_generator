from textnode import TextNode, TextType

#markdown to textnodes
#delims: code, italic, bold
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        #splits up text via delimeter

        if len(sections)%2 == 0:
            raise Exception("Error: Not valid markdown syntax, missing delimiter")

        for i in range(len(sections)):
            if sections[i] == "":
                continue #skips spaces
            if i%2 == 0: #checks if middle (different text type) section
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        
        new_nodes.extend(split_nodes)

    return new_nodes