from htmlnode import HTMLNODE

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.props = props
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        elif self.children == None:
            raise ValueError("No children")
        else:
            html_str = ""
            for child in self.children: #add if prop
                if child.props:
                    html_str += (f"<{self.tag}>{self.prop}={child.to_html()}</{self.tag}>")
                else:
                    html_str += (f"<{self.tag}>{child.to_html()}</{self.tag}>")
            return html_str