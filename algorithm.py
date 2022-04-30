from collections import defaultdict

def solution(money):
    # 1. init
    n = len(money)
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    a[0] = money[0]

    for i in range(1, n-1):
        a[i] = max(a[i-2] + money[i], a[i-1])

    for i in range(1, n):
        b[i] = max(b[i-2] + money[i], b[i-1])

    return max(a[n-2], b[n-1])


money = [1, 2, 3, 1]
money = [10000, 3, 7, 4, 5]
money = [1, 100, 1, 100, 1]

res = solution(money)

print('res', res)