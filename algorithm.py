from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1. init
        n, m = len(grid), len(grid[0])
        check = [[False for _ in range(m)] for _ in range(n)]
        d = (0, -1), (0, 1), (1, 0), (-1, 0)
        result = 0

        # 2. bfs
        def bfs(x, y):
            check[x][y] = True
            q = deque()
            cnt = 0
            link_cnt = 0
            q.append((x, y))

            while q:
                x, y = q.popleft()
                cnt += 1
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if grid[nx][ny] == 1:
                        link_cnt += 1
                        if not check[nx][ny]:
                            check[nx][ny] = True
                            q.append((nx, ny))
            return cnt * 4 - link_cnt

        # 3. loop
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not check[i][j]:
                    result += bfs(i, j)


        return result

sl = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# grid = [[1]]
# grid = [[1, 0]]
# grid = [[0, 1]]
# grid = [[1,1],[1,1]]
res = sl.islandPerimeter(grid)

print('res', res)