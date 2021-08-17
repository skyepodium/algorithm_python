class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1. binary_search
        def binary_search(l, r):
            # not overflow
            if l <= r:
                mid = l + (r - l) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, r)
                elif nums[mid] > target:
                    return binary_search(l, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)
