from collections import deque


d = []
check = []
v = []


def find(node):
    if node == d[node]:
        return node
    else:
        d[node] = find(d[node])
        return d[node]


def bfs(start_x, start_y, num, size, land, height):

    dx = 0, 0, 1, -1
    dy = -1, 1, 0, 0

    q = deque()
    check[start_x][start_y] = num
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue

            diff = abs(land[nx][ny] - land[x][y])
            if check[nx][ny] == -1 and diff <= height:
                check[nx][ny] = num
                q.append((nx, ny))


def solution(land, height):
    answer = 0
    size = len(land)
    max_val = 2147483647

    num = -1
    global check
    check = [[-1 for _ in range(size+1)] for _ in range(size+1)]
    for i in range(size):
        for j in range(size):
            if check[i][j] == -1:
                num += 1
                bfs(i, j, num, size, land, height)

    global d
    d = []
    for i in range(num+1):
        d.append(i)

    dx = 0, 0, 1, -1
    dy = -1, 1, 0, 0
    global v
    for i in range(size):
        for j in range(size):
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    continue
                c_group = check[i][j]
                n_group = check[nx][ny]
                if c_group != n_group:
                    diff = abs(land[i][j] - land[nx][ny])
                    v.append((c_group, n_group, diff))

    v = sorted(v, key=lambda a: a[2])
    for start_node, end_node, cost in v:
        start_node = find(start_node)
        end_node = find(end_node)

        if start_node != end_node:
            d[start_node] = end_node
            answer += cost

    return answer


# land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
# height = 3

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1

res = solution(land, height)

print('res', res)