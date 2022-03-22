from typing import List
from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 1. init
        c = Counter()

        # 2. loop
        for a, b in edges:
            c[a] += 1
            c[b] += 1

        return c.most_common()[0][0]


sl = Solution()
edges = [[1,2],[2,3],[4,2]]
edges = [[1,2],[5,1],[1,3],[1,4]]
res = sl.findCenter(edges)

print('res', res)