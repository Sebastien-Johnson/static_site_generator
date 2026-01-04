import shutil
import os
from src.markdown_html import markdown_to_html
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")
    md_file = from_path.read()
    templpate_file = template_path.read()
    html_text = markdown_to_html(md_file).to_html()
    title = extract_title(md_file)

    template_path.replace("{{ Title }}", title, count = 1)
    template_path.replace("{{ Content }}", html_text, count = 1)
    #check if directory exists
    os.mkdir(dest_path)
    shutil.copy(template_path, dest_path)