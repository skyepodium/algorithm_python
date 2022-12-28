class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. init
        d = {}
        res = []

        # 2. loop
        for idx, num in enumerate(nums):
            remain = target - num

            if remain in d:
                return [d[remain], idx]

            d[num] = idx

        return res
