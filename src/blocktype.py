# blocktype.py
#
# (c) ClicKill Microbits

import re
from enum import Enum

class BlockType(Enum):
	BLOCK_PARAGRAPH = "paragraph"
	BLOCK_HEADING = "heading"
	BLOCK_CODE = "code"
	BLOCK_QUOTE = "quote"
	BLOCK_UNORD_LIST = "unordered_list"
	BLOCK_ORD_LIST = "ordered_list"

	def __repr__(self):
		if self == BlockType.BLOCK_HEADING:
			return "BlockType.BLOCK_HEADING"
		elif self == BlockType.BLOCK_CODE:
			return "BlockType.BLOCK_CODE"
		elif self == BlockType.BLOCK_QUOTE:
			return "BlockType.BLOCK_QUOTE"
		elif self == BlockType.BLOCK_UNORD_LIST:
			return "BlockType.BLOCK_UNORD_LIST"
		elif self == BlockType.BLOCK_ORD_LIST:
			return "BlockType.BLOCK_ORD_LIST"
		else:
			return "BlockType.BLOCK_PARAGRAPH"

	def strategy(self, block_text: str) -> str:
		match self:
			case BlockType.BLOCK_HEADING:
				pattern = r"^#{1,6} "
				return re.sub(pattern, "", block_text)
			case BlockType.BLOCK_CODE:
				# pattern = r'```\n[\s\S]*```'
				# return re.sub(pattern, "", block_text)
				without_leading = block_text.removeprefix("```\n")
				without_trailing = without_leading.removesuffix("```")
				return without_trailing
			case BlockType.BLOCK_QUOTE:
				lines = block_text.split('\n')
				new_lines = [line.removeprefix(">").lstrip() for line in lines]
				return " ".join(new_lines)
			case BlockType.BLOCK_UNORD_LIST:
				lines = block_text.split('\n')
				new_lines = [line.removeprefix("- ") for line in lines]
				return "\n".join(new_lines)
			case BlockType.BLOCK_ORD_LIST:
				lines = block_text.split('\n')
				new_lines = []
				for i, line in enumerate(lines):
					expected_number = f"{i + 1}. "
					new_line = re.sub(expected_number, "", line)
					new_lines.append(new_line)
				return "\n".join(new_lines)
			case _:
				return block_text

def block_to_block_type(markdown: str) -> BlockType:
	result = BlockType.BLOCK_PARAGRAPH
	the_ch = markdown[0]
	if the_ch == '#':
		# starts with 1-6 hashtag followed by a space.
		pattern = r"^#{1,6} "
		if re.match(pattern, markdown):
			result = BlockType.BLOCK_HEADING
	elif the_ch == '`':
		# This case is more difficult because we could have 3x '`' characters.
		pattern = r'```\n[\s\S]*```'
		if re.match(pattern, markdown):
			# starts with three '`' and a newline, and ends with '```'.
			result = BlockType.BLOCK_CODE
	elif the_ch == '>':
		lines = markdown.split('\n')
		for line in lines:
			if line[0] != '>':
				break
		else:
			result = BlockType.BLOCK_QUOTE
	elif (the_ch == '-') and (is_unordered_list_item(markdown)):
		lines = markdown.split('\n')
		for line in lines:
			if not is_unordered_list_item(line):
				break
		else:
			result = BlockType.BLOCK_UNORD_LIST
	else:
		lines = markdown.split('\n')
		for i, line in enumerate(lines):
			expected_number = f"{i + 1}. "
			if not re.match(expected_number, line):
				break
		else:
			result = BlockType.BLOCK_ORD_LIST
	return result

def is_unordered_list_item(s: str) -> bool:
	return (len(s) >= 2) and (s[0:2] == '- ')
