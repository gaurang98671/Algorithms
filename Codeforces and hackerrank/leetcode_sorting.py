arr = []

#incrementing all elements in subtree x * 2 + 1, x * 2 + 2
def incr_val(node, val, arr):
    if node < len(arr):
        arr[node] += val
        incr_val(node * 2 + 1, val, arr)
        incr_val(node * 2 + 2, val, arr)
"""
5
1
1
1
1
3
3
3
2
4
5
1
1
"""
for _ in range(int(input())):

    x = int(input())
    arr.append(x)

q_c = int(input())

queries = [[] for x in range(q_c)]

for i in range(q_c):
    queries[i].append(int(input()))

for i in range(q_c):
    queries[i].append(int(input()))

for i in queries:
    node = i[0]
    val = i[1]

    incr_val(node, val, arr)


#xor
ans = arr[0]
for i in arr[1:]:
    ans = ans ^ i
print(ans)