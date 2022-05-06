from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1. init
        n = len(nums)
        res = 0

        # 2. sort
        nums.sort()

        # 3. two pointer
        l, r = 0, n - 1
        while l < r:
            cur = nums[l] + nums[r]
            if cur == k:
                res += 1
                l += 1
                r -= 1
            elif cur < k:
                l += 1
            else:
                r -= 1

        return res

sl = Solution()

nums = [1,2,3,4]
k = 5
nums = [3,1,3,4,3]
k = 6


res = sl.maxOperations(nums, k)

print('res', res)