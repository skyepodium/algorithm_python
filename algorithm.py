def dijkstra(graph, start, end):
    # initialize
    dist = {start: 0}
    prev = {}
    queue = []
    for node in graph:
        if node != start:
            dist[node] = float('inf')
        heapq.heappush(queue, (dist[node], node))
    # loop
    while queue:
        u = heapq.heappop(queue)[1]
        if u == end:
            break
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    # return
    return dist, prev