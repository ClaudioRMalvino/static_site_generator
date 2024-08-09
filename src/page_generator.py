import os
from src.markdown_to_html import markdown_to_html_node
from src.markdown_utils import extract_title

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the source markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Path where the generated HTML file will be saved.
    """
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path} \n")

    # Read the markdown file
    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()

    # Read the template file
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html() if html_node else ""

    # Extract the title
    try:
        title = extract_title(markdown_content)
    except ValueError:
        title = "Untitled"  # Fallback title if no h1 is found

    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the full HTML to the destination file
    with open(dest_path, 'w') as dest_file:
        dest_file.write(full_html)

    print(f"\nPage generated successfully: {dest_path} \n")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates HTML pages from markdown files in a directory.

    Args:
        dir_path_content (str): Path to the content directory.
        template_path (str): Path to the HTML template file.
        dest_dir_path (str): Path to the destination directory for generated HTML files.
    """
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                # Construct paths
                md_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_file_path, dir_path_content)
                html_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')

                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(html_file_path), exist_ok=True)

                # Generate the HTML page
                generate_page(md_file_path, template_path, html_file_path)

    print(f"\nPages generated recursively from {dir_path_content} to {dest_dir_path} \n")
