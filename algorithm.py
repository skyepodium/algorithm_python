class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 0. exception
        if len(pattern) != len(s.split(" ")):
            return False

        # 1. init
        d = {}
        w = {}

        # 2. loop
        for p, c in zip(pattern, s.split(" ")):
            if p in d and d[p] != c:
                return False

            if c in w and w[c] != p:
                return False

            d[p] = c
            w[c] = p

        return True

sl = Solution()
pattern = "abba"
s = "dog cat cat dog"


pattern = "abba"
s = "dog dog dog dog"

pattern = "aaa"
s = "aa aa aa aa"

res = sl.wordPattern(pattern, s)

print('res', res)