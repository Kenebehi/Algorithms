class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


def remove_node(head, target):
    """

    :param self:
    :param head:
    :param target: type - node
    :return:
    """
    current = head

    # first find node
    while current:
        if current.next == target:
            # to remove a node assign the prev node to target.next
            current.next = target.next
        current = current.next

    return


def print_linked_list(head):
    current = head
    output = ""

    while current:
        output += f"{str(current.data)}"
        current = current.next
    return output


e = Node(7, None)
d = Node(-1, e)
c = Node(3, d)
b = Node(8, c)
a = Node(2, b)

print(remove_node(a, d))
print(print_linked_list(a))


