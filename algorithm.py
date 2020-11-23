max_int = 5
a = []
dx = 0, 0, 1, -1
dy = -1, 1, 0, 0
str_list = []
result = 0


def go(x, y, s):
    if len(s) >= 6:

        is_exist = False
        for item in str_list:
            if item == s:
                is_exist = True
                break

        if not is_exist:
            str_list.append(s)
            global result
            result += 1

        return False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= max_int or ny < 0 or ny >= max_int: continue

        go(nx, ny, s + str(a[nx][ny]))


for i in range(max_int):
    arr = list(map(int, input().split()))
    a.append(arr)

for i in range(max_int):
    for j in range(max_int):
        go(i, j, str(a[i][j]))


print(result)