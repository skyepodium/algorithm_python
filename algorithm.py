from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 1. init
        n, m = len(image), len(image[0])
        visited = [[False] * m for _ in range(n)]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start_color = image[sr][sc]

        # 2. bfs
        def bfs(start_x, start_y):
            q = deque()
            q.append((start_x, start_y))

            while q:
                x, y = q.popleft()
                visited[x][y] = True
                image[x][y] = color

                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if visited[nx][ny] or image[nx][ny] != start_color:
                        continue

                    q.append((nx, ny))
                    visited[nx][ny] = True
                    image[nx][ny] = color

        bfs(sr, sc)

        return image


image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

sl = Solution()
print(sl.floodFill(image, sr, sc, color))
