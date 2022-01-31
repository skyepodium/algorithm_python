from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. init
        res = []
        c = sorted(Counter(nums).items(), key=lambda x: -x[1])
        cnt = 0
        for x in c:
            cnt += 1
            res.append(x[0])
            if cnt >= k:
                break

        return res

sl = Solution()
res = sl.topKFrequent([1, 1, 1, 2, 2, 3], 2)

print('res', res)