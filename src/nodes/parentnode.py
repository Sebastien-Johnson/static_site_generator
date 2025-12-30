from src.nodes.htmlnode import HTMLNode
from src.nodes.leafnode import LeafNode

#parent of child nodes
#must have child and tag to enclose child
#no value, child takes its place
#put none place holders for unneeded attributes
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self): #must have tag and children
        if self.tag is None:
            raise ValueError("No tag provided, node must have tag, please re-submit with one.")
        
        if self.children is None:
            raise ValueError("No child value")
        
        children_html = ""

        #recursive call on children
        for child in self.children:
            children_html += child.to_html()
            #html nodes have only 'tag' and 'child'
            #nested recursive call will keep adding nested tags if 'child' is just another node
            #final child node with string content will be innermost nested string

        #props to html returns formatted html string of props if it exist, empty space if not
        #children_html inserts recursive call within current html branch of nested tags and final strings/content
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            
        
        #recursive call on children
        #if no child than append
        #if has child than recursive call with current child in iteration as called  node's "children"
        