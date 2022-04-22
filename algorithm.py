from typing import List
from heapq import heappush, heappop

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # 1. exception
        if len(nums) < 2: return 0

        # 2. init
        pq = []

        # 3. loop
        for idx, val in enumerate(nums):
            heappush(pq, (-val, idx))

        first, idx = heappop(pq)
        second, _ = heappop(pq)
        first, second = -first, -second

        return idx if first >= second * 2 else -1

sl = Solution()
nums = [3,6,1,0]
nums = [1,2,3,4]
nums = [1]
res = sl.dominantIndex(nums)

print('res', res)


