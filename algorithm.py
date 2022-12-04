class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 1. init
        MAX_INT = int(1e14)
        d = [MAX_INT] * (n+1)
        v = [[] for _ in range(n+1)]

        # 2. make graph
        for s, e, c in roads:
            v[s].append((e, c))
            v[e].append((s, c))

        # 3. dijkstra
        def dijkstra(start_node):
            pq = []
            heappush(pq, (d[start_node], start_node))

            while pq:
                cost, node = heappop(pq)

                if d[node] < cost:
                    continue

                for n_node, n_cost in v[node]:
                    cost = min(cost, n_cost)
                    if d[n_node] > cost:
                        d[n_node] = cost
                        heappush(pq, (d[n_node], n_node))

        dijkstra(1)

        return d[n]