n, m = map(int, input().split())

a = []

for i in range(1, m+1):
    if len(a) >= m: break
    for _ in range(i):
        if len(a) >= m: break
        a.append(i)

print(sum(a[n-1:]))