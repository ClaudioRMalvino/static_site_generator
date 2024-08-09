from src.textnode import TextNode
from src.split_node import split_nodes_image, split_nodes_link, split_nodes_delimiter
from src.htmlnode import LeafNode, HTMLNode,ParentNode


def text_to_textnodes(text):
    """
    Converts raw text to a list of TextNode objects.

    Args:
        text (str): The input text.

    Returns:
        list: List of TextNode objects.
    """
    nodes = [TextNode(text, "text")]

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "**", "bold")

    nodes = split_nodes_delimiter(nodes, "*", "italic")

    nodes = split_nodes_delimiter(nodes, "`", "code")

    nodes = [node for node in nodes if node.text.strip() != ""]

    return nodes

def text_node_to_leaf_node(text_node):
    """
    Converts a TextNode object into an HTML LeafNode.
    Args:
        text_node (TextNode): The TextNode to convert.
    Returns:
        LeafNode: The converted HTML LeafNode.
    Raises:
        Exception: If an unknown text type is encountered.
    """
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.text_type == "italic":
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.text_type == "code":
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == "link":
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(
            value="", tag="img", props={"src": text_node.url, "alt": text_node.text}
        )
    elif text_node.text_type == "unordered_list":
        return LeafNode(value=text_node.text, tag="li")
    elif text_node.text_type == "ordered_list":
        return LeafNode(value=text_node.text, tag="li")
    else:
        raise Exception(f"Unknown text type: {text_node.text_type}")

def text_node_to_html_node(text_node):
    """
    Converts a TextNode object into an HTMLNode.

    Args:
        text_node (TextNode): The TextNode to convert.

    Returns:
        HTMLNode: The converted HTMLNode.

    Raises:
        ValueError: If an unknown text type is encountered.
    """
    if text_node.text_type == "text":
        return HTMLNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return ParentNode("b", [HTMLNode(None, text_node.text)])
    elif text_node.text_type == "italic":
        return ParentNode("i", [HTMLNode(None, text_node.text)])
    elif text_node.text_type == "code":
        return ParentNode("code", [HTMLNode(None, text_node.text)])
    elif text_node.text_type == "link":
        return ParentNode("a", [HTMLNode(None, text_node.text)], {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")
