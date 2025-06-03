import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
        node = TextNode("This is a node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal(self):
        node = TextNode("This is a node", TextType.BOLD, "www.brugnieuws.nl")
        node2 = TextNode("This is a node", TextType.BOLD, "www.brugnieuws.nl/agenda")
        self.assertNotEqual(node, node2)
    
    def test_url_equal(self):
        node1 = TextNode("text", TextType.LINK, "https://example.com")
        node2 = TextNode("text", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)
    
    def test_url_none_vs_empty_string(self):
        node1 = TextNode("text", TextType.LINK, None)
        node2 = TextNode("text", TextType.LINK, "")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
