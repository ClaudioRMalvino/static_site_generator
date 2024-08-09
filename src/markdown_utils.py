import re


def extract_markdown_images(text):
    """
    Extracts all markdown-style image references from the given text.

    This function uses a regular expression to find all occurrences of
    markdown image references in the format ![alt text](image URL) within the input text.

    Args:
        text (str): The input text containing markdown-style image references.

    Returns:
        list of tuples: A list where each tuple contains two elements:
            - The alt text (str): The alternative text for the image
            - The image URL (str): The URL or path to the image
        If no image references are found, an empty list is returned.
    """
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """
      Extracts all markdown-style links from the given text.

      This function uses a regular expression to find all occurrences of
      markdown links in the format [link text](URL) within the input text.

      Args:
          text (str): The input text containing markdown-style links.

      Returns:
          list of tuples: A list where each tuple contains two elements:
              - The link text (str)
              - The URL (str)
          If no links are found, an empty list is returned.
    """
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_title(markdown):
    """
    Extracts the title (h1 header) from a markdown string.

    Args:
    markdown (str): The markdown content.

    Returns:
    str: The extracted title.

    Raises:
    ValueError: If no h1 header is found in the markdown.
    """
    lines = markdown.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()
    raise ValueError("No h1 header found in the markdown")
