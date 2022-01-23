class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1. init
        d = {}

        # 2. loop
        for idx, num in enumerate(nums):
            if num in d and idx - d[num] <= k:
                return True

            d[num] = idx

        return False
