from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1. init
        n = len(nums)
        d = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and d[j] + 1 > d[i]:
                    d[i] = d[j] + 1

        return max(d)



sl = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
res = sl.lengthOfLIS(nums)

print('res', res)