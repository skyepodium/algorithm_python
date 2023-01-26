class Solution:
    def trap(self, height: list[int]) -> int:

        result = 0;

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                result += left_max - height[l]
                l += 1
            else:
                result += right_max - height[r]
                r -= 1

        return result