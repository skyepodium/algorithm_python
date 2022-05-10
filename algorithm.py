from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1. init
        max_int = 101
        c = [0 for _ in range(max_int)]
        d = [0 for _ in range(max_int)]
        res = []

        # 2. loop
        for num in nums:
            c[num] += 1

        prev = 0
        for i in range(max_int):
            if c[i] != 0:
                d[i], prev = prev, c[i] + prev

        for num in nums:
            res.append(d[num])

        return res



sl = Solution()
nums = [8,1,2,2,3]
nums = [6,5,4,8]
nums = [7,7,7,7]
res = sl.smallerNumbersThanCurrent(nums)

print('res', res)