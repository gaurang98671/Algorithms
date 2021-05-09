print("Merge sort")
def merge_sort(arr):
    if len(arr) > 1:

        # find mid
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1

            else:
                arr[k] = right[j]
                j += 1
                k += 1

        # Check for remaining elements
        # For left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # For right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


a = [2, 4, 3, 5, 1]
print("Unsorted array: ", a)
merge_sort(a)
print("Sorted array: ", a)
