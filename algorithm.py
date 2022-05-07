from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 1. init
        prev = 0
        res = 0

        # 2. loop
        for g in gain:
            prev = prev + g
            res = max(res, prev)

        return res

sl = Solution()

gain = [-5,1,5,0,-7]

res = sl.largestAltitude(gain)

print('res', res)