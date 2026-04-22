# main.py
#
# (c) 2026 Boot.dev
from textnode import TextType, TextNode
from nodehelp import markdown_to_blocks

def main():
	# test = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item\n"
	test = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
	result = markdown_to_blocks(test)
	print(f"{result=}")

if __name__ == "__main__":
	main()

