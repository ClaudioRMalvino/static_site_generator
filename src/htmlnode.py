class HTMLNode:
    """
    Base class for HTML nodes.

    Attributes:
        tag (str): The HTML tag for the node.
        value (str): The value/content of the node.
        children (list): Child nodes of this node.
        props (dict): Properties/attributes of the node.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initialize an HTMLNode.

        Args:
            tag (str, optional): The HTML tag for the node.
            value (str, optional): The value/content of the node.
            children (list, optional): Child nodes of this node.
            props (dict, optional): Properties/attributes of the node.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Convert the node to HTML string representation.

        Raises:
            NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError

    def props_to_html(self):
        """
        Convert node properties to HTML attribute string.

        Returns:
            str: HTML attribute string.
        """
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __eq__(self, other):
        """
        Check if this node is equal to another node.

        Args:
            other (HTMLNode): Another HTMLNode to compare with.

        Returns:
            bool: True if nodes are equal, False otherwise.
        """
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        """
        Return a string representation of the node.

        Returns:
            str: String representation of the node.
        """
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"


class LeafNode(HTMLNode):
    """
    Represents a leaf node in the HTML tree (a node with no children).

    Attributes:
        value (str): The content of the leaf node.
        tag (str): The HTML tag for the node.
        props (dict): Properties/attributes of the node.
    """

    def __init__(self, value, tag=None, props=None):
        """
        Initialize a LeafNode.

        Args:
            value (str): The content of the leaf node.
            tag (str, optional): The HTML tag for the node.
            props (dict, optional): Properties/attributes of the node.

        Raises:
            ValueError: If value is None.
        """
        if value is None:
            raise ValueError("Leaf nodes must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """
        Convert the leaf node to HTML string representation.

        Returns:
            str: HTML string representation of the leaf node.

        Raises:
            ValueError: If value is None.
        """
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        """
        Return a string representation of the leaf node.

        Returns:
            str: String representation of the leaf node.
        """
        return f"LeafNode(value={self.value!r}, tag={self.tag!r}, props={self.props!r})"

    def __eq__(self, other):
        """
        Check if this leaf node is equal to another leaf node.

        Args:
            other (LeafNode): Another LeafNode to compare with.

        Returns:
            bool: True if leaf nodes are equal, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        return (
            self.value == other.value
            and self.tag == other.tag
            and self.props == other.props
        )

    def debug(self):
        """
        Return detailed information about the leaf node instance.

        Returns:
            str: Detailed string representation of the leaf node.
        """
        return f"LeafNode(value={self.value!r}, tag={self.tag!r}, props={self.props!r})"


class ParentNode(HTMLNode):
    """
    Represents a parent node in the HTML tree (a node with children).

    Attributes:
        tag (str): The HTML tag for the node.
        children (list): Child nodes of this node.
        props (dict): Properties/attributes of the node.
    """

    def __init__(self, tag, children, props=None):
        """
        Initialize a ParentNode.

        Args:
            tag (str): The HTML tag for the node.
            children (list): Child nodes of this node.
            props (dict, optional): Properties/attributes of the node.

        Raises:
            ValueError: If children is empty or None.
        """
        if not children:
            raise ValueError("Parent nodes must have children")
        super().__init__(tag=tag, children=children, props=props)
        self.children = [child for child in (children or []) if child is not None]

    def to_html(self):
        """
        Convert the parent node and its children to HTML string representation.

        Returns:
            str: HTML string representation of the parent node and its children.

        Raises:
            ValueError: If tag is None.
        """
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        """
        Return a string representation of the parent node.

        Returns:
            str: String representation of the parent node.
        """
        return f"ParentNode(tag={self.tag!r}, children={self.children!r}, props={self.props!r})"
