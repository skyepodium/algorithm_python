from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list((Counter(nums1) - (Counter(nums1) - Counter(nums2))).keys())