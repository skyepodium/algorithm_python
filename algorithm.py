from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 1. init
        n = len(grid)
        m = len(grid[0])
        check = [[-1 for _ in range(m)] for _ in range(n)]
        d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        # 2. bfs
        def bfs(x, y):
            if grid[x][y] != 0: return

            check[x][y] = 1
            q = deque([(x, y)])

            while q:
                x, y = q.popleft()

                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                    if grid[nx][ny] != 0 or check[nx][ny] != -1: continue

                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))

        bfs(0, 0)

        return check[n-1][m-1]


sl = Solution()
grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[1,0,0],[1,1,0],[1,1,0]]
res = sl.shortestPathBinaryMatrix(grid)

print('res', res)