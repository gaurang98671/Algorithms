class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val


class LinkedList:
    def __init__(self):
        self.root = Node(None, None)

    def add_node(self, val):
        node = self.root
        while node.next is not None:
            node = node.next
        new_node = Node(None, val)
        node.next = new_node

    def get_all(self):
        if self.root.next != None:
            node = self.root.next
            while node.next is not None:
                print(node.val)
                node = node.next
            print(node.val)
        else:
            print("Linked list is empty")


ll = LinkedList()

ll.get_all()
