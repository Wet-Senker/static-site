import unittest
from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)
class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlock(unittest.TestCase):
    def test_header_to_block(self):
        result = block_to_block_type("# This is a header")
        self.assertEqual(result, BlockType.HEADING)
    
    def test_second_header_to_block(self):
        result = block_to_block_type("## This is a header")
        self.assertEqual(result, BlockType.HEADING)
    
    def test_code_to_block(self):
        result = block_to_block_type("`print(hoi)`")
        self.assertEqual(result, BlockType.CODE)
    
    def test_quote_to_block(self):
        result = block_to_block_type("> E=mc2")
        self.assertEqual(result, BlockType.QUOTE)
