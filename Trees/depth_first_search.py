class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    return _depth_first_values(root)


def _depth_first_values(root):
    if not root:
        return []

    left_values = _depth_first_values(root.left)
    right_values = _depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# a = Node('a')
