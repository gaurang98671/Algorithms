"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root, level=0):
    if root is not None:
        new_l = [(root.info, level)]
        ll = levelOrder(root.left, level + 1)
        lr = levelOrder(root.right, level + 1)

        for i in ll:
            new_l.append(i)
        for i in lr:
            new_l.append(i)
        if level == 0:
            new_l.sort(key=lambda x: x[1])
            for i in new_l:
                print(i[0], end=' ')
        return new_l
    else:
        return []
