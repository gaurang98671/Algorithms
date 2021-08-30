arr = [54,66,23,21,44,21,23]
arr.sort(reverse=1)
rank = 1
last = arr[0]
ranks = [1]
for i in arr[1:]:
    if i == last:
        ranks.append(rank)

    else:
        last = i
        rank += 1
        ranks.append(rank)
print(arr)
print(


