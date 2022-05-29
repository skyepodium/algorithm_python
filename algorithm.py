from typing import List
from itertools import zip_longest

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        res = []
        for e, o in zip_longest(sorted(nums[0::2]), sorted(nums[1::2], reverse=True)):
            if e: res.append(e)
            if o: res.append(o)
        return res

sl = Solution()
nums = [4,1,2,3]
nums = [2, 1]
nums = [5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21]
res = sl.sortEvenOdd(nums)

print('res', res)