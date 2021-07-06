arr = [9,10,2,3,4,5,6,7,8, 11, 44, 42]
first = arr[0]
second = 0

for i in arr[1:]:
    if i > first:
        second = first
        first = i
    elif i > second:
        second = i




print(second)