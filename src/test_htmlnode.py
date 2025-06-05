import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_tag(self):
        node = HTMLNode("p", "Hoi alles goed?", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "Hoi alles goed?", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("p", "Doei alles goed?", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "Hoi alles goed?", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    
    def test_different_tag(self):
        node = HTMLNode("a", "Doei alles goed?", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "Doei alles goed?", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal(self):
        node = HTMLNode("p", "Doei alles goed?", None, {"href": "https://www.brugnieuws.com"})
        node2 = HTMLNode("p", "Doei alles goed?", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
