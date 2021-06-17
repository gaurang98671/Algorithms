import bisect
for _ in range(int(input())):
    n, l, r = (int(x) for x in input().split(' '))
    arr = [int(x) for x in input().split(' ')]
    arr= sorted(arr)
    count=0
    for i in  range(n):

        upper= bisect.bisect_right(arr, r-arr[i],i+1, n)
        lower = bisect.bisect_left(arr, l - arr[i], i + 1, n)
        count+= upper-lower
    print(count)



#Sort array
#Find range of all numbers that will satisfy conditions
