from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    skip = len(delimiter)
    new_nodes = []
    for node in old_nodes:
        inner_nodes = []

        if node.text_type != TextType.TEXT:
            inner_nodes.append(node)
            new_nodes.extend(inner_nodes)
            continue

        first, last = get_delimiter_positions(node.text, delimiter)

        txt = node.text
        if first > 0 and last != len(txt):
            inner_nodes.append(TextNode(txt[:first], TextType.TEXT))
            inner_nodes.append(TextNode(txt[first+skip:last], text_type))
        elif last + skip == len(txt):
            inner_nodes.append(TextNode(txt[:first], TextType.TEXT))
            inner_nodes.append(TextNode(txt[first+skip:last], text_type))
        else:
            inner_nodes.append(TextNode(txt[first+skip:last], text_type))

        if last+skip != len(txt):
            inner_nodes.append(TextNode(txt[last+skip:], TextType.TEXT))

        new_nodes.extend(inner_nodes)

    return new_nodes

def get_delimiter_positions(text:str, delimiter: str) -> tuple[int, int]:
    first = str.find(text, delimiter)
    last = str.find(text, delimiter, first + 1)
    return (first, last)
