from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 0. exception
        if n == 1:
            return 1

        # 1. init
        trust_count = Counter()

        # 2. loop
        for start, end in trust:
            trust_count[end] += 1
            trust_count[start] -= 1

        for person, cnt in trust_count.items():
            if cnt == n - 1:
                return person

        return -1

n = 2
trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

n = 3
trust = [[1,3],[2,3],[3,1]]

sl = Solution()
res = sl.findJudge(n, trust)

print('res', res)