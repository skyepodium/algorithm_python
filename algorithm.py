class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 1. init
        n = len(grid)
        m = len(grid[0])
        res = 0

        # 2. sort
        for i in range(n):
            grid[i].sort(reverse=True)

        # 2. find max
        max_val = 0
        for j in range(m):
            max_val = 0
            for i in range(n):
                max_val = max(max_val, grid[i][j])
            res += max_val

        return res