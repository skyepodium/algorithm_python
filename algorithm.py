from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 1. init
        max_val = int(1e6)
        n = len(heights)
        m = len(heights[0])
        d = [[max_val for _ in range(m)] for _ in range(n)]
        dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # 2. dijkstra
        def dijkstra(start_x, start_y):
            pq = []
            d[start_x][start_y] = 0
            for i in range(4):
                heappush(pq, (0, start_x, start_y, i))

            while pq:
                cost, x, y, c_dir = heappop(pq)

                if d[x][y] < cost: continue

                for n_dir, dxy in enumerate(dir):

                    dx, dy = dxy
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

                    n_cost = max(abs(heights[nx][ny] - heights[x][y]), d[x][y])
                    if d[nx][ny] > n_cost:
                        d[nx][ny] = n_cost
                        heappush(pq, (d[nx][ny], nx, ny, n_dir))

        dijkstra(0, 0)

        return d[n-1][m-1]


sl = Solution()

heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1,10,6,7,9,10,4,9]]
res = sl.minimumEffortPath(heights)

print('res', res)