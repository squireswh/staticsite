# main.py
#
# (c) 2026 Boot.dev
from textnode import TextType, TextNode
from nodehelp import extract_markdown_images, extract_markdown_links, split_nodes_delimiter

def main():
	# node = TextNode("text `code` text", TextType.TEXT_PLAIN)
	# out_list = split_nodes_delimiter([node], '`', TextType.TEXT_CODE)
	# print(out_list)
	# text = 'This is a text with a [Apple](https://www.apple.com)'
	# print(f"{text=}")
	# print(extract_markdown_images(text))
	matches = extract_markdown_links(
    	"![alt text](https://example.com/image.png)"
	)
	print(f"{matches=}")
	
if __name__ == "__main__":
	main()

