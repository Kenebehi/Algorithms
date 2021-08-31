class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def sum_list(head):
    current = head
    linked_list_sum = 0

    while current:
        linked_list_sum += current.val
        current = current.next

    return linked_list_sum


e = Node(7, None)
d = Node(-1, e)
c = Node(3, d)
b = Node(8, c)
a = Node(2, b)

print(sum_list(a))
