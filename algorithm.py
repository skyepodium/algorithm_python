class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def is_even(num):
            return -1 if num % 2 == 0 else 1

        return sorted(nums, key=lambda x: is_even(x))