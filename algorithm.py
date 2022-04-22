from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # 1. init
        n = len(matrix)

        # 2. loop
        for a in matrix:
            s = set()
            for b in a:
                if b < 1 or b > n: return False
                if b in s: return False
                s.add(b)

        for j in range(n):
            s = set()
            for i in range(n):
                b = matrix[i][j]
                if b < 1 or b > n: return False
                if b in s: return False
                s.add(b)

        return True


sl = Solution()
matrix = [[1,2,3],[3,1,2],[2,3,1]]
matrix = [[1,1,1],[1,2,3],[1,2,3]]
res = sl.checkValid(matrix)

print('res', res)