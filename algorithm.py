from heapq import heappush, heappop

def solution(board):
    # 1. init
    n = len(board)
    m = len(board[0])
    MAX_VAL = n * m * 500
    d = [[[MAX_VAL for _ in range(4)] for _ in range(m)] for _ in range(n)]
    dir_list = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    # 0 - left, 1 - right, 2 - down, 3 - up

    # 2. dijkstra
    def dijkstra(start_x, start_y):
        pq = []

        for c_dir in range(4):
            d[start_x][start_y][c_dir] = 0
            heappush(pq, (0, start_x, start_y, c_dir))

        while pq:
            cost, x, y, dir = heappop(pq)

            for n_dir_idx, n_dir in enumerate(dir_list):
                dx, dy = n_dir
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny] == 1: continue

                n_cost = 100 if dir == n_dir_idx else 600

                if d[nx][ny][n_dir_idx] > d[x][y][dir] + n_cost:
                    d[nx][ny][n_dir_idx] = d[x][y][dir] + n_cost
                    heappush(pq, (d[nx][ny][n_dir_idx], nx, ny, n_dir_idx))

    dijkstra(0, 0)

    return min(d[n-1][m-1])
