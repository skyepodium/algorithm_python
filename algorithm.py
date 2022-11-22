from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(l, r, nums, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        def upper_bound(l, r, nums, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l

        def binary_search(l, r, nums, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        idx = binary_search(0, len(nums)-1, nums, target)
        if idx == -1:
            return [-1, -1]

        l = lower_bound(0, len(nums), nums, target)
        r = upper_bound(0, len(nums), nums, target)

        return [l, r-1]

sl = Solution()
nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10]
target = 6
nums = []
target = 0
# nums = [2, 2]
# target = 3
res = sl.searchRange(nums, target)
print('res', res)