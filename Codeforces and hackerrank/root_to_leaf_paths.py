# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def path(self, root, curr_path, ans, n=0):
        if root != None:
            curr_path.append(root.val)
            if root.left == None and root.right == None:
                ans.append(curr_path)
            else:

                self.path(root.left, curr_path.copy(), ans, 1)
                self.path(root.right, curr_path.copy(), ans, 1)
        if n == 0:
            return ans

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = self.path(root, [], [])
        for i in range(len(paths)):
            path = paths[i]
            str_path = str(path[0])
            for j in range(1, len(path)):
                str_path += "->" + str(path[j])
            paths[i] = str_path
        return paths