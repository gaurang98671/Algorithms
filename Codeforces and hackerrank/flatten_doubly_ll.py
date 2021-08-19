"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node', n=0) -> 'Node':

        node = head
        last_node = node

        while node != None:

            if node.child != None:

                l = self.flatten(node.child, 1)

                next_node = node.next
                node.next = node.child
                node.child.prev = node

                l.next = next_node
                if next_node != None:
                    next_node.prev = l
                node.child = None

            last_node = node

            node = node.next

        if n == 0:
            return head
        else:
            return last_node
