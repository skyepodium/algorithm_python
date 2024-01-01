class Solution:
    def isHappy(self, n: int) -> bool:
        # 1. init
        seen = set()

        # 2. loop
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            next_val = 0
            while n > 0:
                next_val += (n % 10) ** 2
                n //= 10
            n = next_val

        return True


sl = Solution()
res = sl.isHappy(2)
print(res)
