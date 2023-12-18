class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX_INT = 10001
        d = [MAX_INT for _ in range(MAX_INT)]
        d[0] = 0

        for idx in range(len(nums)):
            for step in range(1, nums[idx] + 1):
                next_idx = idx + step
                if next_idx <= len(nums) - 1:
                    d[next_idx] = min(d[next_idx], d[idx] + 1)

        return d[len(nums) - 1]
