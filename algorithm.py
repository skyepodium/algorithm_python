from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        return [nums[nums[idx]] for idx in range(len(nums))]

sl = Solution()
nums = [0,2,1,5,3,4]
nums = [5,0,1,2,3,4]
res = sl.buildArray(nums)

print('res', res)