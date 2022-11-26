n = int(input())

a = []
for _ in range(n):
    t = list(map(int, input().split()))
    a.append(t)

a.sort(key=lambda x: (x[0], x[1], x[2]))

for i in range(n):
    print(*a[i])