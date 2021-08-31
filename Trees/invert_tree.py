class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def invert_tree(root):
    return _invert_tree(root)


def _invert_tree(root):
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()

        if current:
            # print(current.left, current.right)
            # print(current.left)
            current.left, current.right = current.right, current.left
            stack.append(current.left)
            stack.append(current.right)


def traverse_tree(root):
    if not root:
        return []

    left_values = traverse_tree(root.left)
    right_values = traverse_tree(root.right)
    return [root.data, *left_values, *right_values]


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

print(traverse_tree(a))
print(_invert_tree(a))
print(traverse_tree(a))
