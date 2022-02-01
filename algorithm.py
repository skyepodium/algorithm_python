class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 0. exception
        if n == 0: return 1

        # 1. init
        res = 0

        # 2. dec_to_bit
        def dec_to_bit(num):
            res = ""
            while num > 0:
                res += str(num % 2)
                num //= 2
            return res

        str_num = dec_to_bit(n)

        # 3. loop
        for i in range(len(str_num)):
            if str_num[i] == '0':
                res += 2 ** i

        return res
