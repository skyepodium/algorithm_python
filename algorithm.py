class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. init
        n, m = len(text1), len(text2)
        d = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # 2. loop
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])

        return d[n][m]


sl = Solution()
text1 = "abcde"
text2 = "ace"

text1 = "abc"
text2 = "abc"

text1 = "abc"
text2 = "def"

res = sl.longestCommonSubsequence(text1, text2)

print('res', res)