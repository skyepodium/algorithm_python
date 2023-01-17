from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # 1. init
        res = -float(1e6)
        min_dist = float(1e6)

        # 2. loop
        for num in nums:
            abs_num = abs(num)
            if abs_num < min_dist:
                min_dist = abs_num
                res = num
            elif abs_num == min_dist:
                if num > res:
                    res = num

        return res