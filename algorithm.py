class Solution:
    def climbStairs(self, n: int) -> int:
        # 0. exception
        if n <= 2:
            return n

        # 1. init
        d = [0] * (n+1)
        d[0] = 1
        d[1] = 1
        d[2] = 2

        # 2. loop
        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]

        return d[n]