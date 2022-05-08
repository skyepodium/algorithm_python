class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # 1. init
        res = 0

        # 2. loop
        while num1 > 0 and num2 > 0:
            res += 1
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1

        return res

sl = Solution()

num1 = 2
num2 = 3

num1 = 10
num2 = 10

res = sl.countOperations(num1, num2)

print('res', res)