#!/usr/bin/env python3
import os
import sys
from file_operations import cpy_src_to_dst
from markdownnote import generate_page, genereate_pages_recursive
from textnode import TextNode, TextType
from pathlib import Path

build_dir = Path("docs")
template_file = Path("template.html")
content_dir = Path("content")

def main():

    basepath = ""
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    cpy_src_to_dst(Path("static"), build_dir)
    # generate_page(Path("content/index.md"), Path("template.html"), Path("public/index.html"))
    print("Generating content...")
    genereate_pages_recursive(content_dir, template_file, build_dir, Path(basepath))

main()
