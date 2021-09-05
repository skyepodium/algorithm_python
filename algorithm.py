class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, 2) + int(b, 2)

        res = ""
        while c > 0:
            res += str(c % 2)
            c //= 2

        return "0" if res == "" else res[::-1]        