class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0] * (n+1)

        def go(n):
            if n == 0:
                return 0

            if n == 1 or n == 2:
                return 1

            if d[n] > 0:
                return d[n]

            d[n] = go(n - 1) + go(n - 2) + go(n - 3)
            return d[n]

        return go(n)

sl = Solution()
n = 25
print(sl.tribonacci(n))