#!/usr/bin/env python3
from textnode import TextNode, TextType

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://boot.dev"))

main()
