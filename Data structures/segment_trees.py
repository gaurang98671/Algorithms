arr = [1, 2, 3, 4, 5]
segment_tree = [0 for x in range(10)]


def create_tree(arr, parent, node_type=None):
    if node_type == 'l':
        segment_tree[(2*parent)+1] = sum(arr)
    if node_type == 'r':
        segment_tree[(2*parent)+2] = sum(arr)
    if parent == -1:
        segment_tree[0] = sum(arr)

    if len(arr) == 1:
        return
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        create_tree(left, parent+1,'l')
        create_tree(right, parent+1, 'r')
create_tree(arr, -1, None)
print(segment_tree)