from heapq import heappop, heappush

n, m = map(int, input().split())
p = list(map(int, input().split()))
MAX_INT = int(1e12)
d = [MAX_INT] * (n + 1)
v = [[] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    v[s].append((e, c))
    v[e].append((s, c))


def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    pq.append((d[start_node], start_node))

    while pq:
        cost, node = heappop(pq)
        if cost > d[node]:
            continue

        for next_node, next_cost in v[node]:
            if next_node != n-1 and p[next_node] == 1: continue
            if d[next_node] > d[node] + next_cost:
                d[next_node] = d[node] + next_cost
                heappush(pq, (d[next_node], next_node))


dijkstra(0)
print(d[n-1] if d[n-1] != MAX_INT else -1)