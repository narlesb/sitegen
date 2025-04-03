import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"href": "https://test.com", "target": "_blank"})
        assert node.props_to_html() == ' href="https://test.com" target="_blank"'