from typing import List
from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 1. init
        d = defaultdict(str)

        # 2. make graph
        for s, e in paths:
            d[s] = e

        # 3. search
        node = paths[0][0]
        while d[node]:
            n_node = d[node]
            node = n_node

        return node


sl = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["B","C"],["D","B"],["C","A"]]
paths = [["A","Z"]]
res = sl.destCity(paths)

print('res', res)