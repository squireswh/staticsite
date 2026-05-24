# test_markhtml.py
#
# (c) ClicKill Microbits
import unittest
from markhtml import markdown_to_html_node

class TestMarkHTML(unittest.TestCase):
	def test_paragraphs(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		# print(repr(html))
		self.assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)

	def test_headers(self):
		md = "# Some _italic_ title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h1>Some <i>italic</i> title</h1></div>",
		)
		md = "## Some **bold** title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h2>Some <b>bold</b> title</h2></div>",
		)
		md = "### Some plain title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h3>Some plain title</h3></div>",
		)
		md = "#### Some plain title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h4>Some plain title</h4></div>",
		)
		md = "##### Some plain title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h5>Some plain title</h5></div>",
		)
		md = "###### Some plain title"
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h6>Some plain title</h6></div>",
		)

	def test_unordered_list(self):
		md = """
- apples
- bananas
- cherries
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><ul><li>apples</li><li>bananas</li><li>cherries</li></ul></div>"
			)

	def test_ordered_list(self):
		md = """
1. Ordered item 1
2. Ordered item 2
3. Ordered item 3
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><ol><li>Ordered item 1</li><li>Ordered item 2</li><li>Ordered item 3</li></ol></div>"
			)

	def test_blockquote(self):
		md = """
> Line 1
> Line 2
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><blockquote>Line 1 Line 2</blockquote></div>"
			)

