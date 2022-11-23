from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1. init
        cnt = Counter(nums)
        base = len(nums) / 3
        res = []

        # 2. loop
        for num, c in cnt.items():
            if c > base:
                res.append(num)

        return sorted(res)

