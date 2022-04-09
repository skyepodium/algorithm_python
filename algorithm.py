from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 1. init
        n = len(grid)
        check = [[-1 for _ in range(n)] for _ in range(n)]
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # 2. bfs
        def bfs(start_x, start_y, idx):
            check[start_x][start_y] = idx
            q = deque()
            q.append((start_x, start_y))
            cnt = 0

            while q:
                x, y = q.popleft()
                cnt += 1
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if check[nx][ny] == -1 and grid[nx][ny] == 1:
                        check[nx][ny] = idx
                        q.append((nx, ny))
            return cnt

        # 3. loop
        idx = 0
        cnt_dict = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and check[i][j] == -1:
                    cnt = bfs(i, j, idx)
                    cnt_dict[idx] = cnt
                    idx += 1
        print(cnt_dict)
        # 4. loop
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cur_cnt = 0
                    seen = set()
                    for dx, dy in d:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        print(nx, ny)

                        if check[nx][ny] > -1 and check[nx][ny] not in seen:
                            n_idx = check[nx][ny]
                            n_cnt = cnt_dict[n_idx]
                            cur_cnt += n_cnt
                            seen.add(n_idx)
                    res = max(res, cur_cnt + 1)

        return res if res > 0 else n * n


sl = Solution()

grid = [[1,0],[0,1]]

res = sl.largestIsland(grid)

print('res', res)