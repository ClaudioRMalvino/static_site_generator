import re


def markdown_to_blocks(markdown):
    """
    Converts markdown content into a list of block strings.

    Args:
        markdown (str): The markdown content.

    Returns:
        list: List of markdown blocks as strings.
    """
    # Split the markdown into blocks based on blank lines
    blocks = re.split(r"\n{2,}", markdown)

    processed_blocks = []
    for block in blocks:
        # Strip leading/trailing whitespace
        block = block.strip()

        if block:
            # Preserve indentation for code blocks
            if block.startswith("```"):
                lines = block.split("\n")
                # Preserve original indentation for code block content
                processed_block = "\n".join(
                    [lines[0]] + [line.rstrip() for line in lines[1:]]
                )
            else:
                # For non-code blocks, remove extra indentation
                lines = block.split("\n")
                processed_block = "\n".join(
                    [lines[0]] + [line.strip() for line in lines[1:]]
                )

            processed_blocks.append(processed_block)

    return processed_blocks

import re

def block_to_block_type(block):
    """
    Determines the type of a markdown block.

    Args:
        block (str): A single block of markdown text.

    Returns:
        str: The type of the block ('paragraph', 'heading', 'code', etc.).
    """
    # Check for heading
    if re.match(r'^#{1,6}\s', block):
        return "heading"

    # Check for code block
    if block.startswith('```') and block.endswith('```'):
        return "code"

    # Check for quote
    if all(line.strip().startswith('>') for line in block.split('\n')):
        return "quote"

    # Check for unordered list
    if all(line.strip().startswith(('* ', '- ')) for line in block.split('\n') if line.strip()):
        return "unordered_list"

    # Check for ordered list
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    if all(re.match(r'^\d+\.\s', line) for line in lines):
        numbers = [int(line.split('.')[0]) for line in lines]
        if numbers == list(range(1, len(numbers) + 1)):
            return "ordered_list"

    # If none of the above, it's a paragraph
    return "paragraph"
