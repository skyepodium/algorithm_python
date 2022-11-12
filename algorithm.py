class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # 1. decimal_to_base
        def decimal_to_base(num, base):
            res = ""
            while num > 0:
                res += str(num % base)
                num //= base
            return res

        # 2. loop
        for i in range(2, n-1):
            base_str = str(decimal_to_base(n, i))
            if base_str != base_str[::-1]:
                return False

        return True

sl = Solution()
n = 4
n = 9
print(sl.isStrictlyPalindromic(n))