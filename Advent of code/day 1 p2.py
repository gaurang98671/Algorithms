a = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]

a2 = sorted(a)

start, end = -1, -1

for i in range(len(a)):

    if a[i] != a2[i]:
        start = i
        break
for i in range(len(a)-1, -1, -1):
    if a[i] != a2[i]:
        end = i
        break

print(start, end)

#space O(n) time O(n)



