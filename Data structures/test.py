arr = [1, 6, 11, 5 ,7,9]
arr = sorted(arr)
print(arr)
s = sum(arr)
ptr = 0
print(s)
curr_sum = arr[0]
min_sum = abs(curr_sum - (s-curr_sum))

for i in range(1, len(arr)):
    curr_sum += arr[i]
    print(min_sum ,curr_sum, s-curr_sum)

    curr_diff = abs(curr_sum - (s - curr_sum))
    print(curr_diff)
    if curr_diff < min_sum:
        min_sum = curr_diff
        ptr = i
print(arr[:ptr+1], arr[ptr+1:])