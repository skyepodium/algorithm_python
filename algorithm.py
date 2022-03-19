class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(s, e, target):
            if s > e:
                return -1

            mid = s + (e - s) // 2
            if nums[mid] < target:
                return binary_search(mid + 1, e, target)
            elif nums[mid] > target:
                return binary_search(s, mid - 1, target)
            else:
                return mid

        return binary_search(0, len(nums) - 1, target)
