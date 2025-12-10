from htmlnode import HTMLNODE

class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=None)
        self.props= props

    def to_html(self):
        if self.value == None:
            raise ValueError("No value")
        elif self.tag == None:
            return f"{self.value}"
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"