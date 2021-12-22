class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 1. init
        n = len(nums)
        result = 0
        
        # 2. loop
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result += 1
        
        return result
