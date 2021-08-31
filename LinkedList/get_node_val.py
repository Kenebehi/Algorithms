class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def get_node_value(head, index):
    current = head
    count = 0

    while current:
        if count == index:
            return current.val

        current = current.next
        count += 1


e = Node(7, None)
d = Node(-1, e)
c = Node(3, d)
b = Node(8, c)
a = Node(2, b)

print(get_node_value(a, 4))