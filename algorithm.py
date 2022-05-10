class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1. init
        res = []
        n = len(nums)

        # 2. loop
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j: continue
                if nums[i] > nums[j]: cnt += 1
            res.append(cnt)

        return res