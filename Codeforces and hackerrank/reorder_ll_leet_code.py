# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return head

        node = head
        queue = []
        while node != None:
            queue.append(node)
            node = node.next
        ptr1 = 0
        ptr2 = len(queue) - 1

        last_node = None

        while (ptr1 <= ptr2):
            print(last_node)
            if ptr1 == ptr2:
                last_node.next = queue[ptr1]
                queue[ptr1].next = None

            else:
                queue[ptr1].next = queue[ptr2]
                queue[ptr2].next = None
                if last_node != None:
                    last_node.next = queue[ptr1]
                last_node = queue[ptr2]
            ptr1 += 1
            ptr2 -= 1
        return head



