#!/usr/bin/env python3
from file_operations import cpy_src_to_dst
from textnode import TextNode, TextType
from pathlib import Path

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://boot.dev"))
    cpy_src_to_dst(Path("static"), Path("public"))

main()
