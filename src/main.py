import sys
from source_to_destination.static_to_public import clear_dir
from source_to_destination.generate_page import generate_pages_recursive


def main():
    basepath = ""
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    source_dir = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/content"
    dest_dir = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/docs"
    clear_dir(source_dir, dest_dir)
    generate_pages_recursive(
        source_dir,
        "template.html",
        dest_dir,
        basepath
    )

main()



