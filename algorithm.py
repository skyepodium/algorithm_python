from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. init
        res = []
        n = len(nums)
        dq = deque()

        # 2. loop
        for i in range(n):
            # 1) over size
            if dq and dq[0] == i - k: dq.popleft()

            # 2) make front biggest
            while dq and nums[dq[-1]] < nums[i]: dq.pop()

            # 3) insert
            dq.append(i)

            # 4) update
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

sl = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [1]
# k = 1
# nums = [1,3,1,2,0,5]
# k = 3
res = sl.maxSlidingWindow(nums, k)

print('res', res)