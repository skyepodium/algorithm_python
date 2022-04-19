class Solution:
    def findGCD(self, nums: List[int]) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        return gcd(min(nums), max(nums))