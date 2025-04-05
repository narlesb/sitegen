from textnode import TextNode, TextType, split_nodes_delimiter

def main():
    # Create a TextNode with dummy values
    # For example, creating a link node
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the node to see its string representation
    print(node)

def text_delimiter():
    node = TextNode("This is a `delimiter` test", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    for new_node in new_nodes:
        print(f"Node Contet: {new_node.text}, node type: {new_node.text_type}")

# Call the main function
if __name__ == "__main__":
    main()
    text_delimiter()