from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # 1. init
        s = []
        sum_val = 0

        # 2. loop
        for o in ops:
            if o == 'C':
                if len(s) > 0:
                    sum_val -= s[-1]
                    s.pop()
            elif o == 'D':
                val = s[-1] * 2
                sum_val += val
                s.append(val)
            elif o == '+':
                val = s[-1] + s[-2]
                sum_val += val
                s.append(val)
            else:
                val = int(o)
                sum_val += val
                s.append(val)
        return sum_val

sl = Solution()

ops = ["5","-2","4","C","D","9","+","+"]

res = sl.calPoints(ops)

print('res', res)