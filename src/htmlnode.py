# htmlnode.py
#
# (c) Boot.dev, ClicKill Microbits
from enum import Enum
from handy import quote_it

class TagType(Enum):
	TAG_BOLD = "b"
	TAG_ITALICS = "i"
	TAG_SPAN = "span"
	TAG_IMAGE = "img"
	TAG_LINK = "a"
	TAG_PARAGRAPH = "p"
	TAG_HEAD = "head"
	TAG_HEADER1 = "h1"
	TAG_HEADER2 = "h2"
	TAG_HEADER3 = "h3"
	TAG_HEADER4 = "h4"
	TAG_HEADER5 = "h5"
	TAG_HEADER6 = "h6"
	TAG_BODY = "body"
	TAG_NAV = "nav"
	TAG_ARTICLE = "article"
	TAG_AUDIO = "audio"
	TAG_VIDEO = "video"
	TAG_ASIDE = "aside"
	TAG_FOOTER = "footer"
	TAG_MAIN = "main"
	TAG_SECTION = "section"
	TAG_ORDERED_LIST = "ol"
	TAG_UNORDERED_LIST = "ul"
	TAG_LIST_ITEM = "li"
	TAG_DETAILS = "details"
	TAG_SUMMARY = "summary"
	TAG_DIV = "div"
	TAG_FIGURE = "figure"
	TAG_FIGCAPTION = "figcaption"
	TAG_SOURCE = "source"
	TAG_CANVAS = "canvas"
	TAG_EMBED = "embed"
	TAG_CODE = "code"
	TAG_TRACK = "track"
	TAG_DATALIST = "datalist"
	TAG_METER = "meter"
	TAG_PROGRESSBAR = "progress"
	TAG_OUTPUT = "output"
	TAG_DIALOG = "dialog"
	TAG_MARK = "mark"
	TAG_TIME = "time"
	TAG_WBR = "wbr"

class HTMLNode:
	def __init__(self, new_tag=None, new_value=None, children=None, props=None):
		self.tag = new_tag
		self.value = new_value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		if not self.props:
			return ""
		html_str = ""
		for k, v in self.props.items():
			html_temp = f' {k}="{v}"'
			html_str += html_temp
		return html_str

	def __repr__(self):
		tag_tag = quote_it("")
		if not (self.tag is None):
			tag_tag = quote_it(self.tag)
		value_value = quote_it("")
		if not (self.value is None):
			value_value = quote_it(self.value)
		return f"{tag_tag}, {value_value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
	def __init__(self, new_tag, new_value, props=None):
		super().__init__(new_tag, new_value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError()
		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

	def __repr__(self):
		tag_tag = quote_it("")
		if not (self.tag is None):
			tag_tag = quote_it(self.tag)
		value_value = quote_it("")
		if not (self.value is None):
			value_value = quote_it(self.value)
		return f"{tag_tag}, {value_value}, {self.props}"

class ParentNode(HTMLNode):
	def __init__(self, new_tag, children, props=None):
		super().__init__(new_tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("missing tag")
		if self.children is None:
			raise ValueError("ParentNode must have children")
		result = f"<{self.tag}{self.props_to_html()}>"
		for child in self.children:
			result += child.to_html()
		result += f"</{self.tag}>"
		return result

	def __repr__(self):
		tag_tag = quote_it("")
		if not (self.tag is None):
			tag_tag = quote_it(self.tag)
		return f"{tag_tag}, {self.children}, {self.props}"

