print("Insertion sort")
print("__" * 30)

arr = [3, 6, 4, 1, 7, 9, 2]
n = len(arr)


def insert(pos, val):
    print("For value: ", val)
    prev= pos-1
    new_pos= pos
    while(prev>=0 and arr[prev] > val):
        arr[prev], arr[new_pos]= arr[new_pos], arr[prev]
        print("Swapping",prev,new_pos)
        prev-=1
        new_pos-=1


for i in range(1, n):
    insert(i, arr[i])

