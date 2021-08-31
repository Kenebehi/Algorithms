class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def linked_list_find(head, target):
    """
    input: head
    input: target
    return boolean
    """
    current = head
    if current == target:
        return True

    while current:
        if current.val == target:
            return True
        current = current.next
    return False


e = Node(7, None)
d = Node(-1, e)
c = Node(3, d)
b = Node(8, c)
a = Node(2, b)

print(linked_list_find(a, -3))
