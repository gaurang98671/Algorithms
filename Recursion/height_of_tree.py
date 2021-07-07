def height(root, level=0):
    if root is not None:
        ll = left_level = height(root.left, level + 1)
        lr = right_level = height(root.right, level + 1)
        if ll is None:
            ll = 0
        if lr is None:
            lr = 0
        return max(ll, lr, level)
