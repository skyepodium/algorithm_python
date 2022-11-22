from heapq import heappush, heappop

n, m = map(int, input().split())
v = [[] for _ in range(n+1)]
MAX_INT = int(1e9)
d = [MAX_INT] * (n+1)

for _ in range(m):
    s, e, c = map(int, input().split())
    v[s].append((e, c))
    v[e].append((s, c))

def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    heappush(pq, (d[start_node], start_node))

    while pq:
        cost, node = heappop(pq)

        if d[node] < cost:
            continue

        for next_node, n_cost in v[node]:
            if d[next_node] > d[node] + n_cost:
                d[next_node] = d[node] + n_cost
                heappush(pq, (d[next_node], next_node))

dijkstra(1)

print(d[n])