#Find avg if not int return -1 if len or arr is 1 return 0
#else traverse inputs if element greater than avg add  element-avg to list if smaller make it equal to avg
from statistics import mean
for _ in range(int(input())):
    n= int(input())
    arr= [int(x) for x in input().split(' ')]
    avg= mean(arr)

    extras=[]

    if n==1:
        print('0')

    elif type(avg) is float:
        print('-1')
    else:
        k=0
        for i in arr:
            if i > avg:
                k+=1
        print(k)




