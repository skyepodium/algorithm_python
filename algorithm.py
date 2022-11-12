from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 1. init
        res = 0
        min_diff = float('inf')

        # 2. sort
        nums.sort()

        # 3. loop
        for i in range(len(nums)):
            # 3.1. init
            left = i + 1
            right = len(nums) - 1

            # 3.2. loop
            while left < right:
                # 3.2.1. init
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)

                # 3.2.2. update
                if diff < min_diff:
                    res = sum
                    min_diff = diff

                # 3.2.3. update
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum

        return res

nums = [-1,2,1,-4]
target = 1

# nums = [0,0,0]
# target = 1
sl = Solution()
print(sl.threeSumClosest(nums, target))
