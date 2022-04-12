from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # 1. init
        pq = []
        res = 0

        for c in cost:
            heappush(pq, -c)

        # 2. loop
        while pq:
            if len(pq) >= 2:
                a = -heappop(pq)
                b = -heappop(pq)
                res += a + b

                if len(pq) >= 1: heappop(pq)
            else:
                break

        return res - sum(pq)
