class TextNode:

    def __init__(
        self,
        text,
        text_type,
        url=None,
    ):
        # Text content of the node
        self.text = text
        # Type of text contained in the node
        self.text_type = text_type
        # URL of link or image
        self.url = url

    def __eq__(self, target):
        """
        Method returns True if all of the properties of two
        TextNode objects are equal, false otherwise.
        """
        if (
            (self.text == target.text)
            and (self.text_type == target.text_type)
            and (self.url == target.url)
        ):
            return True
        else:
            return False

    def __repr__(self):
        """
        Method prints a string representation of the TextNode
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
