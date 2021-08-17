class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # 1. find min idx
        def min_idx(l, r):
            while l < r:
                mid = l + (r-l) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid

            return l

        pivot_idx = min_idx(0, len(nums) - 1)

        # 2. get_origin_idx
        def get_origin_idx(cur_idx):
            if cur_idx + pivot_idx >= len(nums):
                origin = cur_idx + pivot_idx - len(nums)
            else:
                origin = cur_idx + pivot_idx
            return origin

        # 3. binary_search
        def binary_search(l, r):
            while l <= r:
                mid = l + (r-l) // 2
                origin_mid_idx = get_origin_idx(mid)
                if nums[origin_mid_idx] < target:
                    l = mid + 1
                elif nums[origin_mid_idx] > target:
                    r = mid - 1
                else:
                    return origin_mid_idx

            return -1

        return binary_search(0, len(nums) - 1)

"""
0 1 2 3 - origin
3 0 1 2 - cur
"""

"""
cur = origin + piviot - len

if cur - pivot < 0:
    origin = cur - pivot + len
else:
    origin = cur - pivot
"""

# nums = [4,5,6,7,0,1,2]
# target = 0

nums = [4,5,6,7,0,1,2]
target = 3

nums = [1]
target = 0

nums = [3, 5, 1]
target = 5

sl = Solution()

res = sl.search(nums, target)

print('res', res)


