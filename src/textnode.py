from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        # First check if 'other' is also a TextNode
        if not isinstance(other, TextNode):
            return False
    
     # Compare all properties
        return (
        self.text == other.text and
        self.text_type == other.text_type and
        self.url == other.url
        )
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
        
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    else:
        raise Exception ("Type not supported")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:

        if node.text_type == TextType.TEXT:
            if node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
            
            split_lists = node.text.split(delimiter)
            index = 0
            for part in split_lists:
                if index % 2 == 0: #even index plain text
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else: #odd delimiter text
                    new_nodes.append(TextNode(part, text_type))
                index += 1
        else:
            new_nodes.append(node)

    return new_nodes
               
            
            

