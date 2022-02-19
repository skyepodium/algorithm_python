from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return [[x, n-x] for x in range(1, n//2 + 1) if not "0" in str(x) and not "0" in str(n-x)][0]

sl = Solution()

res = sl.getNoZeroIntegers(11)

print('res', res)