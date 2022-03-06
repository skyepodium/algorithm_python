from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # 1. sort
        arr.sort()

        # 2. sub
        n = len(arr)
        cnt = int(n * 0.05)
        a = arr[cnt: n-cnt]

        return sum(a) / len(a)

arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]

sl = Solution()
res = sl.trimMean(arr)

print('res', res)