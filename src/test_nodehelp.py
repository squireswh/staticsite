# test_nodehelp.py
#
# (c) ClicKill Microbits
import unittest
from nodehelp import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
	# tests for "code" delimiter
	def test_split_nodes_delimiter_code_start(self):
		node = TextNode("`code` text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '`', TextType.TEXT_CODE)
		expected = [
			TextNode("code", TextType.TEXT_CODE),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_code_end(self):
		node = TextNode("text `code`", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '`', TextType.TEXT_CODE)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("code", TextType.TEXT_CODE),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_code_middle(self):
		node = TextNode("text `code` text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '`', TextType.TEXT_CODE)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("code", TextType.TEXT_CODE),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_code_all(self):
		node = TextNode("`all this code text`", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '`', TextType.TEXT_CODE)
		expected = [
			TextNode("all this code text", TextType.TEXT_CODE)
		]
		self.assertEqual(out_list, expected)

	# tests for "bold" delimiter
	def test_split_nodes_delimiter_bold_start(self):
		node = TextNode("**bold** text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("bold", TextType.TEXT_BOLD),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_bold_end(self):
		node = TextNode("text **bold**", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("bold", TextType.TEXT_BOLD),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_bold_middle(self):
		node = TextNode("text **bold** text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("bold", TextType.TEXT_BOLD),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_bold_all(self):
		node = TextNode("**all this bold text**", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("all this bold text", TextType.TEXT_BOLD)
		]
		self.assertEqual(out_list, expected)

	# tests for "italics" delimiter
	def test_split_nodes_delimiter_italics_start(self):
		node = TextNode("_italics_ text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '_', TextType.TEXT_ITALIC)
		expected = [
			TextNode("italics", TextType.TEXT_ITALIC),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_italics_end(self):
		node = TextNode("text _italics_", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '_', TextType.TEXT_ITALIC)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("italics", TextType.TEXT_ITALIC),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_italics_middle(self):
		node = TextNode("text _italics_ text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '_', TextType.TEXT_ITALIC)
		expected = [
			TextNode("text ", TextType.TEXT_PLAIN),
			TextNode("italics", TextType.TEXT_ITALIC),
			TextNode(" text", TextType.TEXT_PLAIN),
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_italics_all(self):
		node = TextNode("_all this italics text_", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '_', TextType.TEXT_ITALIC)
		expected = [
			TextNode("all this italics text", TextType.TEXT_ITALIC)
		]
		self.assertEqual(out_list, expected)

	# other tests
	def test_split_nodes_delimiter_mismatch_beginning(self):
		node = TextNode("all this bold text**", TextType.TEXT_PLAIN)
		with self.assertRaises(Exception):
			out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)

	def test_split_nodes_delimiter_mismatch_end(self):
		node = TextNode("**all this bold text", TextType.TEXT_PLAIN)
		with self.assertRaises(Exception):
			split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)

	def test_split_nodes_delimiter_non_plain_unchanged(self):
		node = TextNode("**all this bold text**", TextType.TEXT_BOLD)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("**all this bold text**", TextType.TEXT_BOLD)
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_plain_unchanged(self):
		node = TextNode("plain old boring text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("plain old boring text", TextType.TEXT_PLAIN)
		]
		self.assertEqual(out_list, expected)

	def test_split_nodes_delimiter_multi_nodes(self):
		node1 = TextNode("plain old boring text", TextType.TEXT_PLAIN)
		node2 = TextNode("**all this bold text**", TextType.TEXT_BOLD)
		node3 = TextNode("more plain text", TextType.TEXT_PLAIN)
		out_list = split_nodes_delimiter([node1, node2, node3], '**', TextType.TEXT_BOLD)
		expected = [
			TextNode("plain old boring text", TextType.TEXT_PLAIN),
			TextNode("**all this bold text**", TextType.TEXT_BOLD),
			TextNode("more plain text", TextType.TEXT_PLAIN)
		]
		self.assertEqual(out_list, expected)

	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			'This is a text with a [link](https://www.apple.com)'
		)
		self.assertListEqual([("link", "https://www.apple.com")], matches)

	def test_extract_markdown_images_multiple(self):
		matches = extract_markdown_images(
			'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
		)
		self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], matches)

	def test_extract_markdown_links_multiple(self):
		matches = extract_markdown_links(
			'This is a text with a [Apple](https://www.apple/com) and [GitHub](https://github.com)'
		)
		self.assertListEqual([('Apple', 'https://www.apple/com'), ('GitHub', 'https://github.com')], matches)

	def test_extract_markdown_links_none_provided(self):
		matches = extract_markdown_links(
			'This is plain text'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_images_none_provided(self):
		matches = extract_markdown_images(
			'This is plain text'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_links_image_provided(self):
		matches = extract_markdown_links(
			'![rick roll](https://i.imgur.com/aKaOqIh.gif)'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_images_link_provided(self):
		matches = extract_markdown_images(
			'This is a text with a [Apple](https://www.apple.com)'
		)
		self.assertListEqual([], matches)

