import os
import shutil
import logging

def copy_directory(src, dst):
    """
    Recursively copy contents from source directory to destination directory.

    This function will:
    1. Check if the source directory exists.
    2. Remove the destination directory if it already exists.
    3. Create a new destination directory.
    4. Copy all files and subdirectories from source to destination.

    Args:
        src (str): Path to the source directory.
        dst (str): Path to the destination directory.

    Returns:
        None

    Raises:
        OSError: If there are issues with file operations.

    Logs:
        INFO: Directory creation, file copying, and directory copying operations.
        ERROR: If the source directory does not exist.
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Check if source directory exists
    if not os.path.exists(src):
        logger.error(f"Source directory does not exist: {src}")
        return

    # Delete destination directory if it exists
    if os.path.exists(dst):
        logger.info(f"Removing existing directory: {dst}")
        shutil.rmtree(dst)

    # Create destination directory
    logger.info(f"Creating directory: {dst}")
    os.makedirs(dst)

    # Walk through source directory
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        if os.path.isfile(s):
            logger.info(f"Copying file: {s} to {d}")
            shutil.copy2(s, d)
        elif os.path.isdir(s):
            logger.info(f"Copying directory: {s} to {d}")
            copy_directory(s, d)
