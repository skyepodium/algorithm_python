class Solution:
    def addDigits(self, num: int) -> int:
        # 1. loop
        while num >= 10:
            n = num
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            num = res

        return num

sl = Solution()

res = sl.addDigits(0)

print('res', res)