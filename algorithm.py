class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 1. init
        num1 = num1[::-1]
        num2 = num2[::-1]

        # 2. swap with length
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        n = len(num1)
        m = len(num2)
        carry = 0
        res = ""

        # 3. loop
        for i in range(n):
            cur = 0

            cur += ord(num1[i]) - ord('0')

            if i < m:
                cur += ord(num2[i]) - ord('0')

            carry, val = divmod(cur + carry, 10)
            res += str(val)

        if carry > 0:
            res += str(carry)

        return str(res)[::-1]