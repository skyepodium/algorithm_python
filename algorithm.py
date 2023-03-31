class Solution:
    def secondHighest(self, s: str) -> int:
        nums = sorted(list(set(sorted([int(num) for num in s if num.isdigit()]))))
        return nums[-2] if len(nums) > 1 else -1
