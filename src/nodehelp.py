# nodehelp.py
#
# (c) Boot.dev
import re
import typing
from textnode import TextType, TextNode
from handy import quote_it

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
	regex_text = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(regex_text, text)
	return matches
	
def extract_markdown_links(text: str) -> list[tuple[str, str]]:
	regex_text = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(regex_text, text)
	return matches

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
	# old_nodes: list[TextNode]
	# delimiter: string
	# text_type: TextType enum
	result = []
	for old_node in old_nodes:
		# old_node is a TextNode
		if old_node.text_type != TextType.TEXT_PLAIN:
			# Add it, as-is
			result.append(old_node)
		else:
			# split it with the delimiter
			plain_text = old_node.text
			# print(f"plain_text: {quote_it(plain_text)}")

			# crap: list[str]
			crap = plain_text.split(delimiter)

			# if the list has an even # elements, then we have a mismatched delimiter.
			if len(crap) % 2 == 0:
				raise Exception("invalid markdown syntax")

			# process the strings in 'crap'
			markdown = False
			for a_string in crap:
				if len(a_string) > 0:
					# valid
					if markdown:
						# we're currently processing an item within the matching delimiters
						if delimiter == '**':
							# bold
							new_node = TextNode(a_string, TextType.TEXT_BOLD)
						elif delimiter == '_':
							# italics
							new_node = TextNode(a_string, TextType.TEXT_ITALIC)
						elif delimiter == '`':
							# code
							new_node = TextNode(a_string, TextType.TEXT_CODE)
						else:
							# just in case...
							raise Exception(f"invalid markdown syntax: unrecognized delimiter: {delimiter}")

						# we just processed the delimited item, clear our flag.
						markdown = False
					else:
						# we're processing an item outside the delimiters
						new_node = TextNode(a_string, TextType.TEXT_PLAIN)

						# we just processed an regular text item; next one will be a delimited item.
						markdown = True
					result.append(new_node)
				else:
					# an item before a delimiter at the beginning, or an item after the delimiter
					# at the end. Just in case it's at the beginning, set the flag as if we had just
					# processed a plain text item.
					markdown = True
	return result

