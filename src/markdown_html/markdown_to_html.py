#converts full markdown doc into single parent html node with <div> tag containing all the children nodes
from src.splitting_text.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.nodes.htmlnode import HTMLNode
from src.nodes.parentnode import ParentNode
from src.nodes.leafnode import LeafNode
from src.nodes.textnode import TextNode, TextType, text_node_to_html_node
from src.splitting_text.text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    #takes raw markdown text and returns parent node with div tag and child nodes of each type
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    #checks block type
    block_type = block_to_block_type(block)
    #paragraph, heading, code, olist, ulist, quote
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return header_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    #raise value error otherwise
    raise ValueError("Invalid block format submitted")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    #takes raw md text and creates textnodes with text_to_text_nodes
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
    #transfers texnode to html node with text to html node function and appends to new list
    

def paragraph_to_html_node(block):
    #breaks blocks into lines
    lines = block.split("\n")
    #joins with spaces to make paragraph
    paragraph = " ".join(lines)
    #lines to nodes with text to children 
    children = text_to_children(paragraph)
    #returns parent node with children
    return ParentNode("p", children)

def header_to_html_node(block):
    #count # for header size
    head_count = 0
    for char in block:
        if char == "#":
            head_count += 1
        else:
            break
    #make sure header level isnt over 6
    if head_count + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {head_count}")
    
    #create text from text in block beyond heading
    text = block[head_count +1:]
    #text to children
    children = text_to_children(text)
    #returns parent node with children
    return ParentNode(f"h{head_count}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    #check if starts and ends with ```
    #create text var from text within back tics
    text = block[4:-3]
    #create raw text node from text
    raw_text_node = TextNode(text, TextType.TEXT)
    #child node with text to html node
    child = text_node_to_html_node(raw_text_node)
    #return parent node with 'pre' tag, child node with code and 'code' tag
    code_node = ParentNode("code", [child])
    return ParentNode("pre", [code_node]) #code and child nodes as list to become iterable

def olist_to_html(block):
    #create list of items from split block at new lines
    items = block.split("\n") #split at new lines for clean formatting
    #create return list
    new_items = []
    #iterate through through each line
    for item in items: 
        #create text var from item beyond initial number, period and space (3 spaces)
        text = item[3:]
        #text to children
        children = text_to_children(text)
        #append parent node to return list with child and "li" tag
        new_items.append(ParentNode("li", children))
    #return parent node with return list as child and "ol" tag
    return ParentNode("ol", new_items)

def ulist_to_html(block):
    #create list of items from split block at new lines
    items = block.split("\n")  #split at new lines for clean formatting
    #create return list
    new_items = []
    #iterate through items
    for item in items:
        #create text var from item beyond initial dash and space (2 spaces)
        text = item[2:]
        #text to children
        children = text_to_children(text)
        #append parent node to return list with child and "li" tag
        new_items.append(ParentNode("li", children))
    #return parent node with return list as child and "ol" tag
    return ParentNode("ul", new_items)

def quote_to_html(block):
    #create list of lines from split block at new lines
    lines = block.split("\n")  #split at new lines for clean formatting
    #create new lines list
    new_lines = []
    #iterate through lines
    for line in lines:
        #check if line startswith > and raise value error
        if not line.startswith(">"):
            raise ValueError("Improper quote block")
        #strip left '>' and then strip of white space on both ends then append to return list
        new_lines.append(line.lstrip(">").strip())
    #join new lines with spaces
    content = " ".join(new_lines)
    #text to children
    children = text_to_children(content)
    #asign to parent node with "blockquote" tag and children and return
    return ParentNode("blockquote", children)
