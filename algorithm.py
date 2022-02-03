import bisect
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 1. init
        res = 0
        f = []
        s = []

        # 2. loop
        for i in nums1:
            for j in nums2:
                f.append(i+j)
        for i in nums3:
            for j in nums4:
                s.append(i+j)

        # 3. sort
        f.sort()
        s.sort()

        # 4. loop
        for num in f:
            target = -num

            l_idx = bisect.bisect_left(s, target)
            r_idx = bisect.bisect_right(s, target)
            res += r_idx - l_idx

        return res



