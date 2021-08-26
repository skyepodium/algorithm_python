from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 1. init
        n = int(sqrt(c)) + 1
        d = [x*x for x in range(n)] 
        size = len(d)
        l = 0
        r = size - 1
        
        while l <= r:
            sum_val = d[l] + d[r]
            
            if sum_val < c:
                l += 1
            elif sum_val > c:
                r -= 1
            else:
                return True
        
        return False
