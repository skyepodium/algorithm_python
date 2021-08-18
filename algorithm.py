class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0. exception        
        if len(nums) <= 2:
            return max(nums)

        # 1. init
        d = [x for x in nums]
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])

        # 2. tabulation
        for i in range(2, len(nums)):
            d[i] = max(d[i - 1], d[i - 2] + nums[i])

        return d[len(nums) - 1]