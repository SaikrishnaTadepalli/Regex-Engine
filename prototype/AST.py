class AST:
    def __init__(self):
        self.pattern = ""
        self.root = None

    def set_pattern(self, pattern):
        self.pattern = pattern

    def get_pattern(self):
        return self.pattern

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def add_node(self, parent, child):
        parent.add_child(child)

    def delete_node(self, node):
        parent = node.get_parent()
        if parent is not None:
            parent.remove_child(node)

    def modify_node(self, node, new_value):
        node.set_value(new_value)

    # Other utility functions specific to AST management
    # ...


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent
