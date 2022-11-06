from collections import defaultdict

n, m, l = map(int, input().split())

d = defaultdict(int)
cur = 1
d[cur] = 1
res = 0


while True:
    if d[cur] >= m:
        break

    n_num = 0
    count = d[cur]
    if count % 2 == 1:
        n_num = (cur + l) % n
    else:
        n_num = (cur - l) % n

    res += 1
    cur = n_num
    d[cur] += 1

print(res)