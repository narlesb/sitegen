import re
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:

        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
            original_text = old_node.text
            images = extract_markdown_images(original_text)
            if len(images) == 0:
                new_nodes.append(old_node)
                continue
            for image in images:
                sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(
                    TextNode(
                        image[0],
                        TextType.IMAGE,
                        image[1],
                    )
                )
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Find all occurrences of the delimiter pairs
        text = old_node.text
        remaining_text = text
        
        while delimiter in remaining_text:
            start_index = remaining_text.find(delimiter)
            if start_index == -1:
                break
                
            # Add text before the delimiter as TEXT
            if start_index > 0:
                new_nodes.append(TextNode(remaining_text[:start_index], TextType.TEXT))
                
            # Find the closing delimiter
            content_start = start_index + len(delimiter)
            end_index = remaining_text.find(delimiter, content_start)
            if end_index == -1:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {text}")
                
            # Add the content between delimiters with the specified text_type
            content = remaining_text[content_start:end_index]
            new_nodes.append(TextNode(content, text_type))
                
            # Update remaining_text for the next iteration
            remaining_text = remaining_text[end_index + len(delimiter):]
        
        # Add any remaining text as TEXT
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes