from typing import List
from collections import Counter

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 1. init
        n = len(words)
        w = [Counter(w) for w in words]
        res = 0

        # 2. loop
        for i in range(n):
            for j in range(i+1, n):
                a, b = w[i], w[j]
                if len(w[i] & w[j]) >= 1: continue

                res = max(res, sum(a.values()) * sum(b.values()))

        return res

sl = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]
res = sl.maxProduct(words)

print('res', res)