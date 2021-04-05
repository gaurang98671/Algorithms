#Best case O(n)
#Worst case O(n^2)
#Use when only few items or items are mostly sorted already
print("Insertion sort")
print("__" * 30)

arr = [3, 6, 4, 1, 7, 9, 2]
n = len(arr)


def insert(pos, val):
    print("For value: ", val)
    prev= pos-1

    while(prev>=0 and arr[prev] > val):
        arr[prev], arr[prev+1]= arr[prev+1], arr[prev]
        print("Swapping", prev, prev+1)
        prev -= 1



for i in range(1, n):
    insert(i, arr[i])
    print(arr)

