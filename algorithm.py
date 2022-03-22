import re

class Solution:
    def checkString(self, s: str) -> bool:
        return len(re.findall("ba", s)) < 1

sl = Solution()
s = "aaabbb"
res = sl.checkString(s)
print('res', res)