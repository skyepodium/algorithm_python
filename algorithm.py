from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 1. init
        n = len(words)
        origin = words[0]
        res = []

        # 2. loop
        for w in origin:
            cnt = 0
            for word in words:
                if w in word: cnt += 1
            if n == cnt:
                res.append(w)
                for i in range(n):
                    words[i] = words[i].replace(w, '', 1)

        return res

sl = Solution()

res = sl.commonChars(["cool","lock","cook"])

print('res', res)