t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    res = 0
    for i in range(n - 1):
        res += abs(a[i] - a[i + 1])

    print(res * 2)