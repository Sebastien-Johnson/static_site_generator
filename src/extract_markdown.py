import re

def extract_markdown_images(text):
    matched_text = re.findall(r"\[.*?]\]")
    matched_image = re.findall(r"\(.*?)\)")
    length = len(matched_text)

    images = []

    for i in range(length):
        images.append((matched_text[i], matched_image[i]))

    return images

def extract_markdown_links(text):
    matched_text = re.findall(r"\[.*?]\]")
    matched_link = re.findall(r"\(.*?)\)")
    length = len(matched_text)

    link = []

    for i in range(length):
        link.append((matched_text[i], matched_link[i]))

    return link
