class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # 1. init
        n, m = len(board), len(board[0])
        check = [[False for _ in range(m)] for _ in range(n)]
        start_nodes = []
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        self.is_exist = False

        # 2. start_nodes
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    start_nodes.append((i, j))

        # 3. DFS
        def dfs(x, y, cnt, s):
            if cnt >= len(word):
                if s == word:
                    self.is_exist = True
                return

            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if not check[nx][ny] and board[nx][ny] == word[cnt]:
                    check[nx][ny] = True
                    dfs(nx, ny, cnt + 1, s + board[nx][ny])
                    check[nx][ny] = False

        # 4. loop
        for x, y in start_nodes:
            check[x][y] = True
            dfs(x, y, 1, f"{board[x][y]}")
            if self.is_exist:
                return True
            check[x][y] = False

        return False