import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_grand_grandchildren(self):
        grand_grandchild_node = LeafNode("b", "hello")
        grandchild_node = ParentNode("p", [grand_grandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("body", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<body><div><p><b>hello</b></p></div></body>"
        )
    
    def test_no_tag(self):
        child_node = LeafNode("b")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
            self.assertEqual(str(context.exception),
            "ParentNode must have a tag."
        )

if __name__ == "__main__":
    unittest.main()