# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sol(self, root, ans, path, n=0):
        if root != None:
            new_path = path.copy()
            new_path.append(chr(root.val + 97))
            if root.left == None and root.right == None:
                s = "".join(new_path[::-1])
                if ans[0] == -1:
                    ans[0] = s
                else:
                    ans[0] = min(ans[0], s)

            self.sol(root.left, ans, new_path, 1)
            self.sol(root.right, ans, new_path, 1)

        if n == 0:
            return ans

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        a = self.sol(root, [-1], [])
        return a[0]
