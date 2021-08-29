class Solution:
    def reverseBits(self, n: int) -> int:
        def bit_to_str(num):
            res = ""
            while num > 0:
                res += str(num % 2)
                num //= 2

            return res[::-1].zfill(32)[::-1]

        val = bit_to_str(n)

        return int(val, 2)