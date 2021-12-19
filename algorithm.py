class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        check = [[False for _ in range(m)] for _ in range(n)]
        d = (0, -1), (0, 1), (1, 0), (-1, 0)

        cnt = 0

        def dfs(x, y):
            check[x][y] = True

            for dx, dy in d:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if grid[nx][ny] == "1" and not check[nx][ny]:
                    dfs(nx, ny)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not check[i][j]:
                    dfs(i, j)
                    cnt += 1

        return cnt