from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.textnode import TextNode
from src.markdown_blocks import markdown_to_blocks, block_to_block_type
from src.text_to_node import text_to_textnodes, text_node_to_leaf_node
import re

def block_to_html_node(block_type, block):
    """
    Converts a Markdown block of a specific type to an HTML node.

    Args:
        block_type (str): The type of the Markdown block (e.g., "paragraph", "heading", "code", "quote", "unordered_list", "ordered_list").
        block (str): The content of the Markdown block.

    Returns:
        HTMLNode: An HTMLNode instance representing the HTML structure of the Markdown block, or None if the block is empty.

    Raises:
        ValueError: If the block_type is invalid.
    """
    if not block.strip():
        return None
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    elif block_type == "heading":
        return heading_to_html_node(block)
    elif block_type == "code":
        return code_to_html_node(block)
    elif block_type == "quote":
        return quote_to_html_node(block)
    elif block_type == "unordered_list":
        return unordered_list_to_html_node(block)
    elif block_type == "ordered_list":
        return ordered_list_to_html_node(block)
    else:
        raise ValueError(f"Invalid block type: {block_type}")

def markdown_to_html_node(markdown):
    """
    Converts a Markdown document to an HTML node.

    Args:
        markdown (str): The Markdown content to be converted.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown document.
    """
    blocks = markdown_to_blocks(markdown)
    print(f"Number of blocks: {len(blocks)}")
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print(f"Block type: {block_type}")
        child = block_to_html_node(block_type, block)
        if child is not None:
            children.append(child)
    return ParentNode("div", children, None)

def text_to_children(text):
    """
    Converts a text string to a list of HTML nodes.

    Args:
        text (str): The text to be converted.

    Returns:
        List[HTMLNode]: A list of HTMLNode instances representing the HTML structure of the text.
    """
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_leaf_node(node) for node in text_nodes if node.text.strip()]
    return [node for node in html_nodes if node is not None]

def paragraph_to_html_node(block):
    """
    Converts a Markdown paragraph block to an HTML node.

    Args:
        block (str): The content of the Markdown paragraph block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown paragraph.
    """
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    """
    Converts a Markdown heading block to an HTML node.

    Args:
        block (str): The content of the Markdown heading block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown heading.
    """
    level = block.count("#")
    text = block[level:].strip()
    return ParentNode(f"h{level}", [LeafNode(value=text)])

def code_to_html_node(block):
    """
    Converts a Markdown code block to an HTML node.

    Args:
        block (str): The content of the Markdown code block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown code block.
    """
    code_content = block.strip().split("\n")[1:-1]  # Remove ``` lines
    code_text = "\n".join(code_content)
    return ParentNode("pre", [ParentNode("code", [LeafNode(value=code_text)])])

# def quote_to_html_node(block):
#     """
#     Converts a Markdown quote block to an HTML node.

#     Args:
#         block (str): The content of the Markdown quote block.

#     Returns:
#         ParentNode: A ParentNode instance representing the HTML structure of the Markdown quote.
#     """
#     lines = [line.strip()[2:] for line in block.split("\n")]  # Remove "> " from each line
#     return ParentNode("blockquote", text_to_children(" ".join(lines)))
def quote_to_html_node(block):
    """
    Converts a Markdown quote block to an HTML node.

    Args:
        block (str): The content of the Markdown quote block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown quote.
    """
    lines = [line.strip()[2:] for line in block.split("\n") if line.strip()]  # Remove "> " from each non-empty line
    return ParentNode("blockquote", [LeafNode(value=" ".join(lines))])

# def unordered_list_to_html_node(block):
#     """
#     Converts a Markdown unordered list block to an HTML node.

#     Args:
#         block (str): The content of the Markdown unordered list block.

#     Returns:
#         ParentNode: A ParentNode instance representing the HTML structure of the Markdown unordered list.
#     """
#     list_item_pattern = r"^\s*[-*]\s*(.+)$"
#     items = [match.group(1) for line in block.split("\n") if (match := re.match(list_item_pattern, line))]
#     li_nodes = [ParentNode("li", [LeafNode(value=item)]) for item in items]
#     return ParentNode("ul", li_nodes, None)
def unordered_list_to_html_node(block):
    """
    Converts a Markdown unordered list block to an HTML node.

    Args:
        block (str): The content of the Markdown unordered list block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown unordered list.
    """
    list_item_pattern = r"^\s*[-*]\s*(.+)$"
    items = [match.group(1) for line in block.split("\n") if (match := re.match(list_item_pattern, line))]
    li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ul", li_nodes, None)

def ordered_list_to_html_node(block):
    """
    Converts a Markdown ordered list block to an HTML node.

    Args:
        block (str): The content of the Markdown ordered list block.

    Returns:
        ParentNode: A ParentNode instance representing the HTML structure of the Markdown ordered list.
    """
    list_item_pattern = r"^\s*\d+\.\s*(.+)$"
    items = [match.group(1) for line in block.split("\n") if (match := re.match(list_item_pattern, line))]
    li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ol", li_nodes, None)
