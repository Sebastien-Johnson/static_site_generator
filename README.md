# static_site_generator
Static site generator 
-Takes raw markdown text and transforms it into HTML for static site usage
-Sent to and hosted on python's built in HTTP server: 
-Architecture:
    -public/Holds html and css
    -static/Holds images and css
    -src/ Holds python code, the generator and fills public directory
        -content/ & template.html
    -File server (python3 -m http.server 8888) serves the public files so browser can access them
    -Browser: Renders html and css as webpage

-Flow:
    -Markdown files are in /content directory
    -template.html file is in root of project
    -src/ reads the markdown files and the template file
    -Generator in src/ comverts markdown files to final html file for each page and writes them to /public
    -Separately, the built in python server serves the contents of /public to out localy hosted website
    -Browser is viewable on: http://localhost:8888

-How it works:
    -Delete everything in /public
    -Cipy templates, images and css to /public
    -Generate and HTML file for each markdown file in /content
    -For each markdown file:
        -Open & read the file contents
        -Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
        -Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
            -Raw markdown -> TextNode -> HTMLNode
        -Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
        -Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
        -Write the full HTML string to a file for that page in the /public directory.

-TextNode: 
    -Takes raw text, text type and url, representing the different forms of 'inline' text
    -text (plain)
    -**Bold text**
    -_Italic text_
    -`Code text`
    -Links, in this format: [anchor text](url)
    -Images, in this format: ![alt text](url)

-Block level text: Headings, paragraphs and bullet lists

-Shell scripts:
    -main.sh: Runs main() file
    -test.sh: Runs all the test files