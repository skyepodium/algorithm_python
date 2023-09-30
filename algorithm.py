from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 1. init
        n, m = len(matrix), len(matrix[0])

        def check(x, y):
            val = matrix[x][y]
            while x < n and y < m:
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1

            return True

        # 2. check
        for i in range(n):
            if not check(i, 0):
                return False

        for j in range(m):
            if not check(0, j):
                return False

        return True


sl = Solution()
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(sl.isToeplitzMatrix(matrix))
