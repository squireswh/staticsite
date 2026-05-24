# main.py
#
# (c) 2026 Boot.dev
from markhtml import markdown_to_html_node

def main():
	markdown = "# header 1\n\n"
	markdown += "## header 2\n\n"
	markdown += "```\n# python comment\n```"
	markdown += "> A happy quote\n\n"
	markdown += "- Unordered list item 1\n- Unordered list item 2\n\n"
	markdown += "1. Ordered list item 1\n2. Ordered list item 2\n3. Ordered list item 3\n\n"
	markdown += "An ordinary paragraph. With two sentences.\n\n"
	markdown_to_html_node(markdown)

if __name__ == "__main__":
	main()

