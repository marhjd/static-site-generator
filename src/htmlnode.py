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
