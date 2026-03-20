# main.py
#
# (c) 2026 Boot.dev
from textnode import TextType, TextNode

def main():
	new_node = TextNode("This is some anchor text", TextType.TEXT_LINK, "https://www.boot.dev")
	print(new_node)

if __name__ == "__main__":
	main()

