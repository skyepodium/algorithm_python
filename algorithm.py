from heapq import heappush, heappop
from collections import deque

MAX_N = 501
MAX_INT = int(1e12)

d = [MAX_INT] * MAX_N
p = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
path = [[] for _ in range(MAX_N)]


def dijkstra(start_node, n):
    d[start_node] = 0
    pq = []
    heappush(pq, (d[start_node], start_node))

    while pq:
        cost, node = heappop(pq)

        if d[node] < cost:
            continue

        for next_node in range(n):
            if next_node == node: continue
            next_cost = p[node][next_node]
            if next_cost == 0: continue

            if d[next_node] > d[node] + next_cost:
                path[next_node].clear()
                path[next_node].append(node)
                d[next_node] = d[node] + next_cost
                heappush(pq, (d[next_node], next_node))
            elif d[next_node] == d[node] + next_cost:
                path[next_node].append(node)


def remove_path(end_node):
    q = deque()
    q.append(end_node)

    while q:
        end_node = q.popleft()

        for start_node in path[end_node]:
            if p[start_node][end_node] > 0:
                p[start_node][end_node] = 0
                q.append(start_node)


while True:
    # 1. input
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    # 2. init
    for i in range(n):
        d[i] = MAX_INT
        path[i].clear()
        for j in range(n):
            p[i][j] = 0

    # 3. make graph
    start_node, end_node = map(int, input().split())
    for _ in range(m):
        s, e, c = map(int, input().split())
        p[s][e] = c

    dijkstra(start_node, n)

    remove_path(end_node)

    for i in range(n):
        d[i] = MAX_INT
        path[i].clear()

    dijkstra(start_node, n)

    print(d[end_node] if d[end_node] != MAX_INT else -1)