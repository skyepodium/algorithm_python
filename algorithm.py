from collections import deque

n, m = map(int, input().split())
v = [[] for _ in range(n+1)]
ind = [0] * (n + 1)
res = [1] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    ind[e] += 1
    v[s].append(e)

q = deque()
for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i)

while q:
    node = q.popleft()

    for n_node in v[node]:
        ind[n_node] -= 1
        res[n_node] = res[node] + 1

        if ind[n_node] == 0:
            q.append(n_node)

print(" ".join([str(i) for i in res[1:]]))
