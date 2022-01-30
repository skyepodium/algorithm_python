from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 1. init
        res = Counter(words[0])

        # 2. loop
        for w in words:
            res = res & Counter(w)

        return list(res.elements())

sl = Solution()

res = sl.commonChars(["cool","lock","cook"])

print('res', res)