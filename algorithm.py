from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 if w.find(pref) == 0 else 0 for w in words])
    

sl = Solution()
words = ["leetcode","win","loops","success"]
pref = "code"
res = sl.prefixCount(words, pref)

print('res', res)