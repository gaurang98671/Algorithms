for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr = sorted(arr)
    count= 1
    min_val = float('inf')
    for i in range(1, n):
        d = abs(arr[i] - arr[i - 1])
        min_val = min(min_val, d)
        if min_val < arr[i]:
            break
        count += 1
    print(count)


