from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 1. init
        n, m = len(matrix), len(matrix[0])
        MAX_VAL = int(1e10)
        d = [[MAX_VAL for _ in range(m)] for _ in range(n)]

        # 2. bottom-up
        for i in range(n):
            for j in range(m):
                # 1) exception
                if i == 0:
                    d[i][j] = matrix[i][j]
                    continue

                # 2) min update
                c = d[i-1][j]
                l = d[i-1][j-1] if j-1 >= 0 else MAX_VAL
                r = d[i-1][j+1] if j+1 < m else MAX_VAL
                d[i][j] = matrix[i][j] + min(l, c, r)

        return min(d[n-1])


sl = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]
res = sl.minFallingPathSum(matrix)

print('res', res)