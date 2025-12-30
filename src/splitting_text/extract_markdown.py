#takes raw markdwon texts and returns a lists of tuples with alt text and urls
import re


def extract_markdown_images(text): #raw markdown text
    images = []
    tup_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text) #creates list of (alt text : url) tuples
    for tup in tup_list: #iterates through list of tuples
        images.append(tup) #appends current tuple
    
    return images #list of (alt text : url) tuples

def extract_markdown_links(text): #raw markdown text
    links = []
    tup_list = re.findall(r"\[(.*?)\]\((.*?)\)", text) #creates list of (alt text : url) tuples

    for tup in tup_list: #iterates through list of tuples
        links.append(tup) #appends current tuple
    
    return links #list of (alt text : url) tuples