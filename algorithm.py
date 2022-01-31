from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. init
        d = {}
        res = []
        cnt = 0

        # 2. cnt
        for w in words:
            if w in d: d[w] += 1
            else: d[w] = 1

        # 3. sort
        c = sorted(d.items(), key=lambda x: (-x[1], x[0]))

        # 4. result
        for x in c:
            if cnt >= k: break
            res.append(x[0])
            cnt += 1

        return res
