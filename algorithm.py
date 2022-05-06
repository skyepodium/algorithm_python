from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1. init
        c = Counter(nums)
        res = 0

        # 2. loop
        for num in nums:
            remain = k - num
            if num == remain and c[remain] <= 1: continue
            if c[remain] < 1 or c[num] < 1: continue

            res += 1
            c[remain] -= 1
            c[num] -= 1

        return res

sl = Solution()

nums = [1,2,3,4]
k = 5
nums = [3,1,3,4,3]
k = 6

nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3


res = sl.maxOperations(nums, k)

print('res', res)