import re

class Solution:
    def countSegments(self, s: str) -> int:
        if s.strip() == "": return 0

        return len(re.split(" +", s.strip()))


sl = Solution()
s = "Of all the gin joints in all the towns in all the world,   "
res = sl.countSegments(s)

print('res', res)