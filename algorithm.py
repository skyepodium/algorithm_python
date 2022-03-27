import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. init
        MIN_INT = -2147483648
        MAX_INT = 2147483647

        # 2. def
        def check(val):
            res = int(val.strip())
            if res < MIN_INT: res = MIN_INT
            elif res > MAX_INT: res = MAX_INT
            return res

        # step 1
        a = re.findall("^ +[0-9]+", s)
        if a:
            return check(a[0])

        # step 2
        b = re.findall("^ *[-+][0-9]+", s)
        if b:
            return check(b[0])

        # step 3
        c = re.findall("^[0-9]+ *", s)
        if c:
            return check(c[0])

        return 0


sl = Solution()
s = "42"
s = "-42"
s = "+42"
s = "+-12"
# s = "4193 with words"
# s = "words and 987"
# s = "   123 with  3"
s = "-91283472332"
# s = "   -42"
res = sl.myAtoi(s)

print('res', res)