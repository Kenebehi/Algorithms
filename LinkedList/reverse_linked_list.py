class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    current = head
    prev = None

    while current:
        next = current.next

        # set current head to None
        current.next = prev

        prev = current
        current = next

    return prev


def reverse_list_recursive(head, prev=None):
    # a -> b ->c
    # next = b

    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_recursive(next, head)


def print_linked_list(head):
    linked_list_string = ""
    current = head

    while current:
        linked_list_string += f" {str(current.val)}"
        current = current.next

    return linked_list_string


e = Node(7, None)
d = Node(-1, e)
c = Node(3, d)
b = Node(8, c)
a = Node(2, b)

print(reverse_list(a))
print(print_linked_list(e))
print(reverse_list_recursive(e))
print(print_linked_list(a))