#represents a node in the doc tree
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #string of html tag name
        self.value = value #string value of the tag 
        self.children = children #children of the current node
        self.props = props #dict of attributes for the html tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")


    #returns formatted string of node attributes IN html format
    def props_to_html(self):
        if self.props == None:
            return ""
        
        formatted_props = ""

        for prop in self.props:
            formatted_props += f' {prop}="{self.props[prop]}"'
        
        return formatted_props
    
    #returns string of HTML attributes(values)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, Children: {self.children}, {self.props})"