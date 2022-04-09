from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [a for a, b in sorted(Counter(words).items(), key=lambda x: -x[1])][:k]

sl = Solution()
nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
res = sl.topKFrequent(nums, k)

print('res', res)