from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set()
        res = []

        for x in permutations(nums):
            key = "".join([str(a) for a in x])
            if key not in s:
                s.add(key)
                res.append(x)

        return res



sl = Solution()

nums = [1, 1, 2]
res = sl.permuteUnique(nums)

print('res', res)