class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. init
        d = [0] * (n + 1)

        # 2. top-down
        def dp(i):
            if i <= 2:
                return i

            if d[i] > 0:
                return d[i]

            d[i] = dp(i - 1) + dp(i - 2)
            return d[i]

        return dp(n)