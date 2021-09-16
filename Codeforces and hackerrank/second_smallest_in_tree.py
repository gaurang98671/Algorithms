# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sol(self, root, first, second, n=0):
        if root != None:
            if root.val < first[0]:
                second[0] = first[0]
                first[0] = root.val

            elif root.val < second[0] and root.val != first[0]:
                second[0] = root.val

            self.sol(root.left, first, second, 1)
            self.sol(root.right, first, second, 1)

        if n == 0:
            return second

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a = self.sol(root, [float(inf)], [float(inf)])
        if a[0] == inf:
            return -1
        else:
            return a[0]