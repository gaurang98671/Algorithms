#Best case, worst case:  O(n^2)
print("Selection sort")
print("__"*30)
arr = [3, 6, 4, 1, 7, 9, 2, 3]
n=len(arr)

for i in range(0, n-1):
    smallest=i

    #Finding smallest value for between all the values to right
    for j in range(i+1, n):
        if arr[j] < arr[smallest]:
            smallest = j

    #Swap current index with new smallest value found
    arr[i], arr[smallest] = arr[smallest], arr[i]


print(arr)