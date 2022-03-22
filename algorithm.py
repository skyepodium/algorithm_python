class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 1. init
        res = 0
        cur = 0
        prev = -1

        # 2. loop
        for num in nums:
            if num > prev:cur += num
            else:
                cur = num
            prev = num

            res = max(res, cur)

        return res