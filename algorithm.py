from typing import List
from collections import deque

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. init
        dq = deque(sorted(people, reverse=True))
        res = 0

        # 2. loop
        while dq:
            front = dq.popleft()
            if dq and front + dq[-1] <= limit:
                dq.pop()
            res += 1

        return res

sl = Solution()
people = [1, 2]
limit = 3
people = [3,2,2,1]
limit = 3
# people = [3,5,3,4]
# limit = 5
# people = [5, 1, 4, 2]
# limit = 6
res = sl.numRescueBoats(people, limit)

print('res', res)