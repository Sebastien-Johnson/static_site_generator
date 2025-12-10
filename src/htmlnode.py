class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        #props is a dict of tag attributes and their values

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
        #converts prop dict to html format and returns

        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        #repr returns the string representation of an object, where it would otherwise be the memory address
        