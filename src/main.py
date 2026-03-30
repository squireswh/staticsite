# main.py
#
# (c) 2026 Boot.dev
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import LeafNode

def main():
	node = TextNode("evil squirbo", TextType.TEXT_IMAGE, "squirbo.png")
	html_node = text_node_to_html_node(node)
	print(html_node.to_html())

if __name__ == "__main__":
	main()

