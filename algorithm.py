from collections import deque

f, s, g, u, d = map(int, input().split())

q = deque()
check = {}

def bfs():
    while q:
        cur = q.popleft()

        l, r = cur - d, cur + u
        if l > 0 and l not in check:
            cost = check[cur]
            n_cost = cost + 1
            check[l] = n_cost
            q.append(l)

        if r <= f and r not in check:
            cost = check[cur]
            n_cost = cost + 1
            check[r] = n_cost
            q.append(r)


check[s] = 0
q.append(s)
bfs()

if g not in check:
    print("use the stairs")
else:
    print(check[g])

