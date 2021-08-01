class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        result = 0

        while l <= r:
            mid = (l + r) // 2

            val = mid * mid

            if val > x:
                r = mid - 1
            elif val == x:
                return mid
            else:
                result = mid
                l = mid + 1

        return result