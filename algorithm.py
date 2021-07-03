def solution(rows, columns, queries):
    answer = []

    a = [[0 for _ in range(columns)] for _ in range(rows)]

    dx = 1, 0, -1, 0
    dy = 0, 1, 0, -1

    num = 1
    for i in range(rows):
        for j in range(columns):
            a[i][j] = num
            num += 1

    for sx, sy, ex, ey in queries:
        sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
        points = [(sx, sy), (ex, sy), (ex, ey), (sx, ey)]
        height, width = ex - sx + 1, ey - sy + 1
        first_num = a[sx][sy]
        min_num = 10001
        min_num = min(min_num, first_num)

        for dir in range(4):
            cx, cy = points[dir]
            range_size = height if dir % 2 == 0 else width
            range_size -= 1

            for idx in range(range_size):

                bx, by = cx + dx[dir], cy + dy[dir]
                a[cx][cy] = a[bx][by]
                if dir == 3 and idx == range_size - 1:
                    a[cx][cy] = first_num
                min_num = min(min_num, a[cx][cy])
                cx, cy = bx, by

        answer.append(min_num)

    return answer




r = 6
c = 6
q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# q = [[2,2,5,4]]

res = solution(r, c, q)
print("res", res)