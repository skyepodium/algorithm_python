from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # 1. init
        s = set()

        # 2. loop
        for i in range(len(nums) - 1):
            val = nums[i] + nums[i+1]
            if val in s:
                return True

            s.add(val)

        return False

