from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 1. init
        n = len(nums)
        res = 0
        s = set(nums)

        # 3. loop
        for j in range(1, n-1):
            if nums[j] - diff in s and nums[j] + diff in s:
                res += 1

        return res

nums = [0,1,4,6,7,10]
diff = 3

sl = Solution()
res = sl.arithmeticTriplets(nums, diff)
print('res', res)