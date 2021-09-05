class Solution:
    def countPrimes(self, n: int) -> int:
        # 0. exception
        if n <= 2:
            return 0

        # 1. init
        d = [1 for _ in range(n + 1)]

        # 2.eratos
        def eratos():
            for i in range(2, int(sqrt(n)) + 1):
                for j in range(i * 2, n + 1, i):
                    if d[j] == 1:
                        d[j] = 0

        eratos()

        return sum(d[2:n])
