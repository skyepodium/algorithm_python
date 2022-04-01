from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        max_val = max(target)
        idx = 0

        for t in range(1, n + 1):
            if t > max_val: break

            res.append("Push")
            if t is not target[idx]:
                res.append("Pop")
            else:
                idx += 1

        return res

sl = Solution()

target = [1,3]
n = 3
target = [1,2]
n = 4
target = [2, 3, 4]
n = 4
res = sl.buildArray(target, n)

print('res', res)