def solution(n):
    # 1. init
    d = [1 for _ in range(n+1)]

    def eratos():
        for i in range(2, int(n ** 0.5) + 1):
            for j in range(i*2, n+1, i):
                d[j] = 0

    d[0], d[1] = 0, 0
    eratos()

    return sum(d)


n = 10
n = 5
res = solution(n)

print('res', res)