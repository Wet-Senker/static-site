from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text: str, text_type: TextType, url: str | None = None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if not isinstance(other, TextNode):
			return False
		return (
			self.text == other.text and
			self.text_type == other.text_type and	
			self.url == other.url
			)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == TextType.LINK:
        return LeafNode(value=text_node.text, tag="a", props={'href': text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})