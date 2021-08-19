class Solution:
    def climbStairs(self, n: int) -> int:

        d = [0 for _ in range(n + 1)]

        def go(i):
            if i <= 2:
                return i

            if d[i] > 0:
                return d[i]

            d[i] = go(i - 2) + go(i - 1)

            return d[i]

        return go(n)