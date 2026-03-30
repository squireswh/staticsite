# textnode.py
#
# (c) 2026 Boot.dev
from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT_PLAIN = "text"
	TEXT_BOLD = "bold"
	TEXT_ITALIC = "italic"
	TEXT_CODE = "code"
	TEXT_LINK = "link"
	TEXT_IMAGE = "image"

class TextNode:
	def __init__(self, our_text,text_type,url=None):
		self.text = our_text
		self.text_type = text_type
		self.url = url

	def __eq__(self,other):
		return (self.text==other.text) and (self.text_type==other.text_type) and (self.url==other.url)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
	the_tag = text_node.text_type
	if the_tag == TextType.TEXT_PLAIN:
		return LeafNode(None, text_node.text)
	elif the_tag == TextType.TEXT_BOLD:
		return LeafNode("b", text_node.text)
	elif the_tag == TextType.TEXT_ITALIC:
		return LeafNode("i", text_node.text)
	elif the_tag == TextType.TEXT_CODE:
		return LeafNode("code", text_node.text)
	elif the_tag == TextType.TEXT_LINK:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	elif the_tag == TextType.TEXT_IMAGE:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	else:
		raise Exception("TextNode must have a valid text type")

