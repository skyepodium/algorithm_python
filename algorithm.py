from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        base = Counter([x for x in range(1, len(nums) + 1)])
        cur = Counter(nums)

        return [(cur - base).most_common()[0][0], (base - cur).most_common()[0][0]]

sl = Solution()
nums = [1,2,2,4]
nums = [1, 1]
res = sl.findErrorNums(nums)

print('res', res)
