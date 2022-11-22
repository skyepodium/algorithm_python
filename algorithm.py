class Solution:
    def numSquares(self, n: int) -> int:
        # 1. init
        squares = set()
        d = [n] * (n + 1)

        # 2. loop
        for i in range(1, n+1):
            if int(i ** 0.5) ** 2 == i:
                squares.add(i)
                d[i] = 1

        # 3. bottom-up
        for i in range(1, n+1):
            for square in squares:
                diff = i - square
                if diff < 0:
                    continue
                d[i] = min(d[i], d[diff] + 1)

        return d[n]

sl = Solution()
n = 12
n = 13
res = sl.numSquares(n)
print('res', res)
