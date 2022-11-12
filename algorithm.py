from collections import defaultdict

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # 1. init
        d = defaultdict(int)

        # 2. loop
        for c in s:
            d[c] += 1
            if d[c] >= 2:
                return c

        return ''