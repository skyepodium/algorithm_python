from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. init
        banned_set = set(banned)
        paragraph = re.sub('[^a-zA-z ]', ' ', paragraph.lower())

        # 2. loop
        c = Counter([p for p in paragraph.split() if p not in banned_set])
        return c.most_common()[0][0]


sl = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
res = sl.mostCommonWord(paragraph, banned)

print('res', res)