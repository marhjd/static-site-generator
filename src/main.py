#!/usr/bin/env python3
import os
from file_operations import cpy_src_to_dst
from markdownnote import generate_page
from textnode import TextNode, TextType
from pathlib import Path

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://boot.dev"))
    cpy_src_to_dst(Path("static"), Path("public"))
    generate_page(Path("content/index.md"), Path("template.html"), Path("public/index.html"))


main()
