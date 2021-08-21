# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getr(self, root, arr, n = 0):
        if root!=None:
            arr[n] =  root.val
            self.getr(root.left, arr, n+1)
            self.getr(root.right, arr, n+1)
        if n == 0:
            return arr
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = [-1 for x in range(100)]
        ans = self.getr(root, arr)
        n = 0
        for i in ans:
            if i == -1:
                break
            else:
                n += 1
        return ans[:n]