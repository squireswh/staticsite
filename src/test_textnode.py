# test_textnode.py
#
# (c) Boot.dev
import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.TEXT_BOLD)
		node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.TEXT_BOLD)
		node2 = TextNode("This is not a text node", TextType.TEXT_BOLD)
		self.assertNotEqual(node, node2)

	def test_not_eq_type(self):
		node = TextNode("This is a text node", TextType.TEXT_BOLD)
		node2 = TextNode("This is a text node", TextType.TEXT_ITALIC)
		self.assertNotEqual(node, node2)

	def test_not_eq_link1(self):
		node = TextNode("This is a link node", TextType.TEXT_LINK, "https://www.apple.com")
		node2 = TextNode("This is a link node", TextType.TEXT_LINK)
		self.assertNotEqual(node, node2)

	def test_not_eq_link2(self):
		node = TextNode("This is a link node", TextType.TEXT_LINK, "https://www.apple.com")
		node2 = TextNode("This is a link node", TextType.TEXT_LINK, "https://www.github.com")
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
