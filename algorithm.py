from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # 1. init
        d = [0] * (n+1)

        # 2. count indegree
        for s, e in edges:
            d[s] += 1
            d[e] += 1

        # 3. sort