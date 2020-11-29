def dfs(x, y, soldier):
    check[x][y] = True
    global cnt
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

        if not check[nx][ny] and a[nx][ny] == soldier:
            dfs(nx, ny, a[nx][ny])


m, n = map(int, input().split())
a = []
check = [[False for _ in range(m)] for _ in range(n)]
w_result = b_result = 0
dx = 0, 0, 1, -1
dy = -1, 1, 0, 0

for _ in range(n):
    arr = list(input())
    a.append(arr)

for i in range(n):
    for j in range(m):
        if not check[i][j]:
            cnt = 0

            dfs(i, j, a[i][j])

            if a[i][j] == 'W':
                w_result += cnt * cnt
            else:
                b_result += cnt * cnt

print("{0} {1}".format(w_result, b_result))