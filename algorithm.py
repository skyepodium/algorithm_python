from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # 1. init
        res = []
        if n % 2 != 0:
            res.append(0)

        # 2. loop
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)

        return res