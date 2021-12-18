class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def go(num):
            p = 1
            s = 0

            while num > 0:
                x = num % 10
                p *= x
                s += x
                num //= 10

            return p - s

        return go(n)



