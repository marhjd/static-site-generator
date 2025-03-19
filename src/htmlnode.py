class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props = ""
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        return props

    def __repr__(self) -> str:
        children = ""
        if self.children is not None:
            children = "".join(str(child) for child in self.children)
        return f'<{self.tag}{self.props_to_html()}>{self.value}{children}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)


    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode has no value")
        if self.tag is None:
            return str(self.value)

        properties = ""
        if self.props is not None:
            for k, val in self.props.items():
                properties += f" {k}=\"{val}\""
        return f"<{self.tag}{properties}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag : str, children: list[HTMLNode], props=None) -> None:
        super().__init__(tag, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("parent node has no tag")
        if self.children is None:
            raise ValueError("parent node has no children")

        html = f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            html += c.to_html()
        html += f"</{self.tag}>"

        return html

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
