from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # 1. init
        n = len(digits)
        digits.sort()
        s = set()
        res = []

        # 2. get_num
        def get_num(a, b, c):
            return a * 100 + b * 10 + c

        # 3. loop
        for i, a in enumerate(digits):
            if a == 0: continue
            for j, b in enumerate(digits):
                if i == j: continue
                for k, c in enumerate(digits):
                    if i == j or j == k or i == k: continue

                    cur = get_num(a, b, c)
                    if cur not in s and cur % 2 == 0:
                        res.append(cur)
                        s.add(cur)

        return res

sl = Solution()

digits = [2,1,3,0]
digits = [2,2,8,8,2]
res = sl.findEvenNumbers(digits)

print('res', res)