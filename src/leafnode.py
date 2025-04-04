from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)


    def to_html(self):
        #check if value is empty or None
        if self.value is None or self.value == "":
            raise ValueError("LeafNode must have a value!")
        
        #check for tag else return plain text
        if self.tag is None:
            return self.value
        


        #return properly tagged html
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"