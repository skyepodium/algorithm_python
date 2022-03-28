class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1. init
        n = len(triangle)
        MAX_VAL = float(2e6 + 1)
        d = [[MAX_VAL for i in range(_+1)] for _ in range(n)]
        d[0][0] = triangle[0][0]

        # 2. loop
        for i, l in enumerate(triangle):
            if i == 0: continue

            for j, t in enumerate(l):
                if j == 0:
                    d[i][j] = d[i-1][j] + t
                elif j == i:
                    d[i][j] = d[i-1][j-1] + t
                else:
                    d[i][j] = min(d[i-1][j-1], d[i-1][j]) + t

        return int(min(d[n-1]))
