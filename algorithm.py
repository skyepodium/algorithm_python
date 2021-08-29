from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. init
        max_val = 10001
        res = 0
        d = [max_val for _ in range(n + 1)]
        v = [[] for _ in range(n + 1)]

        # 2. make graph
        for s, e, c in times:
            v[s].append((c, e))

        # 3. dijkstra
        def dijkstra(start_node):
            pq = []
            d[start_node] = 0
            heappush(pq, (d[start_node], start_node))

            while pq:
                cost, node = heappop(pq)

                if d[node] < cost:
                    continue

                for n_cost, n_node in v[node]:
                    if d[n_node] > d[node] + n_cost:
                        d[n_node] = d[node] + n_cost
                        heappush(pq, (d[n_node], n_node))

        dijkstra(k)

        # 4. check
        for i in range(1, n + 1):
            res = max(res, d[i])

        return -1 if res == max_val else res
