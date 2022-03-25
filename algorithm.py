class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # 1. init
        n = len(nums)
        res = 0

        # 2. loop
        for i in range(n):
            for j in range(i + 1, n):
                start = nums[i]
                end = nums[j]
                if abs(start - end) == k: res += 1

        return res
