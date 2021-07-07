import math
import os

sample_arr = [1, 2, 5, 6, 7, 9]
segment_tree = ["Dummy" for x in range(15)]

def create_tree(arr, parent):
    segment_tree[parent] = sum(arr)
    print(arr, parent)
    if len(arr) == 1:
        return
    else:
        mid = math.ceil(len(arr) / 2)
        left = arr[:mid]
        right = arr[mid:]
        create_tree(left, (2 * parent) + 1)
        create_tree(right, (2 * parent) + 2)


create_tree(sample_arr, 0)
print(segment_tree)

