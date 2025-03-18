from htmlnode import HTMLNode

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
