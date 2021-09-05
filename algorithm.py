class Solution:
    def countBits(self, n: int) -> List[int]:
        # 1. init
        res = []

        # 2. loop
        for i in range(n + 1):
            val = bin(i)
            res.append(str(val).count('1'))

        return res