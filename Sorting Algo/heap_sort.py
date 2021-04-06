arr = [1, 12, 9, 5, 6, 10]
n = len(arr)
new_arr=[]

def heapify(i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(arr) and arr[left] > arr[largest]:
        largest = left

    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    # swap root with largest
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        #print(arr)
        heapify(largest)


print("Original array: ", arr)

for i in range((n//2)-1, -1, -1):
    print("For:  ", i)
    heapify(i)
    print(arr)

while(len(arr)!=1):
    arr[0], arr[len(arr)-1]= arr[len(arr)-1], arr[0]
    print("After swapping", arr)
    print("Popping", arr[len(arr)-1])
    new_arr.append(arr[len(arr)-1])
    arr.pop(len(arr)-1)
    print("after popping", arr)

    heapify(0)

print(new_arr)