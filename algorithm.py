from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx % 10 == val:
                return idx

        return -1

nums = [0, 1, 2]
# nums = [4,3,2,1]

sl = Solution()
print(sl.smallestEqual(nums))