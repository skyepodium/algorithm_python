from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sorted(list(Counter(nums).items()), key=lambda x: x[1])[0][0]



sl = Solution()
nums = [2, 2, 1]
res = sl.singleNumber(nums)

print('res', res)
