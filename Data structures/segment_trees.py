arr = [1, 2, 3, 4, 5]
segment_tree = []

def create_tree(arr):
    print(arr)
    if len(arr)==1:
        return
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        create_tree(left)
        create_tree(right)
create_tree(arr)