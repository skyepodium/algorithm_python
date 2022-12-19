from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. init
        check = [False] * (n+1)
        v = [[] for _ in range(n+1)]

        # 2. make graph
        for s, e in edges:
            v[s].append(e)
            v[e].append(s)

        # 3. dfs
        def dfs(node):
            check[node] = True
            for next_node in v[node]:
                if not check[next_node]:
                    dfs(next_node)

        dfs(source)

        return check[destination]