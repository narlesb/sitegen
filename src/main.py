from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.bood.dev")

    print(node)


#call main function
if __name__ == "__main___":
    main()