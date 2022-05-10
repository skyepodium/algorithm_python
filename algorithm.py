from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 1. init
        max_int = 10
        check = [False for _ in range(max_int)]
        res = []

        # 2. recursive
        def go(cnt, l, sum_val):
            if sum_val > n:
                return

            if cnt >= k:
                if sum_val == n:
                    res.append(l[::])
                return

            for i in range(1, max_int):
                if not check[i]:
                    if l and l[-1] > i: continue

                    check[i] = True
                    l.append(i)
                    go(cnt + 1, l, sum_val + i)
                    check[i] = False
                    l.pop()

        go(0, [], 0)

        return res


sl = Solution()

k = 3
n = 7

k = 3
n = 9

k = 4
n = 1

k = 2
n = 18

res = sl.combinationSum3(k, n)

print('res', res)

