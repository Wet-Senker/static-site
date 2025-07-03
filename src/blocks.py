from textnode import TextNode, TextType
from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph" 
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown):
   if markdown.startswith("#"):
       return BlockType.HEADING
   elif markdown.startswith("`"):
        return BlockType.CODE
   elif markdown.startswith(">"):
        return BlockType.QUOTE
   elif markdown.startswith("-"):
        return BlockType.UNORDERED_LIST
   elif markdown.startswith(r"\d+\."):
        return BlockType.ORDERED_LIST 
   else:
       return BlockType.PARAGRAPH