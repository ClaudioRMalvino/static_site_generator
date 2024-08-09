import os
import shutil
import logging
from src.page_generator import generate_page, generate_pages_recursive
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
        logger.info(f"\n Removing existing public directory: {public_dir} \n")
        shutil.rmtree(public_dir)

    # Step 2: Copy all static files from static to public
    logger.info(f"\nCopying static files from {static_dir} to {public_dir} \n")
    copy_directory(static_dir, public_dir)

    # Step 3: Generate pages recursively from content directory
    logger.info(f"\nGenerating pages recursively from {content_dir} to {public_dir} \n")
    generate_pages_recursive(content_dir, template_path, public_dir)

    logger.info("\nStatic site generation complete \n")


if __name__ == "__main__":
    main()
