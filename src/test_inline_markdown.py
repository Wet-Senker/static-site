import unittest
from inline_markdown import (
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from textnode import TextNode, TextType

class TestSplitNodesImages(unittest.TestCase):
    def test_extract_one_link(self):
        node = TextNode("This is text with an image ![funny cat](https://www.boot.dev)", TextType.TEXT)
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("funny cat", TextType.IMAGE, "https://www.boot.dev"),
        ],
            new_node)

class TestSplitNodesLinks(unittest.TestCase):
    def test_extract_one_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ],
            new_node)

    def test_extract_two_links(self):
        node = TextNode(
        "This is text with a [link](https://www.boot.dev.com) and another [second link](https://www.brugnieuws.nl)!",
        TextType.TEXT,
    )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://www.brugnieuws.nl"
            ),
            TextNode("!", TextType.TEXT),
        ],
        new_nodes,
    )

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [linkname](https://brugnieuws.nl)"
        )
        self.assertListEqual([("linkname", "https://brugnieuws.nl")], matches)
    
    def test_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is a text with two images. The first one is ![image1](https://image1.png), the second one is ![image2](https://image2.png)"
        )
        self.assertListEqual([("image1", "https://image1.png"), ("image2", "https://image2.png")], matches)

    def test_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with two links. The first one is [link1](https://site1.com), the second one is [link2](https://site2.com)"
        )
        self.assertListEqual([("link1", "https://site1.com"), ("link2", "https://site2.com")], matches)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
