import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_tag(self):
        node = HTMLNode("<p>", "Hello")
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_url_equal(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
