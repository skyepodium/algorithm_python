class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # 1. init
        n = len(s)
        res = ""

        # 2. loop
        for i in range(n):
            for j in range(i+1, n+1):
                # 1) set
                cur = s[i:j]
                se = set(cur)
                is_nice = True

                # 2) check
                for c in list(se):
                    if (c == c.lower() and c.upper() not in se) or (c == c.upper() and c.lower() not in se):
                        is_nice = False
                        break

                if is_nice:
                    if len(res) < len(cur):
                        res = cur

        return res

s = "YazaAay"
# s = "Bb"
# s = "c"

sl = Solution()
res = sl.longestNiceSubstring(s)

print('res', res)