from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        base = Counter(arr)

        return len(base) == len(set([cnt for cnt in base.values()]))

sl = Solution()
arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
res = sl.uniqueOccurrences(arr)

print('res', res)