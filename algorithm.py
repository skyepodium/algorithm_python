from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        for g in grid:
            for num in g:
                if num < 0:
                    res += 1

        return res