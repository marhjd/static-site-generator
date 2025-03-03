class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        props = ""
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        return props

    def __repr__(self) -> str:
        return f'<{self.tag}{self.props_to_html()}>{self.value}{"".join(str(child) for child in self.children)}</{self.tag}>'
