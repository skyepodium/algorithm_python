from collections import deque

n = int(input())
q = deque([num for num in range(1, n+1)])

res = []
while q:
    res.append(q.popleft())
    if q:
        q.append(q.popleft())

print(*res)