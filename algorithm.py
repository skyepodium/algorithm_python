import re

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return format(n, ",").replace(",", ".")


sl = Solution()

n = 10000
res = sl.thousandSeparator(n)

print('res', res)