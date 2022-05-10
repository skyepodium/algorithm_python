from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: return []

        # 1. init
        res = []

        # 2. loop
        cnt = 0
        t = []
        for o in original:
            t.append(o)
            cnt += 1
            if cnt >= n:
                cnt = 0
                res.append(t[::])
                t = []

        return res



original = [1,2,3,4]

m = 2
n = 2

original = [1,2,3]
m = 1
n = 3

original = [1,2]
m = 1
n = 1

sl = Solution()

res = sl.construct2DArray(original, m, n)

print('res', res)