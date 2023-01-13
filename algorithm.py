import re


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # 1. init
        ones = re.split("[0+]", s)
        zeroes = re.split("[1+]", s)
        one_max_length = 0
        zero_max_length = 0

        # 2. loop
        for one in ones:
            if one == '':
                continue

            one_max_length = max(one_max_length, len(one))

        for zero in zeroes:
            if zero == '':
                continue

            zero_max_length = max(zero_max_length, len(zero))

        return one_max_length > zero_max_length


sl = Solution()
s = "1101"
s = "111000"
s = "110100010"
res = sl.checkZeroOnes(s)

print('res', res)
