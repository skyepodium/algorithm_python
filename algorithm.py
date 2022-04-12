class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 1. init
        n = len(board)
        m = len(board[0])
        d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        a = [[0 for _ in range(m)] for _ in range(n)]
        
        # 2. loop
        for i in range(n):
            for j in range(m):
                cur = board[i][j]
                cnt = 0
                
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        
                    ne = board[nx][ny]
                    if ne == 1: cnt += 1
                
                if cur == 1:
                    if 2 <= cnt <= 3: a[i][j] = 1
                else:
                    if cnt == 3: a[i][j] = 1
        
        # 3. copy
        for i in range(n):
            for j in range(m):
                board[i][j] = a[i][j]
