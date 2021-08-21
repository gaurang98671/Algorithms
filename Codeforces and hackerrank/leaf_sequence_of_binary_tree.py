# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getseq(self, root, arr, n=0):
        if root != None:
            if root.left == None and root.right == None:
                arr.append(root.val)
            self.getseq(root.left, arr, 1)
            self.getseq(root.right, arr, 1)
        if n == 0:
            return arr

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        f = self.getseq(root1, [])
        s = self.getseq(root2, [])
        return f == s
