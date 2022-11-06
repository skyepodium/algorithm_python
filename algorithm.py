from collections import defaultdict

d = defaultdict(int)

a, b, c = map(int, input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            r = i + j + k
            d[r] += 1

r = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(r[0][0])