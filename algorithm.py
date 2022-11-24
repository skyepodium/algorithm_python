from heapq import heappush, heappop

n, m, k = map(int, input().split())

v = [[] for _ in range(n+1)]
MAX_INT = int(1e12)
d = [[MAX_INT for _ in range(k+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    v[s].append((e, c))
    v[e].append((s, c))


def dijkstra(start_node):
    pq = []
    d[start_node][k] = 0
    heappush(pq, (d[start_node][k], start_node, k))

    while pq:
        cost, node, cnt = heappop(pq)

        if d[node][cnt] < cost:
            continue

        for next_node, next_cost in v[node]:
            # 1. not use
            if d[next_node][cnt] > d[node][cnt] + next_cost:
                d[next_node][cnt] = d[node][cnt] + next_cost
                heappush(pq, (d[next_node][cnt], next_node, cnt))

            # 2. use
            if cnt > 0:
                if d[next_node][cnt-1] > d[node][cnt]:
                    d[next_node][cnt-1] = d[node][cnt]
                    heappush(pq, (d[next_node][cnt-1], next_node, cnt-1))


dijkstra(1)

print(min(d[n]))