class Solution:
    def fib(self, n: int) -> int:
        # 1. init
        d = [0 for _ in range(n + 1)]

        # 2. fibo
        def fibo(i):
            if i <= 1:
                return i

            if d[i] != 0:
                return d[i]

            d[i] = fibo(i - 1) + fibo(i - 2)
            return d[i]

        return fibo(n)
