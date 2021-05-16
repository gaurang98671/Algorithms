class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(temp):

    if not temp:
        return
    inorder(temp.left)
    print(temp.val)
    inorder(temp.right)

if __name__ == '__main__':
    root = Node(11)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(14)

    inorder(root)

