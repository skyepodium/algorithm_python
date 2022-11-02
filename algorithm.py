from collections import deque

a, b = map(int, input().split())
n = int(input())

MAX_INT = 1001
check = [-1 for _ in range(MAX_INT)]
q = deque()
check[a] = 0
q.append(a)

for _ in range(n):
    c = int(input())
    check[c] = 1 if c != a else 0
    q.append(c)

def bfs():
    while q:
        node = q.popleft()

        l, r = node - 1, node + 1

        if l >= 1 and check[l] == -1:
            check[l] = check[node] + 1
            q.append(l)
        if r < MAX_INT and check[r] == -1:
            check[r] = check[node] + 1
            q.append(r)

bfs()

print(check[b])