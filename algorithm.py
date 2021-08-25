class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 1. init
        n = len(num1) - 1
        m = len(num2) - 1

        # 2. loop
        carry = 0
        res = ""
        while n >= 0 or m >= 0 or carry > 0:
            a = 0
            if n >= 0:
                a = ord(num1[n]) - ord('0')
                n -= 1

            b = 0
            if m >= 0:
                b = ord(num2[m]) - ord('0')
                m -= 1

            carry, val = divmod(a + b + carry, 10)
            res += str(val)

        # 3. reverse
        return res[::-1]