import shutil
from core.markdown_processor import process_posts
from core.index_generator import *
from core.copy_static import copy_static_files

STATIC_DIR = "static/"
INPUT_DIR = "content/posts/"
OUTPUT_DIR = "docs/posts/"
INDEX_OUTPUT_PATH = "docs/index.html"
TEMPLATE_PATH = "html/post_base.html"

def main():
    shutil.rmtree('docs/', ignore_errors=True)

    print("Copying static files...")
    try:
        copy_static_files(STATIC_DIR, "docs/")
    except Exception as e:
        print(f"Erro: {e}")

    print("Processing markdown files...")
    posts = process_posts(INPUT_DIR, OUTPUT_DIR, TEMPLATE_PATH)

    print("Generating index.html...")
    generate_page("Home", md_to_html(load_html("content/index.md")), posts, "docs/index.html")

    print("Generating about.html...")
    generate_page("About", md_to_html(load_html("content/about.md")), posts, "docs/about.html")

    print("Generating projects.html...")
    generate_page("Projects", md_to_html(load_html("content/projects.md")), posts, "docs/projects.html")
    
    print("Generating posts.html...")
    blog_posts_html = "\n".join(
        f'<p>{post.post_date.strftime("%Y-%m-%d %H:%M")}<p><a href="posts/{os.path.splitext(post.filename)[0]}.html">{post.title}</a>'
        for post in posts
        if not post.filename.startswith('_')
    )

    generate_page("Posts", blog_posts_html, posts, "docs/posts.html")

    for post in posts:
        generate_page(post.title, post.html_content, posts, "docs/posts/" + post.filename.replace(".md", ".html"))
    print("Done!")

if __name__ == "__main__":
    main()
