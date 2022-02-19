from typing import List

from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 1. init
        d = defaultdict(int)
        res = 0

        # 2. counter
        for a, b in dominoes:
            if a > b: a, b = b, a
            d[f"{a}{b}"] += 1

        # 3. count
        for x in d.values():
            if x > 1:
                res += (x * (x - 1)) // 2

        return res

sl = Solution()
dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
res = sl.numEquivDominoPairs(dominoes)

print('res', res)