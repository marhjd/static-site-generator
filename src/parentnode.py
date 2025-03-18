from htmlnode import HTMLNode


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
