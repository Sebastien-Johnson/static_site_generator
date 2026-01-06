import shutil
import os
from markdown_html.markdown_to_html import markdown_to_html_node
from .extract_title import extract_title

#accepts string paths as vars
#from_path leads to markdown file
#template_path is html template
#dest_path is path to FILE in public directory
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r", encoding="utf-8")
    md_text = from_file.read()
    from_file.close()

    template_file = open(template_path, "r", encoding="utf-8")
    template = template_file.read()
    template_file.close()
    
    html = markdown_to_html_node(md_text).to_html()

    #fill tempplate with title and html content
    title = extract_title(md_text)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')


    
    dest_dir_path = os.path.dirname(dest_path)
    #check if directory exists
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w", encoding="utf-8")
    to_file.write(template)
    

#dir_path_content = content source directory
    #generate new html file for each md file found
#template_path = template directory
#dest_dir_path = where pages are to be generated
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_pages = os.listdir(dir_path_content) 
    #creates list of items in source directory

    for page in content_pages:
        new_content_path = os.path.join(dir_path_content, page)
        new_dest_dir = os.path.join(dest_dir_path, page)
        html_page = page.replace(".md", ".html")
        new_dest_file = os.path.join(dest_dir_path, html_page)
        if os.path.isfile(new_content_path):
            if new_dest_file[-3:] != ".md":
                continue
            #(markdown file, template, destination directory)
            generate_page(new_content_path, template_path, new_dest_file, basepath)
        else:
            #is directory
            #os.mkdir(new_dest_path)
            generate_pages_recursive(new_content_path, template_path, new_dest_dir, basepath)
    
    return