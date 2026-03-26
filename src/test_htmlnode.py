# test_htmlnode.py
#
# (c) ClicKill Microbits
import unittest
from htmlnode import HTMLNode, LeafNode
from handy import quote_it

class TestHTMLNode(unittest.TestCase):
	def test_node(self):
		htmlnode = HTMLNode("tag", "value", [], {"href": "https://www.apple.com", "target": "Apple"})
		self.assertEqual(htmlnode.tag, "tag")
		self.assertEqual(htmlnode.value, "value")
		self.assertEqual(htmlnode.children, [])
		self.assertEqual(htmlnode.props, {"href": "https://www.apple.com", "target": "Apple"})

	def text_to_html(self):
		with self.assertRaises(NotImplementedError):
			htmlnode.to_html()

	def test_props_to_html(self):
		htmlnode = HTMLNode("tag", "value", [], {"href": "https://www.apple.com", "target": "Apple"})
		self.assertEqual(htmlnode.props_to_html(), ' href="https://www.apple.com" target="Apple"')

	def test_props_to_html2(self):
		htmlnode = HTMLNode("tag", "value", [], {})
		self.assertEqual(htmlnode.props_to_html(), "")

	def test_props_to_html3(self):
		htmlnode = HTMLNode("tag", "value", [], None)
		self.assertEqual(htmlnode.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
	def test_leaf_node_paragraph(self):
		htmlleaf = LeafNode("p", "This is a paragraph of text.")
		self.assertEqual(htmlleaf.to_html(), "<p>This is a paragraph of text.</p>")

	def test_leaf_node_link(self):
		htmlleaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(htmlleaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

	def test_leaf_node_no_tag(self):
		htmlleaf = LeafNode(None, "raw text")
		self.assertEqual(htmlleaf.to_html(), "raw text")

	def test_leaf_node_span(self):
		htmlleaf = LeafNode("span", "marker for CSS")
		self.assertEqual(htmlleaf.to_html(), '<span>marker for CSS</span>')

	def test_leaf_node_empty_value_str(self):
		htmlleaf = LeafNode("p", "")
		self.assertEqual(htmlleaf.to_html(), "<p></p>")

	def test_leaf_node_fail(self):
		with self.assertRaises(ValueError):
			LeafNode("p", None).to_html()

	def test_leaf_node_no_tag2(self):
		htmlleaf = LeafNode(None, "")
		self.assertEqual(htmlleaf.to_html(), "")

	def test_repr(self):
		htmlleaf = LeafNode("img", "", {"src": "cat.png", "alt": "a cat"})
		self.assertEqual(repr(htmlleaf), '"img", "", {\'src\': \'cat.png\', \'alt\': \'a cat\'}')

	def test_leaf_node_img(self):
	    node = LeafNode("img", "", {"src": "cat.png", "alt": "a cat"})
	    self.assertEqual(node.to_html(), '<img src="cat.png" alt="a cat"></img>')

