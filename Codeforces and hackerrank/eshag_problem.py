from collections import  Counter
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print(len(arr)-arr.count(min(arr)))
