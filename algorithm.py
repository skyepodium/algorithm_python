from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)

        while original in s:
            original *= 2

        return original


sl = Solution()
nums = [1,16,13,19,12,10]
original = 2
res = sl.findFinalValue(nums, original)

print('res', res)