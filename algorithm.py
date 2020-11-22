from collections import deque


def sort_value(tx, ty, tz):
    arr = [tx, ty, tz]
    arr.sort()

    return arr


max_int = 1501
check = [[False for _ in range(max_int)] for _ in range(max_int)]
a, b, c = map(int, input().split())
a, b, c = sort_value(a, b, c)
result = 0


def bfs(x, y, z):
    q = deque()
    check[x][y] = True
    q.append((x, y, z))

    while q:
        x, y, z = q.popleft()

        if x == y and y == z:
            global result
            result = 1
            break

        if y - x > 0:
            nx = x * 2
            ny = y - x
            nz = z

            if nx < max_int and ny > 0:
                nx, ny, nz = sort_value(nx, ny, nz)

                if not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, nz))

        if z - x > 0:
            nx = x * 2
            ny = z - x
            nz = y

            if nx < max_int and ny > 0:
                nx, ny, nz = sort_value(nx, ny, nz)

                if not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, nz))

        if z - y > 0:
            nx = y * 2
            ny = z - y
            nz = x

            if nx < max_int and ny > 0:
                nx, ny, nz = sort_value(nx, ny, nz)

                if not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, nz))


bfs(a, b, c)

print(result)
