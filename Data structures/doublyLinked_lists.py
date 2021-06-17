class Node:
    def __init__(self, next, prev, val):
        self.next = next
        self.prev = prev
        self.val = val


class LinkedList:
    def __init__(self):
        self.root = Node(None, None, None)



    def add_node(self, val):
        node = self.root
        while node.next is not None:
            node = node.next
        new_node = Node(None, node, val)
        node.next = new_node

    def get_all(self):
        if self.root.next != None:

            node = self.root.next
            while node is not None:

                print("Address", str(node),"Value",node.val,"Previous",  node.prev, "Next",node.next)
                node = node.next

        else:
            print("Linked list is empty")
    def delete_node(self, val):
        prev_node = self.root
        node = self.root.next


        while node.next != None:
            if node.val == val:
                prev_node.next = node.next

                return  "value deleted"
            else:
                prev_node = node
                node = node.next

        if node.val==val:
            prev_node.next = None
            return "value deleted"
        return "value not found"

    def reverse(self):
        node = self.root.next
        prev_node = None

        while node is not None:

            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.root.next = prev_node




ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.get_all()