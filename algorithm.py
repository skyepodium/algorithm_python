from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 1. init
        res = 0
        d = defaultdict(int)

        # 2. loop
        for i in nums1:
            for j in nums2:
                d[i+j] += 1

        for i in nums3:
            for j in nums4:
                res += d[0 - (i+j)]

        return res



