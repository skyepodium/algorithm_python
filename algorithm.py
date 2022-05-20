from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. init
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        d = [[0 for _ in range(m+1)] for _ in range(n+1)]
        if obstacleGrid[0][0] == 1:
            return 0
        d[1][1] = 1

        # 2. loop
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1: continue
                if obstacleGrid[i-1][j-1] == 1: continue

                d[i][j] = d[i-1][j] + d[i][j-1]

        return d[n][m]


sl = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[1]]
res = sl.uniquePathsWithObstacles(obstacleGrid)

print('res', res)