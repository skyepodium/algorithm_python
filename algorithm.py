from heapq import heappop, heappush
from collections import deque

# 1. input
n, m, p = map(int, input().split())
MAX_INT = int(1e10)
d = [MAX_INT] * (n+1)

# 2. make graph
v = [[] for _ in range(n+1)]
path = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    v[s].append((e, c))
    v[e].append((s, c))


# 3. dijkstra
def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    heappush(pq, (d[start_node], start_node))

    while pq:
        cost, node = heappop(pq)

        if d[node] < cost:
            continue

        for next_node, next_cost in v[node]:
            if d[next_node] > d[node] + next_cost:
                path[next_node] = [node]
                d[next_node] = d[node] + next_cost
                heappush(pq, (d[next_node], next_node))
            elif d[next_node] == d[node] + next_cost:
                path[next_node].append(node)


start_node, end_node = 1, n
dijkstra(start_node)

check = [False] * (n+1)

def bfs():
    q = deque()
    for node in path[end_node]:
        q.append(node)
        check[node] = True

    while q:
        node = q.popleft()

        for next_node in path[node]:
            if check[next_node]:
                continue
            check[next_node] = True
            q.append(next_node)

bfs()

if check[p]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
