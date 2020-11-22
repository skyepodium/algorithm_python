from heapq import heappush, heappop


def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    heappush(pq, (d[start_node], start_node))

    while pq:
        c_cost, c_node = heappop(pq)

        for idx in range(1, 7):
            n_node = c_node + idx

            if n_node > 100: continue

            ladder_node = ladder[n_node]

            if ladder_node == -1:
                if d[n_node] > d[c_node] + 1:
                    d[n_node] = d[c_node] + 1
                    heappush(pq, (d[n_node], n_node))
            else:
                if d[ladder_node] > d[c_node] + 1:
                    d[ladder_node] = d[n_node] = d[c_node] + 1
                    heappush(pq, (d[ladder_node], ladder_node))


max_val = max_int = 101
n, m = map(int, input().split())
ladder = [-1 for _ in range(max_int)]
d = [max_val for _ in range(max_int)]

for i in range(n+m):
    start_point, end_point = map(int, input().split())

    ladder[start_point] = end_point

dijkstra(1)

print(d[100])
