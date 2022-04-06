from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        return [s[i:i+k] if i+k <= len(s) else s[i:i+k] + fill * (i+k - len(s)) for i in range(0, len(s), k)]

sl = Solution()
s = "abcdefghi"
k = 3
fill = "x"

s = "abcdefghij"
k = 3
fill = "x"
res = sl.divideString(s, k, fill)

print('res', res)