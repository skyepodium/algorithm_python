def solution(n, results):
    max_val = 101
    max_cnt = 0
    d = [[max_val for _ in range(n+1)] for _ in range(n+1)]

    for e, s in results:
        d[s][e] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue

            if d[i][j] == max_val and d[j][i] == max_val:
                max_cnt += 1
                break

    return n - max_cnt


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

1 < 2

res = solution(n, results)

print('res', res)