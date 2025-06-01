import os
import markdown

def load_html(input):
    # Load the content of the index.html template file
    if not os.path.exists(input):
        raise FileNotFoundError(f"Template {input} not found.")
    
    with open(input, 'r', encoding='utf-8') as template_file:
        return template_file.read()

def md_to_html(input):
    html = markdown.markdown(input)
    return html

def generate_page(title, content, posts, output_path):
    index_template = load_html("html/index.html")
    index_template = index_template.replace("{{ title }}", title)

    sidebar_left = load_html("html/sidebar_left.html")
    sidebar_right = load_html("html/sidebar_right.html")
    sidebar_right = sidebar_right.replace("{{ posts-1 }}", posts[0].title)
    sidebar_right = sidebar_right.replace("{{ posts-2 }}", posts[1].title)
    sidebar_right = sidebar_right.replace("{{ posts-3 }}", posts[2].title)

    index_template = index_template.replace("{{ sidebar_left }}", sidebar_left)
    
    if(title != "lucasof"):
        content =  "<h1>" + title + "</h1>" + content

    index_template = index_template.replace("{{ content }}", content)
    index_template = index_template.replace("{{ sidebar_right }}", sidebar_right)

    footer = open("html/footer.html", "r")
    index_template = index_template.replace("{{ footer }}", footer.read())

    final_url = ""
    nested_count = output_path.count('/') - 1
    for i in range(nested_count):
        final_url = final_url + "../"

    index_template = index_template.replace("{{ rootdir }}", final_url)
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the generated content to the index.html file in the build/ directory
    with open(output_path, 'w', encoding='utf-8') as index_file:
        index_file.write(index_template)
