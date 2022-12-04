from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # 1. init
        n = len(nums)
        d = [0] * (n+1)
        d[0] = nums[0]
        min_average_diff = int(1e10)
        min_idx = 0

        # 2. cumulative sum
        for i in range(1, n):
            d[i] = d[i-1] + nums[i]

        # 3. update
        for i in range(n):
            l = d[i] // (i+1)
            r = (d[n-1] - d[i]) // (n-i-1) if i < n-1 else 0

            average_diff = abs(l - r)
            if min_average_diff > average_diff:
                min_average_diff = average_diff
                min_idx = i

        return min_idx

nums = [2,5,3,9,5,3]
nums = [0]
nums = [4,2,0]

sl = Solution()
res = sl.minimumAverageDifference(nums)
print('res', res)