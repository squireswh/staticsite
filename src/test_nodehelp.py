# test_nodehelp.py
#
# (c) ClicKill Microbits
import unittest
from nodehelp import markdown_to_blocks, text_to_textnodes, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, split_nodes_delimiter
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

	def test_extract_markdown_images_multiple(self):
		matches = extract_markdown_images(
			'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
		)
		self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], matches)

	def test_extract_markdown_images_none_provided(self):
		matches = extract_markdown_images(
			'This is plain text'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_images_link_provided(self):
		matches = extract_markdown_images(
			'This is a text with a [Apple](https://www.apple.com)'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_images_other_markdown(self):
		matches = extract_markdown_images(
			'some **bold** and _italic_ text'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			'This is a text with a [link](https://www.apple.com)'
		)
		self.assertListEqual([("link", "https://www.apple.com")], matches)

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

	def test_extract_markdown_links_image_provided(self):
		matches = extract_markdown_links(
			'![rick roll](https://i.imgur.com/aKaOqIh.gif)'
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_links_other_markdown(self):
		matches = extract_markdown_links(
			'some **bold** and _italic_ text'
		)
		self.assertListEqual([], matches)

	def test_split_image_no_markup(self):
		node = TextNode("This is basic text.", TextType.TEXT_PLAIN)
		result = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is basic text.", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_image_empty_string(self):
		node = TextNode("", TextType.TEXT_PLAIN)
		result = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_image_empty_list(self):
		result = split_nodes_image([])
		self.assertListEqual([], result)

	def test_split_image_wrong_markup(self):
		node = TextNode("Visit [Boot.dev](https://boot.dev) today", TextType.TEXT_PLAIN)
		result = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("Visit [Boot.dev](https://boot.dev) today", TextType.TEXT_PLAIN, None)
			],
		result
		)

	def test_split_image_basic_markup_beginning(self):
		node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) <- image", TextType.TEXT_PLAIN)
		result = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" <- image", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_image_basic_markup_end(self):
		node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT_PLAIN)
		result = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT_PLAIN),
				TextNode("image", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			result,
		)

	def test_split_images_good_with_bad(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [github](https://github.com)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT_PLAIN),
				TextNode("image", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and a link [github](https://github.com)", TextType.TEXT_PLAIN),
			],
			new_nodes,
		)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT_PLAIN),
				TextNode("image", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT_PLAIN),
				TextNode("second image", TextType.TEXT_IMAGE, "https://i.imgur.com/3elNhQu.png"),
			],
			new_nodes,
		)

	def test_split_images_consecutive(self):
		node = TextNode(
			"This is text with consecutive images: ![image1](https://i.imgur.com/zjjcJKZ.png)![image2](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with consecutive images: ", TextType.TEXT_PLAIN),
				TextNode("image1", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode("image2", TextType.TEXT_IMAGE, "https://i.imgur.com/3elNhQu.png"),
			],
			new_nodes,
		)

	def test_split_images_only_image(self):
		node = TextNode(
			"![image](https://i.imgur.com/zjjcJKZ.png)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.TEXT_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes,
		)

	def test_split_images_other_markup(self):
		node = TextNode("**bold text**", TextType.TEXT_BOLD)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("**bold text**", TextType.TEXT_BOLD),
			],
			new_nodes,
		)
		node = TextNode("_italic text_", TextType.TEXT_ITALIC)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("_italic text_", TextType.TEXT_ITALIC),
			],
			new_nodes,
		)
		node = TextNode("some code snippet", TextType.TEXT_CODE)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("some code snippet", TextType.TEXT_CODE),
			],
			new_nodes,
		)
		node = TextNode("some **bold** and _italic_ text", TextType.TEXT_PLAIN)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("some **bold** and _italic_ text", TextType.TEXT_PLAIN),
			],
			new_nodes,
		)

	def test_split_images_multi_nodes(self):
		node1 = TextNode("plain text, no markup", TextType.TEXT_PLAIN)
		node2 = TextNode("already bold", TextType.TEXT_BOLD)
		node3 = TextNode("text with ![img](https://x.com/a.png) inside", TextType.TEXT_PLAIN)
		new_nodes = split_nodes_image([node1, node2, node3])
		self.assertListEqual(
			[
				TextNode("plain text, no markup", TextType.TEXT_PLAIN),
				TextNode("already bold", TextType.TEXT_BOLD),
				TextNode("text with ", TextType.TEXT_PLAIN),
				TextNode("img", TextType.TEXT_IMAGE, "https://x.com/a.png"),
				TextNode(" inside", TextType.TEXT_PLAIN),
			],
			new_nodes,
		)

	def test_split_link_no_markup(self):
		node = TextNode("This is basic text.", TextType.TEXT_PLAIN)
		result = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is basic text.", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_link_empty_string(self):
		node = TextNode("", TextType.TEXT_PLAIN)
		result = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_link_empty_list(self):
		result = split_nodes_link([])
		self.assertListEqual([], result)

	def test_split_link_wrong_markup(self):
		node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png).", TextType.TEXT_PLAIN)
		result = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png).", TextType.TEXT_PLAIN)
			],
			result,
		)

	def test_split_link_basic_markup_beginning(self):
		node = TextNode("[Boot.dev](https://boot.dev) <- link", TextType.TEXT_PLAIN)
		result = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Boot.dev", TextType.TEXT_LINK, "https://boot.dev"),
				TextNode(" <- link", TextType.TEXT_PLAIN),
			],
			result,
		)

	def test_split_link_basic_markup_end(self):
		node = TextNode("Visit [Boot.dev](https://boot.dev)", TextType.TEXT_PLAIN)
		result = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Visit ", TextType.TEXT_PLAIN),
				TextNode("Boot.dev", TextType.TEXT_LINK, "https://boot.dev"),
			],
			result,
		)

	def test_split_links_good_with_bad(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [github](https://github.com)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link ", TextType.TEXT_PLAIN),
				TextNode("github", TextType.TEXT_LINK, "https://github.com"),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with a link to [GitHub](https://github.com) and another [Apple](https://www.apple.com)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a link to ", TextType.TEXT_PLAIN),
				TextNode("GitHub", TextType.TEXT_LINK, "https://github.com"),
				TextNode(" and another ", TextType.TEXT_PLAIN),
				TextNode("Apple", TextType.TEXT_LINK, "https://www.apple.com"),
			],
			new_nodes,
		)

	def test_split_links_consecutive(self):
		node = TextNode(
			"This is text with consecutive links: [GitHub](https://github.com)[Apple](https://www.apple.com)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with consecutive links: ", TextType.TEXT_PLAIN),
				TextNode("GitHub", TextType.TEXT_LINK, "https://github.com"),
				TextNode("Apple", TextType.TEXT_LINK, "https://www.apple.com"),
			],
			new_nodes,
		)

	def test_split_links_only_link(self):
		node = TextNode(
			"[GitHub](https://github.com)",
			TextType.TEXT_PLAIN,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("GitHub", TextType.TEXT_LINK, "https://github.com"),
			],
			new_nodes,
		)

	def test_split_links_other_markup(self):
		node = TextNode("**bold text**", TextType.TEXT_BOLD)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("**bold text**", TextType.TEXT_BOLD),
			],
			new_nodes,
		)
		node = TextNode("_italic text_", TextType.TEXT_ITALIC)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("_italic text_", TextType.TEXT_ITALIC),
			],
			new_nodes,
		)
		node = TextNode("some code snippet", TextType.TEXT_CODE)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("some code snippet", TextType.TEXT_CODE),
			],
			new_nodes,
		)
		node = TextNode("some **bold** and _italic_ text", TextType.TEXT_PLAIN)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("some **bold** and _italic_ text", TextType.TEXT_PLAIN),
			],
			new_nodes,
		)

	def test_split_links_multi_nodes(self):
		node1 = TextNode("plain text, no markup", TextType.TEXT_PLAIN)
		node2 = TextNode("already bold", TextType.TEXT_BOLD)
		node3 = TextNode("text with [link](https://github.com) inside", TextType.TEXT_PLAIN)
		new_nodes = split_nodes_link([node1, node2, node3])
		self.assertListEqual(
			[
				TextNode("plain text, no markup", TextType.TEXT_PLAIN),
				TextNode("already bold", TextType.TEXT_BOLD),
				TextNode("text with ", TextType.TEXT_PLAIN),
				TextNode("link", TextType.TEXT_LINK, "https://github.com"),
				TextNode(" inside", TextType.TEXT_PLAIN),				
			],
			new_nodes,
		)

	# Tests for images:
	# def test_split_image_no_markup(self):
	# def test_split_image_empty_string(self):
	# def test_split_image_empty_list(self):
	# def test_split_image_wrong_markup(self):
	# def test_split_image_basic_markup_beginning(self):
	# def test_split_image_basic_markup_end(self):
	# def test_split_images_good_with_bad(self):
	# def test_split_images(self):
	# def test_split_images_consecutive(self):
	# def test_split_images_only_image(self):
	# def test_split_images_other_markup(self):
	# def test_split_images_multi_nodes(self):

	# Tests for links:
	# def test_split_link_no_markup(self):
	# def test_split_link_empty_string(self):
	# def test_split_link_empty_list(self):
	# def test_split_link_wrong_markup(self):
	# def test_split_link_basic_markup_beginning(self):
	# def test_split_link_basic_markup_end(self):
	# def test_split_links_good_with_bad(self):
	# def test_split_links(self):
	# def test_split_links_consecutive(self):
	# def test_split_links_only_link(self):
	# def test_split_links_other_markup(self):
	# def test_split_links_multi_nodes(self):

	# tests for text_to_textnode()
	def test_text_to_textnodes_full(self):
		result = text_to_textnodes("some **bold** and _italic_ text")
		self.assertEqual(len(result), 5)
		self.assertEqual(result[1].text_type, TextType.TEXT_BOLD)
		self.assertEqual(result[3].text_type, TextType.TEXT_ITALIC)

	def test_text_to_textnodes_no_markup(self):
		result = text_to_textnodes("some bold and italic text")
		self.assertEqual(len(result), 1)

	def test_text_to_textnodes_empty_string(self):
		result = text_to_textnodes("")
		self.assertEqual(len(result), 0)

	def test_text_to_textnodes_basic_markdown(self):
		result = text_to_textnodes("some **bold** text")
		self.assertEqual(len(result), 3)
		self.assertEqual(result[1].text_type, TextType.TEXT_BOLD)
		result = text_to_textnodes("some _italic_ text")
		self.assertEqual(len(result), 3)
		self.assertEqual(result[1].text_type, TextType.TEXT_ITALIC)
		result = text_to_textnodes("some `code` text")
		self.assertEqual(len(result), 3)
		self.assertEqual(result[1].text_type, TextType.TEXT_CODE)
		result = text_to_textnodes("a [link](https://github.com)")
		self.assertEqual(len(result), 2)
		self.assertEqual(result[1].text_type, TextType.TEXT_LINK)
		result = text_to_textnodes("an ![image](https://i.imgur.com/zjjcJKZ.pn)")
		self.assertEqual(len(result), 2)
		self.assertEqual(result[1].text_type, TextType.TEXT_IMAGE)

	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)