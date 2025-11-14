import os
import shutil
import logging
from src.page_generator import generate_page, generate_pages_recursive
from src.copy_directory import copy_directory

def main():
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)  
    static_dir = os.path.join(root_dir, "static")
    public_dir = os.path.join(root_dir, "public")
    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")

    
    if os.path.exists(public_dir):
        logger.info(f"\n Removing existing public directory: {public_dir} \n")
        shutil.rmtree(public_dir)

    
    logger.info(f"\nCopying static files from {static_dir} to {public_dir} \n")
    copy_directory(static_dir, public_dir)

    
    logger.info(f"\nGenerating pages recursively from {content_dir} to {public_dir} \n")
    generate_pages_recursive(content_dir, template_path, public_dir)

    logger.info("\nStatic site generation complete \n")


if __name__ == "__main__":
    main()
