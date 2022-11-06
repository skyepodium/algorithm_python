n = int(input())

for _ in range(n):
    s, e = map(int, input().split())
    res = 0
    for i in range(s, e + 1):
        res += str(i).count("0")

    print(res)