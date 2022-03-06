from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 1. init
        n = len(arr)
        res = [-1 for _ in range(n)]
        cur_max = arr[n-1]

        # 2. loop
        for i in reversed(range(n)):
            if i == n - 1: continue
            if arr[i+1] > cur_max: cur_max = arr[i+1]
            res[i] = cur_max

        return res


sl = Solution()
arr = [17,18,5,4,6,1]
res = sl.replaceElements(arr)

print('res', res)