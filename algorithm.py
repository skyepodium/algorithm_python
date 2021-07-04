def solution(dirs):
    answer = 0
    max_int = 11

    check = [[[[False for _ in range(max_int)] for _ in range(max_int)] for _ in range(max_int)] for _ in range(max_int)]

    x, y = 5, 5
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for cur in dirs:
        dir_num = 0
        if cur == 'R': dir_num = 1
        elif cur == 'D': dir_num = 2
        elif cur == 'L': dir_num = 0
        else: dir_num = 3

        dx, dy = d[dir_num]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx > 10 or ny < 0 or ny > 10:
            continue

        if not check[x][y][nx][ny]:
            check[x][y][nx][ny] = True
            check[nx][ny][x][y] = True
            answer += 1

        x, y = nx, ny

    return answer
