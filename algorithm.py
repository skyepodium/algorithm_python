from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 1. init
        n = len(p)
        base = Counter(p)
        c = Counter()
        res = []

        # 2. loop
        for i in range(len(s)):
            # 1) cur
            cur = s[i]

            # 2) update
            c[cur] += 1

            if i >= n - 1:
                if c == base:
                    res.append(i - n + 1)
                c[s[i-n+1]] -= 1

        return res
