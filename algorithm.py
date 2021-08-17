class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # 1. binary_search
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1

        return binary_search(0, len(nums) - 1)