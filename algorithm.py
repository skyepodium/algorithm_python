import collections


def riverSizes(matrix):

    n = len(matrix)
    m = len(matrix[0])
    d = (0, -1), (0, 1), (1, 0), (-1, 0)

    check = [[-1 for _ in range(m)] for _ in range(n)]
    res = []

    def bfs(i, j):
        check[i][j] = 0
        cnt = 1
        q = collections.deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()

            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if matrix[nx][ny] == 1 and check[nx][ny] == -1 :
                    check[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))

        return cnt

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and check[i][j] == -1:
                bfs_cnt = bfs(i, j)
                res.append(bfs_cnt)

    return res


m = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

print(riverSizes(m))
