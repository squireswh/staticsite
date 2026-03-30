# test_htmlnode.py
#
# (c) ClicKill Microbits
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from handy import quote_it

class TestText2HTML(unittest.TestCase):
	def test_text_to_html_plain(self):
		htmlnode = text_node_to_html_node(TextNode("plain text", TextType.TEXT_PLAIN))
		self.assertEqual(htmlnode.to_html(), "plain text")

	def test_text_to_html_bold(self):
		htmlnode = text_node_to_html_node(TextNode("bold text", TextType.TEXT_BOLD))
		self.assertEqual(htmlnode.to_html(), "<b>bold text</b>")

	def test_text_to_html_italics(self):
		htmlnode = text_node_to_html_node(TextNode("italic text", TextType.TEXT_ITALIC))
		self.assertEqual(htmlnode.to_html(), "<i>italic text</i>")

	def test_text_to_html_code(self):
		the_code = "// This is code"
		htmlnode = text_node_to_html_node(TextNode(the_code, TextType.TEXT_CODE))
		self.assertEqual(htmlnode.to_html(), f"<code>{the_code}</code>")

	def test_text_to_html_link(self):
		htmlnode = text_node_to_html_node(TextNode("url", TextType.TEXT_LINK, "https://www.apple.com"))
		self.assertEqual(htmlnode.to_html(), f'<a href={quote_it("https://www.apple.com")}>url</a>')

	def test_text_to_html_image(self):
		htmlnode = text_node_to_html_node(TextNode("evil squirbo", TextType.TEXT_IMAGE, "squirbo.png"))
		self.assertEqual(htmlnode.to_html(), f'<img src={quote_it("squirbo.png")} alt={quote_it("evil squirbo")}></img>')

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

class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_multiple_children(self):
		child_node1 = LeafNode("span", "child")
		child_node2 = LeafNode(None, "Our text")
		parent_node = ParentNode("div", [child_node1, child_node2])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span>Our text</div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_great_grandchildren(self):
		g_grandchild_node = LeafNode("i", "great grandchild")
		grandchild_node = ParentNode("b", [g_grandchild_node])
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b><i>great grandchild</i></b></span></div>",
		)

	def test_to_html_mixed(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		sibling_node = LeafNode("p", "paragraph")
		parent_node = ParentNode("div", [child_node, sibling_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span><p>paragraph</p></div>",
		)

	def test_no_tag(self):
		parent_node = ParentNode(None, [LeafNode("span", "child")])
		with self.assertRaises(ValueError):
			parent_node.to_html()

	def test_no_children(self):
		parent_node = ParentNode("div", None)
		with self.assertRaises(ValueError):
			_ = parent_node.to_html()

	def test_to_html_empty_children(self):
		parent_node = ParentNode("div", [])
		self.assertEqual(parent_node.to_html(), "<div></div>")

	def test_to_html_no_props(self):
		parent_node = ParentNode("div", [])
		self.assertEqual(parent_node.to_html(), "<div></div>")

	def test_to_html_props_None(self):
		parent_node1 = ParentNode("div", [])
		parent_node2 = ParentNode("div", [], None)
		self.assertEqual(parent_node1.to_html(), parent_node2.to_html())

	def test_to_html_with_props(self):
		parent_node = ParentNode("div", [], {"class": "product-item"})
		self.assertEqual(parent_node.to_html(), f'<div class={quote_it("product-item")}></div>')

	def test_to_html_with_props_children(self):
		child_node = LeafNode("h2", "header 2")
		parent_node = ParentNode("div", [child_node], {"class": "product-item"})
		self.assertEqual(parent_node.to_html(), f'<div class={quote_it("product-item")}><h2>header 2</h2></div>')
