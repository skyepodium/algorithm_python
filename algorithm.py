from collections import deque

n, m = map(int, input().split())
l = list(map(int, input().split()))
q = deque(l)

for _ in range(m):
    q.popleft()
    q.append(0)

print(*list(q))