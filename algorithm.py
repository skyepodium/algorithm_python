class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1. init
        res = 1
        sqrt = int(num ** 0.5)

        # 2. check
        for i in range(2, sqrt + 1):
            if num % i == 0:
                res += i
                res += num // i

        if sqrt == num ** 0.5:
            res -= sqrt
            
        # 3. return
        return res == num


# 1 2 3

sl = Solution()
num = 1
num = 9
print(sl.checkPerfectNumber(num))
