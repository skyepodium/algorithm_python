from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 1. init
        res = 0

        # 2. loop
        for g in grid:
            for num in g:
                if num < 0:
                    res += 1

        return res