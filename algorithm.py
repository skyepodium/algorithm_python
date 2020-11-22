from collections import deque


def bfs(x, y):
    q = deque()
    check[x][y] = True
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and a[nx][ny] == 0:
                    check[nx][ny] = True
                    q.append((nx, ny))


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input())))

check = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
result = 0


for i in range(n):
    for j in range(m):
        if not check[i][j] and a[i][j] == 0:
            result += 1
            bfs(i, j)

print(result)