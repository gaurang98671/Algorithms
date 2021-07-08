# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

def insert(self, val):
    node = self.root
    new_node = Node(info=val)

    if node == None:
        self.root = new_node
        return self.root
    while True:

        if val < node.info:

            if node.left == None:
                node.left = new_node
                break
            else:
                node = node.left
        else:

            if node.right == None:
                node.right = new_node
                break
            else:
                node = node.right
    return self.root
