from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 1. init
        n = len(strs)
        m = len(strs[0])
        res = 0

        # 2. loop
        for j in range(m):
            prev = "a"
            is_sorted = True
            for i in range(n):
                if prev <= strs[i][j]:
                    prev = strs[i][j]
                else:
                    is_sorted = False
                    break
            if not is_sorted:
                res += 1

        return res

sl = Solution()
strs = ["cba","daf","ghi"]
strs = ["a","b"]
strs = ["zyx","wvu","tsr"]
res = sl.minDeletionSize(strs)
print('res', res)