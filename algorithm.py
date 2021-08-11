import heapq


def dijkstra(node):
    d[node] = 0
    pq = []
    heapq.heappush(pq, (d[node], node))

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > d[node]: continue

        for n_cost, n_node in v[node]:
            if d[n_node] > d[node] + n_cost:
                d[n_node] = d[node] + n_cost
                heapq.heappush(pq, (d[n_node], n_node))


n = int(input())
m = int(input())

max_val = 100000 * 1000
v = [[] for _ in range(n+1)]
d = [max_val for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    v[a].append((c, b))

start_node, end_node = map(int, input().split())

dijkstra(start_node)

print(d[end_node])



