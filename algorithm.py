from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 1. init
        n = len(code)
        res = [0] * n

        # 2. loop
        if k > 0:
            for i in range(n):
                for j in range(1, abs(k)+1):
                    res[i] += code[(i + j) % n]
        elif k < 0:
            for i in range(n):
                for j in range(1, abs(k)+1):
                    res[i] += code[(i - j) % n]

        return res

sl = Solution()

code = [5,7,1,4]
k = 3

code = [1,2,3,4]
k = 0

code = [2,4,9,3]
k = -2

print(sl.decrypt(code, k))
