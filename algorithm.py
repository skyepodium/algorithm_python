class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # 1. init
        res = []

        # 2. loop
        for i in range(0, len(nums), 2):
            freq, num = nums[i], nums[i + 1]
            for _ in range(freq):
                res.append(num)

        return res
