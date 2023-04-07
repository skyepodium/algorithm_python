from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 1. init
        res = 0
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # 2. dfs
        def dfs(x, y):
            visited[x][y] = True

            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if grid[nx][ny] != 0 or visited[nx][ny]:
                    continue
                dfs(nx, ny)

        # 3. edge
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 0 and not visited[i][j]:
                        dfs(i, j)

        # 4. center
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    dfs(i, j)
                    res += 1

        return res

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]

sl = Solution()
res = sl.closedIsland(grid)
print('res', res)