class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return ''.join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"tag: {self.tag}\n \
                value: {self.value}\n \
                children: {self.children}\n \
                props: {self.props}\n"
