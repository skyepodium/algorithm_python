from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 0. exception
        if len(s) < len(t):
            return ""

        # 1. init
        base = Counter(t)
        min_length = len(s) + 1
        res = ""

        # 2. loop
        cur = Counter()
        l = 0
        for r, c in enumerate(s):
            cur[c] += 1
            while len(base - cur) == 0:
                diff = r - l + 1
                if min_length > diff:
                    min_length = diff
                    res = s[l:r+1]

                if cur[s[l]] > 0:
                    cur[s[l]] -= 1
                l += 1

        return res

s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "a"

s = "a"
t = "aa"
#
s = "a"
t = "b"
#
s = "ab"
t = "A"

s = "abc"
t = "cba"

sl = Solution()
res = sl.minWindow(s, t)
print('res', res)