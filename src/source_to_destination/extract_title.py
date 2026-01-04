def extract_title(markdown):
    if markdown.startswith("#"):
        lines = markdown.split("\n")
        return lines[0].lstrip("#").strip() 
    else:
        raise ValueError("invalid title format")