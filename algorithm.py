class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # 1. init
        n = len(nums)
        res = -1

        # 2. loop
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, nums[i] - nums[j])

        return res    