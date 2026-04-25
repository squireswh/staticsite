# blocktype.py
#
# (c) ClicKill Microbits

from enum import Enum
import re

class BlockType(Enum):
	BLOCK_PARAGRAPH = "paragraph"
	BLOCK_HEADING = "heading"
	BLOCK_CODE = "code"
	BLOCK_QUOTE = "quote"
	BLOCK_UNORD_LIST = "unordered_list"
	BLOCK_ORD_LIST = "ordered_list"

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
