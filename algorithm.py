class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # 1. init
        l = 0
        r = len(nums) - 1

        # 2. binary search
        def binary_search(l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l += 1
                elif nums[mid] > target:
                    r -= 1
                else:
                    return mid

            return -1

        return binary_search(l, r)