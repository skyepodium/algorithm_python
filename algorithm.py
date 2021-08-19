from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. init
        d = [0 for _ in range(len(nums))]
        res = d[0] = nums[0]

        # 2. tabulation
        for i in range(1, len(nums)):
            d[i] = max(nums[i], d[i - 1] + nums[i])
            res = max(res, d[i])

        return res
