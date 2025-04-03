from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, prop, value):
        super().__init(tag, prop, value)

    def to_html(self):
        #check if value is empty or None
        if self.value is None or self.value == "":
            raise ValueError("LeafNode must have a value!")
        
        #check for tag else return plain text
        if self.tag is None:
            return self.value
        


        #return properly tagged html
        props = ""
        if self.prop:
            props = " ".join(f'{key}="{value}"' for key, value in self.prop.items())
            return f"<{self.tag} {props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")