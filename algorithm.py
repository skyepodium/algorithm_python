t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    def sum_val(s, e, nx, ny):
        res = 0
        while 0 <= s < n and 0 <= e < m:
            res += a[s][e]
            s, e = s + nx, e + ny
        return res

    res = 0
    for i in range(n):
        for j in range(m):
            val = -3 * a[i][j]
            d = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
            for dx, dy in d:
                val += sum_val(i, j, dx, dy)
            res = max(res, val)
    print(res)



