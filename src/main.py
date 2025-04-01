from textnode import TextNode, TextType

def main():
    # Create a TextNode with dummy values
    # For example, creating a link node
    node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    
    # Print the node to see its string representation
    print(node)

# Call the main function
if __name__ == "__main__":
    main()