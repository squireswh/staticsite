# main.py
#
# (c) 2026 Boot.dev
from htmlnode import HTMLNode, LeafNode

def main():
	htmlleaf = LeafNode("img", "", {"src": "cat.png", "alt": "A cat"})
	print(f"{htmlleaf}")

if __name__ == "__main__":
	main()

