from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 1. init
        d = defaultdict(int)
        d[0] = 1
        res = 0
        sum = 0
        found = False

        # 2. loop
        for num in nums:
            if num < k:
                sum -= 1
            elif num > k:
                sum += 1
            else:
                found = True
            if found:
                res += d[sum] + d[sum - 1]
            else:
                d[sum] += 1

        return res

nums = [3,2,1,4,5]
k = 4

nums = [2,3,1]
k = 3

sl = Solution()
res = sl.countSubarrays(nums, k)
print('res', res)
