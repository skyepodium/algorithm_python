class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. init        
        l = 0
        r = len(nums) - 1

        # 2. sort
        d = [(idx, val) for idx, val in enumerate(nums)]
        d.sort(key=lambda x: x[1])

        # 3. two pointer
        while l < r:
            cur = d[l][1] + d[r][1]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return d[l][0], d[r][0]