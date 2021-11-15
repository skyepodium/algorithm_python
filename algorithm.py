from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(s, e, target):

            while s <= e:
                mid = s + (e - s) // 2
                cur = nums[mid]
                if cur < target:
                    s = mid + 1
                elif cur == target:
                    return mid
                else:
                    e = mid - 1

            return -1

        return binary_search(0, len(nums) - 1, target)
