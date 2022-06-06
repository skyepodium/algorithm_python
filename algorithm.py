from heapq import heappush, heappop

# 1. init
n = int(input())
MAX_VAl = 1000001 * 16
MAX_INT = 1 << n
v = []
d = [[MAX_VAl for _ in range(MAX_INT)] for _ in range(n)]
size = 1 << n
res = [MAX_VAl]

# 2. make graph
for _ in range(n):
    v.append(list(map(int, input().split())))

# 3. BFS
def dijkstra(node):
    d[node][1] = 0
    pq = []
    heappush(pq, (0, node, 1))

    while pq:
        cost, node, status = heappop(pq)

        if cost > d[node][status]: continue

        if status == size - 1 and v[node][0] != 0:
            res[0] = min(res[0], cost + v[node][0])

        for n_node in range(n):
            if v[node][n_node] == 0 or status & 1 << n_node: continue

            n_status = status | (1 << n_node)
            n_cost = d[node][status] + v[node][n_node]
            if d[n_node][n_status] > n_cost:
                d[n_node][n_status] = n_cost
                heappush(pq, (n_cost, n_node, n_status))
dijkstra(0)

print(res[0])

