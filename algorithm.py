class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # 1. init
        res = nums[0]

        # 2. xor
        for i in range(1, len(nums)):
            res ^= nums[i]
            print(nums[i], res)

        return res

sl = Solution()
nums = [4,1,2,1,2]
res = sl.singleNumber(nums)
print('res')