from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # 1. init
        max_val = 1000001
        res = max_val
        d = [[max_val for _ in range(k + 2)] for _ in range(n + 1)]
        v = [[] for _ in range(n + 1)]

        # 2. make_graph
        for s, e, c in flights:
            v[s].append((c, 0, e))

        def dijkstra(start_node):
            d[start_node][0] = 0
            pq = []
            heappush(pq, (d[start_node][0], 0, start_node))

            while pq:
                cost, cnt, node = heappop(pq)

                if d[node][cnt] < cost:
                    continue

                for n_cost, n_cnt, n_node in v[node]:
                    if cnt + 1 <= k + 1 and d[n_node][cnt + 1] > d[node][cnt] + n_cost:
                        d[n_node][cnt + 1] = d[node][cnt] + n_cost
                        heappush(pq, (d[n_node][cnt + 1], cnt + 1, n_node))

        dijkstra(src)

        # 3. check loop
        for i in range(0, k + 2):
            res = min(res, d[dst][i])

        return res if res != max_val else -1


