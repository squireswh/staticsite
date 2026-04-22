# blocktype.py
#
# (c) ClicKill Microbits

from enum import Enum

class BlockType(Enum):
	BLOCK_PARAGRAPH = "paragraph"
	BLOCK_HEADING = "heading"
	BLOCK_CODE = "code"
	BLOCK_QUOTE = "quote"
	BLOCK_UO_LIST = "unordered_list"
	BLOCK_ORD_LIST = "ordered_list"

