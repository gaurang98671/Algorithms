# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self, root, ans, n=0, level=0):
        if root != None:
            if len(ans) - 1 < level:
                ans.append(root.val)
            else:
                ans[level] = max(ans[level], root.val)
            self.sol(root.left, ans, 1, level + 1)
            self.sol(root.right, ans, 1, level + 1)

        if n == 0:
            return ans

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        a = self.sol(root, [])
        return a