class Solution:
    def isThree(self, n: int) -> bool:
        # 1. init
        res = 0

        # 2. loop
        for i in range(1, n+1):
            if n % i == 0: res += 1

        return res == 3