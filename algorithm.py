from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # 1. init
        c = Counter(arr)

        # 2. find lucky
        lucky = -1
        for k, v in c.items():
            if k == v:
                lucky = max(lucky, k)

        return lucky
