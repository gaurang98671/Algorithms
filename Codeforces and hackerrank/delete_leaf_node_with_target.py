# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sol(self, root, target, parent=-1, t=0):
        if root != None:

            self.sol(root.left, target, root, 1)
            self.sol(root.right, target, root, 2)

            if root.val == target and root.left == None and root.right == None:
                if t == 0:
                    return None
                elif t == 1:
                    parent.left = None
                else:
                    parent.right = None

            if t == 0:
                return root

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        a = self.sol(root, target)

        return a
