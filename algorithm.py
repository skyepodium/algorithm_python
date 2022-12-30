from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. init
        n = len(nums)

        # 2. binary search
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1