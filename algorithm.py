from heapq import heappop, heappush
from collections import deque

# 1. input
n, m = map(int, input().split())
MAX_INT = int(1e10)
d = [MAX_INT for _ in range(n+1)]
res = []
path = [[] for _ in range(n+1)]
used_edge = []
check = [False] * (n+1)
DISABLED_EDGE_IDX = 0
MIN_DIST, MAX_DIST = MAX_INT, 0

# 2. make graph
v = [[] for _ in range(n+1)]
for edge_idx in range(1, m+1):
    s, e, c = map(int, input().split())
    v[s].append((e, c, edge_idx))
    v[e].append((s, c, edge_idx))


def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    heappush(pq, (d[start_node], start_node))


    while pq:
        cost, node = heappop(pq)

        if d[node] < cost:
            continue

        for next_node, next_cost, next_edge_idx in v[node]:
            if DISABLED_EDGE_IDX == next_edge_idx:
                continue

            if d[next_node] > d[node] + next_cost:
                path[next_node] = [(node, next_edge_idx)]
                d[next_node] = d[node] + next_cost
                heappush(pq, (d[next_node], next_node))
            elif d[next_node] == d[node] + next_cost:
                path[next_node].append((node, next_edge_idx))

dijkstra(1)
MIN_DIST = d[n]

def bfs(end_node):
    q = deque()
    check[end_node] = True
    for next_node, next_edge_idx in path[end_node]:
        q.append(next_node)
        check[next_node] = True
        used_edge.append(next_edge_idx)

    while q:
        node = q.popleft()

        for next_node, next_edge_idx in path[node]:
            if check[next_node]:
                continue
            check[next_node] = True
            used_edge.append(next_edge_idx)
            q.append(next_node)

bfs(n)

for edge_idx in used_edge:
    DISABLED_EDGE_IDX = edge_idx
    d = [MAX_INT for _ in range(n + 1)]
    dijkstra(1)
    MAX_DIST = max(MAX_DIST, d[n])

if MAX_DIST == MAX_INT:
    print(-1)
else:
    print(MAX_DIST - MIN_DIST)