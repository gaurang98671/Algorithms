# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, root, arr, n = 0):
        if root!=None:
            arr.append(1)
            self.count(root.left, arr, 1)
            self.count(root.right, arr, 1)
        if n == 0:
            return len(arr)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        c = self.count(root, [])
        return c