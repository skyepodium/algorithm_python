class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 0
        max_cnt = 0
        res = -1
        cur = -2147483646
        nums.sort()
        
        for num in nums:
            if cur != num:
                if cnt > max_cnt:
                    max_cnt = cnt
                    res = cur
                
                cur = num
                cnt = 1
            else:
                cnt += 1
            
        if cnt > max_cnt:
            max_cnt = cnt
            res = cur
                           
        return res
            
