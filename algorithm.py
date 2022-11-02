import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    res = 0
    s = set()

    for _ in range(n + m):
        c = int(input())
        if c in s:
            res += 1
        else:
            s.add(c)

    print(res)