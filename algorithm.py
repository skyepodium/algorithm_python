def solution(n):
    # 1. init
    res = 0
    d = [0 for _ in range(n+1)]

    # 2. accmulate sum
    d[0], d[1] = 0, 1
    for i in range(1, n+1):
        d[i] = d[i-1] + i

    # 3. two pointer
    s, e = 0, 0
    while s <= e < n + 1 and s < n+1:
        cur = d[e] - d[s]
        if cur <= n:
            if cur == n: res += 1
            e += 1
        else:
            s += 1

    return res



n = 15

res = solution(n)

print('res', res)