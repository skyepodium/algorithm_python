from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        # 1. init
        n = len(nums)
        res = 0

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a%b)

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        for i in range(n):
            l = nums[i]
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k:
                    res += 1
                if l > k:
                    break

        return res

sl = Solution()
nums = [3,6,2,7,1]
k = 6
nums = [3]
k = 2
res = sl.subarrayLCM(nums, k)
print('res', res)