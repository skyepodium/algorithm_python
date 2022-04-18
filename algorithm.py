from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increased = sorted(nums)
        decreased = sorted(nums, reverse=True)

        return nums == increased or nums == decreased

sl = Solution()
nums = [1, 2, 2, 3]
res = sl.isMonotonic(nums)

print('res', res)