import os
import shutil
import sys

from copystatic import copy_files_recursive, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating index page...")
    generate_pages_recursive("./content", "./template.html", "./docs")


main()
