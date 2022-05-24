from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. init
        check = [False for _ in range(n)]
        v = [[] for _ in range(n)]

        # 2. make graph
        for s, e in edges:
            v[s].append(e)
            v[e].append(s)

        # 3. DFS
        def dfs(node):
            check[node] = True
            for n_node in v[node]:
                if check[n_node]: continue
                dfs(n_node)

        dfs(source)

        return check[destination]

