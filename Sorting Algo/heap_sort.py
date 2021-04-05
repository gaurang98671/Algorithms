arr = [1, 12, 9, 5, 6, 10]
n = len(arr)


def heapify(i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n \
            and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
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