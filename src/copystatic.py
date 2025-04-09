import os
import shutil
from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    lines = markdown.split('\n')
    for i in lines:
        if i.startswith("#"):
            return i[1:].strip()
    
    raise Exception ("No header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #read markdown and create variable
    markdown = open(from_path)
    r_markdown = markdown.read()
    markdown.close()
    
    #read templace and create variable
    template = open(template_path)
    r_template = template.read()
    template.close()
    
    #convert markdown to html
    converted_markdown = markdown_to_html_node(r_markdown)
    html_markdown = converted_markdown.to_html()
    
    #extract title
    title = extract_title(r_markdown)
    
    #replace placeholders
    result = r_template.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", html_markdown)

    #ensure directtory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    #write to file
    with open(dest_path, "w") as f:
        f.write(result)

    