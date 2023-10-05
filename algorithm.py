from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # 1. init
        res = []
        n = len(words)

        # 2. loop
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res
