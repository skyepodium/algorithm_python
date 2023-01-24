from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. init
        n = len(nums2)
        next_big = [-1] * n
        index_dic = {}
        res = []

        # 2. loop
        for i in range(n):
            cur = nums2[i]
            index_dic[cur] = i
            for j in range(i+1, n):
                next_nums = nums2[j]
                if next_nums > cur:
                    if next_big[i] == -1:
                        next_big[i] = next_nums

        # 3. search
        for num in nums1:
            res.append(next_big[index_dic[num]])

        return res