arr = [1,2,3,4,5,6,7,8,9]


def search(num):

    low = 0
    high = len(arr) - 1


    while low <= high:
        mid = (low + high) // 2
        if num < arr[mid]:
            print(arr[mid])
            high = mid - 1
        elif num > arr[mid]:
            print(arr[mid])
            low = mid + 1
        else:
            return True, mid
    return False

print(search(2))
