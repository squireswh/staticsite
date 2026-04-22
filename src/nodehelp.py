# nodehelp.py
#
# (c) Boot.dev
import re
import typing
from textnode import TextType, TextNode
from handy import quote_it

def markdown_to_blocks(markdown: str) -> list[str]:
	# result should be a list[str].
	result = markdown.split("\n\n")

	# strip whitespace
	result = [n.strip() for n in result if len(n)>0]

	return result

def text_to_textnodes(text: str) -> list[TextNode]:
	# the final list[TextNode]
	result = []

	# start by putting our input text into a plain TextNode.
	starter = TextNode(text, TextType.TEXT_PLAIN)
	# print(f"{starter=}")

	# split images 1st.
	result = split_nodes_image([starter])
	# print(f"{result=}\n")

	# then split links.
	result = split_nodes_link(result)
	# print(f"{result=}\n")

	# then code
	result = split_nodes_delimiter(result, '`', TextType.TEXT_PLAIN)
	# print(f"{result=}\n")

	# then bold
	result = split_nodes_delimiter(result, '**', TextType.TEXT_PLAIN)
	# print(f"{result=}\n")

	# then italic
	result = split_nodes_delimiter(result, '_', TextType.TEXT_PLAIN)	
	# print(f"{result=}\n")
	return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	# old_nodes: list[TextNode]
	result = []
	for old_node in old_nodes:
		# old_node is a TextNode
		if old_node.text_type != TextType.TEXT_PLAIN:
			# Add it, as-is
			result.append(old_node)
		else:
			# extract the images data from the old_node's .text property.
			# this is going to give us a list of 2-tuples.
			image_data = extract_markdown_images(old_node.text)

			# did we get any?
			if image_data == []:
				# no, leave it alone.
				result.append(old_node)
			else:
				# get the remaining text.
				remaining_text = old_node.text

				# process the image data tuples.
				for two_tuple in image_data:
					# 'two_tuple' now has two items, both of type 'str':
					# 1) the 'alt' text,
					# 2) the image URL
					alt_text = two_tuple[0]
					image_url = two_tuple[1]
					markdown = f"![{alt_text}]({image_url})"

					# split on the markdown.
					# note that we need the '1' here, or we might get more than a 2-tuple!
					before, after = remaining_text.split(markdown, 1)
					if before != "":
						# create a plain TextNode...
						a_text_node = TextNode(before, TextType.TEXT_PLAIN)

						# ...and shove it into the result, ...
						result.append(a_text_node)

					# ...and a TextNode for the image.
					an_image_node = TextNode(alt_text, TextType.TEXT_IMAGE, image_url)
					result.append(an_image_node)

					# if 'after' is the empty string, there's no trailing text to process.
					remaining_text = after

				# is there anything left?
				if remaining_text != "":
					# create a plain TextNode...
					a_text_node = TextNode(remaining_text, TextType.TEXT_PLAIN)

					# and append it.
					result.append(a_text_node)
	return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
	# old_nodes: list[TextNode]
	result = []
	for old_node in old_nodes:
		# old_node is a TextNode
		if old_node.text_type != TextType.TEXT_PLAIN:
			# Add it, as-is
			result.append(old_node)
		else:
			# extract the link data from the old_node's .text property.
			# this is going to give us a list of 2-tuples.
			link_data = extract_markdown_links(old_node.text)

			# did we get any?
			if link_data == []:
				# no, leave it alone.
				result.append(old_node)
			else:
				# get the remaining text.
				remaining_text = old_node.text

				# process the link data tuples.
				for two_tuple in link_data:
					# 'two_tuple' now has two items, both of type 'str':
					# 1) the link descriptor,
					# 2) the link URL
					desc_text = two_tuple[0]
					link_url = two_tuple[1]
					markdown = f"[{desc_text}]({link_url})"

					# split on the markdown.
					# note that we need the '1' here, or we might get more than a 2-tuple!
					before, after = remaining_text.split(markdown, 1)
					if before != "":
						# create a plain TextNode...
						a_text_node = TextNode(before, TextType.TEXT_PLAIN)

						# ...and shove it into the result, ...
						result.append(a_text_node)

					# ...and a TextNode for the link.
					a_link_node = TextNode(desc_text, TextType.TEXT_LINK, link_url)
					result.append(a_link_node)

					# if 'after' is the empty string, there's no trailing text to process.
					remaining_text = after

				# is there anything left?
				if remaining_text != "":
					# create a plain TextNode...
					a_text_node = TextNode(remaining_text, TextType.TEXT_PLAIN)

					# and append it.
					result.append(a_text_node)
	return result

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

