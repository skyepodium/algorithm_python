class Solution:
    def numSquares(self, n: int) -> int:
        # 1. init
        sq_nums = []
        d = [10000 for _ in range(n + 1)]

        # 2. make sq_num
        for i in range(1, 101):
            sq_num = i * i
            sq_nums.append(sq_num)
            if sq_num <= n:
                d[sq_num] = 1

        # 3. bottom up
        for i in range(1, n + 1):
            for sq in sq_nums:
                if i + sq <= n:
                    d[i + sq] = min(d[i] + 1, d[i + sq])

        return d[n]