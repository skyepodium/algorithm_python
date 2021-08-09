import collections


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        d = (0, -1), (0, 1), (1, 0), (-1, 0)

        n = len(grid)
        m = len(grid[0])

        check = [[False for _ in range(m)] for _ in range(n)]
        result = 0

        def bfs(x, y):
            q = collections.deque()
            check[x][y] = True
            q.append((x, y))
            cnt = 0

            while q:
                x, y, = q.popleft()
                cnt += 1
                for dx, dy in d:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if grid[nx][ny] == 1 and not check[nx][ny]:
                        check[nx][ny] = True
                        q.append((nx, ny))

            return cnt

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not check[i][j]:
                    result = max(result, bfs(i, j))

        return result




sl = Solution()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
res = sl.maxAreaOfIsland(grid)

print(res)