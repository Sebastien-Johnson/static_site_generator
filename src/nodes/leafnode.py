from src.nodes.htmlnode import HTMLNode

#a leafnode = a single htmlnode with no children (so its the last in a chain)
#Because of this, it has to have a value and a tag, since it would contain nothing else otherwise
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("Node has no value, all nodes must have a value. Please provide one.")
        if self.tag == None:
            return self.value
        #uses props_to_html to insert empty string or prop
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"