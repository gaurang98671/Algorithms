arr = [2,7,4,3,5]

stack = []
ans = []
for i in range(len(arr)):
    ans.append(0)

    if len(stack) == 0 or stack[-1][0] >= arr[i]:
        stack.append((arr[i], i))
    else:
        while len(stack) > 0 and stack[-1][0] < arr[i]:
            a = stack.pop(-1)
            ans[a[1]] = arr[i]
        arr.append((arr[i], i))

print(ans)
print(stack)