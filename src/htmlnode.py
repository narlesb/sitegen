class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
           return ""
    
        # Create a list of formatted attribute strings
        formatted_props = []
        for key, value in self.props.items():
            # Format each pair as key="value" and add to the list
            formatted_props.append(f'{key}="{value}"')
    
        # Join the formatted props with spaces and add a leading space
        return " " + " ".join(formatted_props)

    #print html object
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
       
        
