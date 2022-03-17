from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if check[nx][ny] == -1 and a[nx][ny] == 0:
                global tomato_cnt, result
                tomato_cnt -= 1
                check[nx][ny] = check[x][y] + 1
                result = max(result, check[nx][ny])
                q.append((nx, ny))

# 1. input
m, n = map(int, input().split())
check = [[-1 for _ in range(m)] for _ in range(n)]
a = []
q = deque()
d = (0, -1), (0, 1), (1, 0), (-1, 0)
tomato_cnt = 0
result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    a.append(arr)
    for j in range(m):
        if arr[j] == 1:
            check[i][j] = 0
            q.append((i, j))
        elif arr[j] == 0:
            tomato_cnt += 1

# 2. BFS
bfs()

print(result if tomato_cnt == 0 else -1)
