import re

class Solution:
    def freqAlphabets(self, s: str) -> str:

        def get_alphabet(n):
            return f"{chr(ord('a') + n - 1)}"

        for num in range(26, -1, -1):
            pattern = f"{num}#" if num >= 10 else f"{num}"
            s = re.sub(pattern, get_alphabet(num), s)

        return s

sl = Solution()
s = "10#11#12"
s = "1326#"
res = sl.freqAlphabets(s)

print('res', res)