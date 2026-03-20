# textnode.py
#
# (c) 2026 Boot.dev
from enum import Enum

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
