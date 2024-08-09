class TextNode:
    """
    Represents a node of text with associated type and optional URL.

    This class is used to store and manipulate text content, its type,
    and an optional URL for links or images.

    Attributes:
        text (str): The text content of the node.
        text_type (str): The type of text contained in the node (e.g., 'bold', 'italic', 'link').
        url (str, optional): The URL associated with the node, used for links or images.
    """

    def __init__(self, text, text_type, url=None):
        """
        Initialize a TextNode instance.

        Args:
            text (str): The text content of the node.
            text_type (str): The type of text contained in the node.
            url (str, optional): The URL associated with the node. Defaults to None.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compare this TextNode to another object for equality.

        Two TextNodes are considered equal if they have the same text, text_type, and url.

        Args:
            other (object): The object to compare with this TextNode.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        """
        Return a string representation of the TextNode.

        This method is useful for debugging and logging purposes.

        Returns:
            str: A string representation of the TextNode in the format
                 "TextNode(text, text_type, url)".
        """
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"
