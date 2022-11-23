from typing import List
from heapq import heappop, heappush

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 1. init
        pq = []
        res = []

        # 2. make max heap
        for h, k in people:
            heappush(pq, (-h, k))

        # 3. insert
        while pq:
            h, k = heappop(pq)
            res.insert(k, [-h, k])

        return res

