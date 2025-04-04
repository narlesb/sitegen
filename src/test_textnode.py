import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Link test", TextType.LINK, "https://example.com")
        node2 = TextNode("Link test", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)
    
    def text_dif_url(self):
        node = TextNode("Link test", TextType.LINK, "https://example.com")
        node2 = TextNode("Link test", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("First text", TextType.BOLD)
        node2 = TextNode("Second text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    def test_not_equal_url_vs_none(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, None)
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()