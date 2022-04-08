from typing import List
from heapq import heappop, heappush, heapify

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = nums
        heapify(self.l)
        while len(self.l) > self.k:
            heappop(self.l)

    def add(self, val: int) -> int:
        heappush(self.l, val)

        if len(self.l) > self.k:
            heappop(self.l)

        return self.l[0]
