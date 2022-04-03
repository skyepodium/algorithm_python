class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")[::-1].upper()
        n = len(s)

        t = ""
        for i in range(0, n, k):
            t += s[i:i+k] + "-"

        t = t[0:len(t) - 1]

        return t[::-1]




sl = Solution()
s = "5F3Z-2e-9-w"
k = 4

s = "2-5g-3-J"
k = 2
res = sl.licenseKeyFormatting(s, k)

print('res', res)