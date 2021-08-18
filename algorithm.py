class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. exception
        if not matrix:
            return -1

        # 2. init
        i = 0
        j = len(matrix[0]) - 1
        n = len(matrix)
        m = len(matrix[0])

        # 3. loop
        while i < n and j >= 0:
            cur = matrix[i][j]

            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else:
                return True

        return False