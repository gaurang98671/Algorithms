class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrder(temp):

    if not temp:
        return
    inOrder(temp.left)
    print(temp.val)
    inOrder(temp.right)


def preOrder(temp):

    if not temp:
        return
    print(temp.val)
    preOrder(temp.left)

    preOrder(temp.right)


def postOrder(temp):

    if not temp:
        return
    postOrder(temp.left)

    postOrder(temp.right)

    print(temp.val)


if __name__ == '__main__':
    root = Node(11)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(14)

    preOrder(root)

