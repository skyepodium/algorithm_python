class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 0. exception
        if n == 0: return 1

        # 1. init
        res = 0
        base = 0

        # 2. loop
        while n > 0:
            res += 2 ** base if n % 2 == 0 else 0
            n //= 2
            base += 1

        return res