from src.textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter: str, text_type):
    """
    Splits TextNode objects based on a delimiter.

    Args:
        old_nodes (list): List of TextNode objects.
        delimiter (str): The delimiter to split on.
        text_type (str): The type to assign to the new split nodes.

    Returns:
        list: New list of TextNode objects after splitting.
    """
    new_nodes = []
    delimiters_dict = {"**": "bold", "*": "italic", "`": "code"}
    if delimiter not in delimiters_dict:
        raise Exception("Invalid Markdown syntax utilized as delimiter.")

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        for i, text in enumerate(parts):
            if text:
                if text == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(text=text, text_type="text"))
                else:
                    new_nodes.append(TextNode(text=text, text_type=text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    """
    Splits TextNodes containing image markdown syntax.

    Args:
        old_nodes (list): List of TextNode objects.

    Returns:
        list: New list of TextNode objects with image markdown split into separate nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        parts = node.text.split("![")
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        current_text = parts[0]
        for part in parts[1:]:
            if "](" not in part or ")" not in part.split("](")[1]:
                current_text += "![" + part
                continue

            if current_text:
                new_nodes.append(TextNode(current_text, "text"))
                current_text = ""

            image_text, remainder = part.split("](", 1)
            image_url, rest = remainder.split(")", 1)
            new_nodes.append(TextNode(image_text, "image", image_url))
            current_text = rest

        if current_text:
            new_nodes.append(TextNode(current_text, "text"))

    return new_nodes


def split_nodes_link(old_nodes):
    """
    Splits TextNodes containing link markdown syntax.

    Args:
        old_nodes (list): List of TextNode objects.

    Returns:
        list: New list of TextNode objects with link markdown split into separate nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        current_text = ""
        remaining_text = node.text

        while "[" in remaining_text:
            parts = remaining_text.split("[", 1)
            current_text += parts[0]
            remaining_text = "[" + parts[1]

            if remaining_text.startswith("[!"):  # This is an image, not a link
                image_end = (
                    remaining_text.find(")") + 1
                    if ")" in remaining_text
                    else len(remaining_text)
                )
                current_text += remaining_text[:image_end]
                remaining_text = remaining_text[image_end:]
                continue

            if "](" not in remaining_text:
                current_text += remaining_text
                remaining_text = ""
                break

            link_text, remainder = remaining_text[1:].split("](", 1)
            if ")" not in remainder:
                current_text += remaining_text
                remaining_text = ""
                break

            url, rest = remainder.split(")", 1)

            if current_text:
                new_nodes.append(TextNode(current_text, "text"))
                current_text = ""

            new_nodes.append(TextNode(link_text, "link", url))
            remaining_text = rest

        if current_text or remaining_text:
            new_nodes.append(TextNode(current_text + remaining_text, "text"))

    return new_nodes
