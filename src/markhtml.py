# markhtml.py
#
# (c) ClicKill Microbits
from blocktype import BlockType, block_to_block_type
from nodehelp import markdown_to_blocks, text_to_textnodes
from htmlnode import HTMLNode, ParentNode, TagType
from textnode import text_node_to_html_node, TextType, TextNode

def some_inline_markdown_parser(text: str) -> list[TextNode]:
	return text_to_textnodes(text)

def text_to_children(text) -> list[HTMLNode]:
	text_nodes = some_inline_markdown_parser(text)

	# Empty list[HTMLNode].
	html_nodes = []
	for text_node in text_nodes:
		html_nodes.append(text_node_to_html_node(text_node))
	return html_nodes

def markdown_to_html_node(markdown: str) -> HTMLNode:
	# 1 separate markdown into blocks.
	blocks = markdown_to_blocks(markdown)
	# print(f'blocks={blocks}')

	# 'blocks' is now a list[str].
	if len(blocks) == 0:
		raise Exception("'blocks' is an empty list")

	node_list = []

	# 2 loop over each block.
	for block in blocks:
		# 2.1 determine the type of block.
		#     'block_type' is type BlockType.
		block_type = block_to_block_type(block)
		# print(f'block_type={block_type}')

		# 2.2 based on the type of block (in the list),
		#     create an appropriate HTMLNode instance.
		#     'block_node' is type HTMLNode, but - in practice - will be a
		#     subclass of HTMLNode.
		block_node = create_html_node(block, block_type)
		# print(f'block_node={block_node}')
		node_list.append(block_node)

	# 'node_list' is now a list[HTMLNode].
	return ParentNode(TagType.TAG_DIV.value, node_list)

def create_html_node(block: str, block_type: BlockType) -> HTMLNode:
	result = None
	# print(f"found {block=}\n")	
	if block_type == BlockType.BLOCK_HEADING:
		# how many hashtags does 'block' have?
		heading_type = count_hashtags(block)

		# Remove the hashtags.
		no_hashtag_block = get_rid_of_hashtags(block, heading_type)
		children = text_to_children(no_hashtag_block)
		match heading_type:
			case 1:
				result = ParentNode(TagType.TAG_HEADER1.value, children)
			case 2:
				result = ParentNode(TagType.TAG_HEADER2.value, children)
			case 3:
				result = ParentNode(TagType.TAG_HEADER3.value, children)
			case 4:
				result = ParentNode(TagType.TAG_HEADER4.value, children)
			case 5:
				result = ParentNode(TagType.TAG_HEADER5.value, children)
			case 6:
				result = ParentNode(TagType.TAG_HEADER6.value, children)
	elif block_type == BlockType.BLOCK_CODE:
		# print(f'{block=}')
		new_block = block_type.strategy(block)
		# print(f'{new_block=}')
		raw_text_node = text_node_to_html_node(TextNode(new_block, TextType.TEXT_PLAIN))
		code_node = ParentNode(TagType.TAG_CODE.value, [raw_text_node])
		return ParentNode(TagType.TAG_PRE.value, [code_node])
	elif block_type == BlockType.BLOCK_QUOTE:
		# strip off the '>' from the block.
		new_block = block_type.strategy(block)
		children = text_to_children(new_block)
		result = ParentNode(TagType.TAG_QUOTE.value, children)
	elif block_type == BlockType.BLOCK_UNORD_LIST:
		# strip off the '- ' from the block.
		new_block = block_type.strategy(block)
		li_nodes = []
		lines = new_block.split('\n')
		for line in lines:
			if line.strip() == "":
				continue
			item_children = text_to_children(line)
			li_nodes.append(ParentNode("li", item_children))
		result = ParentNode(TagType.TAG_UNORDERED_LIST.value, li_nodes)
	elif block_type == BlockType.BLOCK_ORD_LIST:
		# strip off the '<#>. ' from the block.		
		new_block = block_type.strategy(block)
		li_nodes = []
		lines = new_block.split('\n')
		for line in lines:
			if line.strip() == "":
				continue
			item_children = text_to_children(line)
			li_nodes.append(ParentNode("li", item_children))
		result = ParentNode(TagType.TAG_ORDERED_LIST.value, li_nodes)
	else:
		# must be BlockType.BLOCK_PARAGRAPH
		# new_block = text_node_to_html_node(block)
		children = text_to_children(block.replace('\n', ' '))
		result = ParentNode(TagType.TAG_PARAGRAPH.value, children)
	return result

def get_rid_of_hashtags(s: str, knt: int) -> str:
	return s[knt+1:]

def count_hashtags(s: str) -> int:
	result = 0
	for the_ch in s:
		if the_ch == '#':
			result += 1
		else:
			break
	return result
