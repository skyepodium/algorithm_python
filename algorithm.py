class Solution:
    def isHappy(self, n: int) -> bool:
        # 1. init
        s = set()

        # 2. squared_sum
        def squared_sum(num: int) -> int:
            num = str(num)
            res = 0

            for c in num:
                res += (ord(c) - ord('0')) ** 2

            return res

        # 3. loop
        while n not in s:
            s.add(n)
            n = squared_sum(n)
            if n == 1:
                return True

        return False