class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 1. init
        n = len(nums)

        # 2. bubble sort
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp



