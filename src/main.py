import sys
from source_to_destination.static_to_public import clear_dir
from source_to_destination.generate_page import generate_pages_recursive


def main():
    basepath = ""
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    content_source_dir = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/content"
    static_source_dir = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/static"
    dest_dir = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/docs"
    clear_dir(static_source_dir, dest_dir)

    generate_pages_recursive(
        content_source_dir,
        "template.html",
        dest_dir,
        basepath
    )

main()



