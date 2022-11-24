from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. init
        l, r = 0, len(numbers) - 1

        # 2. two pointer
        while l <= r:
            sum_val = numbers[l] + numbers[r]
            if sum_val < target:
                l += 1
            elif sum_val > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return [-1, -1]