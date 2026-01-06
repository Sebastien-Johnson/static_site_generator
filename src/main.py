from source_to_destination.static_to_public import clear_dir
from source_to_destination.generate_page import generate_pages_recursive

def main():
    clear_dir()
    generate_pages_recursive(
        "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/content",
        "template.html",
        "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/public"
    )
main()