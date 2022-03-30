from collections import Counter
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]

nums = [ 1, 3, 4, 2, 2]

sl = Solution()

res = sl.findDuplicate(nums)

print('res', res)