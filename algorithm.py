from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. init
        n = len(board)
        m = len(board[0])
        check = [[False for _ in range(m)] for _ in range(n)]
        d = (0, -1), (0, 1), (1, 0), (-1, 0)

        # 2. bfs
        def bfs(x, y):
            check[x][y] = True
            is_adjacent_to_border = False
            q = deque()
            q.append((x, y))
            s = []

            while q:
                x, y = q.popleft()
                s.append((x, y))
                if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                    is_adjacent_to_border = True

                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if not check[nx][ny] and board[nx][ny] == 'O':
                        check[nx][ny] = True
                        q.append((nx, ny))

            return (is_adjacent_to_border, s)

        # 3. flip
        def flip(s):
            for x, y in s:
                board[x][y] = 'X'

        # 4. loop
        for i in range(n):
            for j in range(m):
                if not check[i][j] and board[i][j] == 'O':
                    is_adjacent_to_border, s = bfs(i, j)

                    if not is_adjacent_to_border:
                        flip(s)        