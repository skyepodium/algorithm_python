class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. init
        d = {}
        l = 0
        res = 0

        # 2. loop
        for r, cur in enumerate(s):
            # 1) dup check
            if cur in d:
                l = max(l, d[cur] + 1)

            # 2) insert
            d[cur] = r

            # 3) update
            res = max(res, r-l+1)

        return res

sl = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "abba"
res = sl.lengthOfLongestSubstring(s)
print('res', res)

