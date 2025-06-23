class HTMLNode:
    def __init__(
        self, 
        tag=None, 
        value=None, 
        children=None, 
        props=None,
        ):

        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
   
    def props_to_html(self) -> str:
        if not self.props:
                return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items()) 

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}" 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        string_html = ''
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children.")
        for child in self.children:
            string_html += child.to_html()
        return f"<{self.tag}>{string_html}</{self.tag}>"
             
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"