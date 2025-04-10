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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        full_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(full_path):
            if entry.endswith(".md"):
                print(f"Processing markdown file: {full_path}")
                dest_html_path = os.path.splitext(dest_path)[0] + ".html"
                generate_page(full_path, template_path, dest_html_path)
        
        elif os.path.isdir(full_path):
            print(f"Entering directory:{full_path}")
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)

            generate_pages_recursive(full_path, template_path, dest_path)
