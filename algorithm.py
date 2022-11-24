from typing import List
from collections import defaultdict, deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 1. init
        visited = defaultdict()
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def bfs(start_node):
            q = deque()
            q.append(start_node)
            key = str(start_node)
            visited[key] = 0

            while q:
                node = q.popleft()

                x, y = 0, 0
                for i in range(2):
                    for j in range(3):
                        if node[i][j] == 0:
                            x, y = i, j

                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= 2 or ny < 0 or ny >= 3:
                        continue

                    temp = []
                    for row in node:
                        t = []
                        for col in row:
                            t.append(col)
                        temp.append(t)

                    temp[nx][ny] = node[x][y]
                    temp[x][y] = node[nx][ny]
                    key = str(temp)
                    if key in visited:
                        continue
                    visited[key] = visited[str(node)] + 1
                    q.append(temp)

        bfs(board)

        end_node = [[1, 2, 3], [4, 5, 0]]
        key = str(end_node)
        return visited[key] if key in visited else -1


sl = Solution()
board = [[1,2,3],[4,0,5]]
board = [[1,2,3],[5,4,0]]
board = [[4,1,2],[5,0,3]]
res = sl.slidingPuzzle(board)

print('res', res)