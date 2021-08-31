class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_linked_list(self):
        """

        :param data:
        :return:
        """
        linked_list_string = ""
        node = self.head

        if node is None:
            return None

        while node:
            linked_list_string += f"{str(node.data)}"
            # update node
            node = node.next

        return linked_list_string


ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1
print(ll.head.data)  # data1 is head of node
print("-"*50)
print(ll.head.next.next.data)
ll.print_linked_list()