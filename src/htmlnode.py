class HTMLNode:
    """
    Represents the HTML node class.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

class LeafNode(HTMLNode):
    """
    Represents the HTML leaf node class.
    """

    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("Leaf nodes must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """
        Function converts leaf node objects to HTML format.
        """
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(value={self.value!r}, tag={self.tag!r}, props={self.props!r})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
            self.value == other.value
            and self.tag == other.tag
            and self.props == other.props
        )

    def debug(self):
        """Returns detailed information about the instance."""
        return f"LeafNode(value={self.value!r}, tag={self.tag!r}, props={self.props!r})"


class ParentNode(HTMLNode):
    """
    Represents the parent node class.
    """

    def __init__(self, tag, children, props=None):
        if not children:
            raise ValueError("Parent nodes must have children")
        super().__init__(tag=tag, children=children, props=props)
        self.children = [child for child in (children or []) if child is not None]

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if not self.children:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag!r}, children={self.children!r}, props={self.props!r})"
