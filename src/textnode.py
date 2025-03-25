from enum import Enum
import re
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(markdown_block:str) -> BlockType:
    heading = re.compile("^#{1,6} \S+")
    code = re.compile("^```(?s:.)*```$")
    quote = re.compile("^>.+", re.MULTILINE)
    unordered_list = re.compile("^- .*", re.MULTILINE)
    ordered_list = re.compile("^1\. ")

    if heading.match(markdown_block):
        return BlockType.HEADING
    if code.match(markdown_block):
        return BlockType.CODE
    if quote.match(markdown_block):
        # make sure each line starts with a '>'
        for line in markdown_block.splitlines():
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if unordered_list.match(markdown_block):
        # make sure each line starts with a '- '
        for line in markdown_block.splitlines():
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if ordered_list.match(markdown_block):
        digit = 1
        for line in markdown_block.splitlines():
            if not line.startswith(f"{digit}. "):
                return BlockType.PARAGRAPH
            digit += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

class TextNode:
    def __init__(self, text:str, text_type:TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        """TextNode(TEXT, TEXT_TYPE, URL)"""
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node : TextNode):
    """Converts a TextNode to an equivalent HTMLNode (LeafNode) representation."""
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"{text_node}'s type '{text_node.text_type}' is not a defined TextType")
