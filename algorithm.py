class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # 1. init
        res = 0

        # 2. loop
        for i in range(len(s) - 2):
            if len(set(s[i:i+3])) >= 3:
                res += 1

        return res

sl = Solution()
s = "xyzzaz"
s = "aababcabc"
res = sl.countGoodSubstrings(s)

print('res', res)