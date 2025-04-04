from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        #check if tag is empty
        if self.tag is None or self.tag == "":
            raise ValueError("Requires a tag")

        #check if children is empty
        if self.children is None or self.children == "":
            raise ValueError("children values must be included")


        #else return string of html tag of node and children
        #create opening tag
        props_str = self.props_to_html()
        opening_tag = f"<{self.tag}{props_str}>"
        closing_tag = f"</{self.tag}>"

        #process children loop
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        #retunr string
        return f"{opening_tag}{children_html}{closing_tag}"

