from typing import List
from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 1. init
        c = Counter(suits)
        r = Counter(ranks)

        if len(c) == 1:
            return "Flush"

        for key, cnt in r.items():
            if cnt >= 3:
                return "Three of a Kind"

        for key, cnt in r.items():
            if cnt >= 2:
                return "Pair"

        return "High Card"

sl = Solution()
ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]

# ranks = [4,4,2,4,4]
# suits = ["d","a","a","b","c"]

ranks = [10,10,2,12,9]
suits = ["a","b","c","a","d"]

res = sl.bestHand(ranks, suits)

print('res', res)