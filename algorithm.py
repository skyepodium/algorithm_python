from collections import deque


def bfs():
    global result, cnt
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0: continue

            if check[nx][ny] == -1 and a[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                result = max(result, check[nx][ny])
                cnt -= 1
                q.append((nx, ny))


m, n = map(int, input().split())
a = []
check = [[-1 for _ in range(m)] for _ in range(n)]
cnt = 0
q = deque()
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    a.append(arr)

    for j in range(m):
        if a[i][j] == 0:
            cnt += 1
        elif a[i][j] == 1:
            check[i][j] = 0
            q.append((i, j))

bfs()
if cnt != 0:
    result = -1

print(result)
