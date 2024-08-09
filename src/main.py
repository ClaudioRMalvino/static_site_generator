import os
import shutil
import logging
from src.page_generator import generate_page
from src.copy_directory import copy_directory

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Define directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)  # Go up one level to reach static_site_generator
    static_dir = os.path.join(root_dir, "static")
    public_dir = os.path.join(root_dir, "public")
    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")

    # Step 1: Delete anything in the public directory
    if os.path.exists(public_dir):
        logger.info(f"Removing existing public directory: {public_dir}")
        shutil.rmtree(public_dir)

    # Step 2: Copy all static files from static to public
    logger.info(f"Copying static files from {static_dir} to {public_dir}")
    copy_directory(static_dir, public_dir)

    # Step 3: Generate page from content/index.md
    index_md_path = os.path.join(content_dir, "index.md")
    index_html_path = os.path.join(public_dir, "index.html")
    logger.info(f"Generating index page from {index_md_path} to {index_html_path}")
    generate_page(index_md_path, template_path, index_html_path)

    logger.info("Static site generation complete")

if __name__ == "__main__":
    main()
