from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))

        d = {}
        for idx, val in enumerate(a):
            d[val] = idx + 1

        return [d[num] for num in arr]

sl = Solution()
arr = [40,10,20,30]
arr = [100,100,100]
arr = [37,12,28,9,100,56,80,5,12]
res = sl.arrayRankTransform(arr)
print('res', res)