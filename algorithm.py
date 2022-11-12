from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1. one appearance
        a = [key for key, count in Counter(s).items() if count == 1]

        # 2. loop
        min_idx = len(s) - 1
        res = -1

        for c in a:
            idx = s.index(c)
            if idx <= min_idx:
                min_idx = idx
                res = idx

        return res


sl = Solution()
s = "leetcode"
print(sl.firstUniqChar(s))