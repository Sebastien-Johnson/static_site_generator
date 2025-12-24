#takes raw markdwon texts and returns a lists of tuples with alt text and urls
import re


def extract_markdown_images(text):
    images = []
    tup_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    for tup in tup_list:
        images.append(tup)
    
    return images

def extract_markdown_links(text):
    links = []
    tup_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    for tup in tup_list:
        links.append(tup)
    
    return links