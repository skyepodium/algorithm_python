from collections import deque

# 1. input
n, r, c = map(int, input().split())
r -= 1
c -= 1

# 2. init
v = [['.' for _ in range(n)] for _ in range(n)]
check = [[-1 for _ in range(n)] for _ in range(n)]
q = deque()
check[r][c] = 0
q.append((r, c))
v[r][c] = 'v'
d = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

# 3. bfs
def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if check[nx][ny] == 0 or v[nx][ny] == 'v':
                continue

            check[nx][ny] = 0
            v[nx][ny] = 'v'
            q.append((nx, ny))

bfs()

res = '\n'.join(''.join(a) for a in v)
print(res)