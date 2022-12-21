from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # 1. init
        res = len(nums)

        # 2. loop
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))

        return res