def solution(m, n, board):
    # 1. init
    n, m = m, n
    res = 0
    board = [list(x) for x in board]
    check = [[False for _ in range(m)] for _ in range(n)]
    d = [(0, 0), (0, 1), (1, 0), (1, 1)]

    # 2. search
    def search():
        cnt = 0
        for i in range(n-1):
            for j in range(m-1):
                prev = board[i][j]
                if prev == "": continue

                is_same = True
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    cur = board[nx][ny]
                    if prev != cur:
                        is_same = False
                        break

                if not is_same: continue

                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if check[nx][ny]: continue
                    check[nx][ny] = True
                    cnt += 1

        return cnt

    # 3. move
    def move():
        for j in range(m):
            for idx in range(n-1, -1, -1):
                i = idx
                if board[i][j] == "" or check[i][j]: continue

                while i < n-1 and board[i][j] != "" and board[i+1][j] == "":
                    board[i+1][j] = board[i][j]
                    board[i][j] = ""
                    i += 1

    # 4. clear
    def clear():
        for i in range(n):
            for j in range(m):
                if check[i][j]:
                    board[i][j] = ""

    # 5. loop
    while True:
        # 1) init
        check = [[False for _ in range(m)] for _ in range(n)]

        # 2) search
        search_cnt = search()
        if search_cnt == 0: break
        res += search_cnt

        # 3) clear
        clear()

        # 4) move
        move()

    return res


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# m = 6
# n = 6
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

res = solution(m, n, board)

print('res', res)