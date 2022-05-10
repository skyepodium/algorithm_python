from typing import List
from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1. init
        c = sorted(Counter(nums).items(), key=lambda x: x[0])
        n = len(c)
        d = [0 for _ in range(n)]
        for i in range(1, n, 1):
            d[i] = d[i-1] + c[i-1][1]
        res = []

        # 2. binary_search
        def binary_search(target):
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                cur = c[mid][0]
                if cur < target:
                    l = mid + 1
                elif cur == target:
                    return mid
                else:
                    r = mid - 1

        # 3. loop
        for num in nums:
            idx = binary_search(num)
            res.append(d[idx])

        return res

sl = Solution()
nums = [8,1,2,2,3]
nums = [6,5,4,8]
nums = [7,7,7,7]
res = sl.smallerNumbersThanCurrent(nums)

print('res', res)