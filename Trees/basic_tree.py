class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

    def insert(self, Node):
        return self._insert(Node)

    def _insert(self, node):
        if self.head is None:
            self.head = node

        if node < self.head:
            self.left

