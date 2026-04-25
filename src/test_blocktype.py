# test_blocktype.py
#
# (c) ClicKill Microbits
import unittest
from blocktype import BlockType,block_to_block_type

class TestBlockType(unittest.TestCase):
	def test_block_to_blocktype_headers(self):
		block = "# Header 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "## Header 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "### Header 3"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "#### Header 4"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "##### Header 5"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "###### Header 6"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_HEADING)
		block = "#Malformed header 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "####### Malformed header 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)

	def test_block_to_blocktype_code(self):
		block = "```\n# python comment\n```"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_CODE)
		block = "```\n# python comment\ndef func():\n\tpass\n```"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_CODE)
		block = "```\n# malformed code block 1\n"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "```\n# malformed code block 2\n``"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "``\n# malformed code block 3\n```"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)

	def test_block_to_blocktype_quote(self):
		block = "> happy quote path 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_QUOTE)
		block = ">happy quote path 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_QUOTE)
		block = "> a quote line\n> another quote"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_QUOTE)
		block = "> happy quote line\n- unordered list item 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)

	def test_block_to_blocktype_uo_list(self):
		block = "- happy unordered list item"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_UNORD_LIST)
		block = "- happy unordered list item 1\n- happy unordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_UNORD_LIST)
		block = "-unhappy unordered list"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "- happy unordered list item 1\n-unhappy unordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)

	def test_block_to_blocktype_ord_list(self):
		block = "1. happy ordered list item"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_ORD_LIST)
		block = "1. happy ordered list item\n2. happy ordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_ORD_LIST)
		block = "1.unhappy ordered list item 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "1 unhappy ordered list item 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "1. happy ordered list item 1\n2.unhappy ordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "1. happy ordered list item 1\n2 unhappy ordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "0. happy ordered list item 1\n2. happy ordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "2. unhappy ordered list item 1\n2.unhappy ordered list item 2"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)

	def test_block_to_blocktype_paragraph(self):
		block = "A happy paragraph"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "A happy paragraph. It has more than one sentence."
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "#Malformed header"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "```\n# malformed code block 1\n"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "> happy quote line\n- unordered list item 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "-unhappy unordered list"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)
		block = "1.unhappy ordered list item 1"
		result = block_to_block_type(block)
		self.assertEqual(result, BlockType.BLOCK_PARAGRAPH)







