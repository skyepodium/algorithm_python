class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 0. exception
        if len(s) < 2 or s == s[::-1]: return s

        # 1. init
        res = ""

        # 2. get_max_len
        def get_max_len(l, r):
            while l >= 0 and r <= len(s) and s[l] == s[r-1]:
                l -= 1
                r += 1

            return s[l+1:r-1]

        # 3. loop
        for i in range(len(s)):
            res = max(res,
                      get_max_len(i, i+1),
                      get_max_len(i, i+2),
                      key=len)

        return res

s = "babad"

sl = Solution()

res = sl.longestPalindrome(s)

print('res', res)