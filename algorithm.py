class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. init
        d = {}

        # 2. loop
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in d:
                return [d[remain], idx]
            else:
                d[num] = idx

