class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 1. sort
        nums = list(set(nums))
        nums.sort(reverse=True)

        # 2. return
        return nums[0] if len(nums) < 3 else nums[2]