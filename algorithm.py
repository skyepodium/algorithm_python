from collections import deque

n, m, k = map(int, input().split())

max_val = 1001 * 1001
a = []
check = [[[max_val for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    arr = list(map(int, input()))
    a.append(arr)

q = deque()
check[0][0][0] = 1
q.append((0, 0, 0))

while q:
    x, y, use = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

        if a[nx][ny] == 0 and check[nx][ny][use] > check[x][y][use] + 1:
            check[nx][ny][use] = check[x][y][use] + 1
            q.append((nx, ny, use))

        if a[nx][ny] == 1 and use < k and check[nx][ny][use + 1] > check[x][y][use] + 1:
            check[nx][ny][use + 1] = check[x][y][use] + 1
            q.append((nx, ny, use + 1))

result = max_val
for value in check[n-1][m-1]:
    result = min(result, value)

if result == max_val: result = -1

print(result)

