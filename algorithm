import sys
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write


max_val = 2147483647


def dijkstra():
    pq = []
    d[start_node] = 0
    heappush(pq, (d[start_node], start_node))

    while pq:
        c_cost, c_node = heappop(pq)

        for n_cost, n_node in v[c_node]:
            if check[c_node][n_node] == False and d[n_node] > d[c_node] + n_cost:
                d[n_node] = d[c_node] + n_cost
                heappush(pq, (d[n_node], n_node))


def reverse_dijkstra():
    pq = []
    heappush(pq, (d[end_node], end_node))

    while pq:
        c_cost, c_node = heappop(pq)

        for n_cost, n_node in rv[c_node]:
            if d[n_node] == d[c_node] - n_cost:
                check[n_node][c_node] = True
                heappush(pq, (d[n_node], n_node))


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    d = [max_val] * (n+1)
    check = [[False for _ in range(n+1)] for _ in range(n+1)]
    v = [[] for _ in range(n+1)]
    rv = [[] for _ in range(n+1)]

    start_node, end_node = map(int, input().split())

    for _ in range(m):
        a, b, c = map(int, input().split())
        v[a].append((c, b))
        rv[b].append((c, a))

    dijkstra()
    reverse_dijkstra()
    d = [max_val] * (n+1)
    dijkstra()

    if d[end_node] == max_val: print("-1\n")
    else: print("%d\n" % d[end_node])


