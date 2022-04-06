from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([x for x, cnt in Counter(nums).items() if cnt == 1])


nums = [1,2,3,2]

sl = Solution()

res = sl.sumOfUnique(nums)

print('res', res)