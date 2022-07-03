mat = [[1,1,0], [1,0,0], [1,0,1]]
h = len(mat)
w = len(mat[0])
def bound(i,j):
    if i < h and j < w:
        return mat[i][j]
    else:
        return 0
visited = set()
ans = 0
for i in range(h):
    for j in range(w):
        if (i,j) not in visited and mat[i][j] == 1:
            ans += 1
            visited.add((i,j))
            q = []
            q.append((i,j))
            while q:
                s = q.pop(0)

                bot = bound(s[0] + 1, s[1])
                rt = bound(s[0], s[1] + 1)
                if bot  == 1:
                    visited.add((s[0] + 1, s[1]))
                    q.append((s[0] + 1, s[1]))
                if rt == 1:
                    visited.add((s[0], s[1] + 1))
                    q.append((s[0], s[1] + 1))

print(ans)