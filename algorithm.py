from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 1. init
        a_set, b_set = set(nums1), set(nums2)

        return [list(a_set - b_set), list(b_set - a_set)]

sl = Solution()

nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

res = sl.findDifference(nums1, nums2)

print('res', res)