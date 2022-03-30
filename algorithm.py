from typing import List
from collections import Counter

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (Counter([x for x in range(len(nums) + 1)]) - Counter(nums)).most_common()[0][0]


sl = Solution()
nums = [3, 0, 1]
res = sl.missingNumber(nums)

print('res', res)